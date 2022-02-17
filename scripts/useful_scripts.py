from webbrowser import get
from brownie import accounts, FundMe, network, MockV3Aggregator
from web3 import Web3

ACTIVE_ACCOUNT = "metamask1"
DECIMALS = 8
STARTING_PRICE = 200000000000
LOCAL_ENVIRONMENTS = ["development", "ganache-local"]
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]


def get_account():
    if (
        network.show_active() in LOCAL_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.load(ACTIVE_ACCOUNT)


def deploy_mock():
    print(f"Deployed network is : {network.show_active()}")
    if len(MockV3Aggregator) <= 0:
        print("Deploying mock ...")
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
    return MockV3Aggregator[-1].address

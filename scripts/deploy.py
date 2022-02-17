from brownie import FundMe, network, config, MockV3Aggregator
from scripts.useful_scripts import get_account, deploy_mock, LOCAL_ENVIRONMENTS


def deploy_fund_me():
    account = get_account()
    print("Deploying contract")

    if network.show_active() not in LOCAL_ENVIRONMENTS:
        print(f"Deployed network is : {network.show_active()}")
        priceFeed_address = config["networks"][network.show_active()]["price_feed"]

    else:

        priceFeed_address = deploy_mock()

    fund_me = FundMe.deploy(
        priceFeed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify_api"],
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()

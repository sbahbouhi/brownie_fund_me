from stat import FILE_ATTRIBUTE_NO_SCRUB_DATA
from brownie import FundMe
from scripts.useful_scripts import get_account


def fund():
    account = get_account()
    fund_me = FundMe[-1]

    entry_fee = fund_me.getEntranceFeeInETH()
    print(f"Entry fee in ETH = {entry_fee}")
    print("Funding ...")
    fund_me.fund({"from": account, "value": entry_fee})


def withdraw():
    account = get_account()
    fund_me = FundMe[-1]
    print("withdrawing ...")
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()

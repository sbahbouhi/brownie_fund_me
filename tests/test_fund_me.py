from brownie import network, accounts, exceptions
from scripts.deploy import deploy_fund_me
from scripts.useful_scripts import (
    get_account,
    LOCAL_ENVIRONMENTS,
    FORKED_LOCAL_ENVIRONMENTS,
)
import pytest


def test_fund_withdraw():
    fund_me = deploy_fund_me()
    account = get_account()
    # Test funding
    funding_amount = fund_me.getEntranceFeeInETH() + 1
    fund_me.fund({"from": account, "value": funding_amount}).wait(1)

    assert funding_amount == fund_me.addressToAmountFunded(account.address)

    # Test withdrawing
    fund_me.withdraw({"from": account}).wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0


def test_only_owner_withdraw():
    if network.show_active() not in LOCAL_ENVIRONMENTS:
        pytest.skip("Only for local environments")

    fund_me = deploy_fund_me()
    bad_actor = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor})

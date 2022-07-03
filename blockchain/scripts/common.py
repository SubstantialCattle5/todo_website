from brownie import accounts, config , network
import web3

DECIMALS = 8
# This is 2,000
INITIAL_VALUE = web3.Web3.toWei(2000, 'ether')

LOCAL_BLOCKCHAIN_ENV = ["development", "ganache-local"]


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENV:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])



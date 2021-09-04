from brownie import AdvancedCollectible, accounts, network, config

from brownie.network.main import show_active

from scripts.helpful_scripts import fund_advanced_collectible


def main():
    dev = accounts.add(config["wallets"]["from_key"])
    
    print(network.show_active())
    
    publish_source = False
    
    advanced_collectible = AdvancedCollectible[len(AdvancedCollectible) - 1]

    fund_advanced_collectible(advanced_collectible)

    return advanced_collectible
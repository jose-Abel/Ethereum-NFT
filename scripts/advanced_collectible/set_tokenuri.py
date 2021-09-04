from brownie import AdvancedCollectible, network, accounts, config

from scripts.helpful_scripts import get_breed

dog_metadata_dic = {
    "PUG": "https://ipfs.io/ipfs/QmQbAgcxXYNPCUMoc3rXfFNi2QqxuyEwE59RM9xWzjvCYF?filename=1-PUG.json",
    
    "SHIBA_INU": "https://ipfs.io/ipfs/QmYGBxMzxTSDYTLRHfWXA3m5xBFRrxU84r2bgBdpQnfgSM?filename=2-SHIBA_INU.json",
    
    "ST_BERNARD": "https://ipfs.io/ipfs/QmcRsSUcq9vGJuPaYFCXEQpMpEQCBmGaKZ2Jwmcr7PP1yQ?filename=0-ST_BERNARD.json"
}

OPENSEA_FORMAT = "https://testnets.opensea.io/assets/{}/{}"

def main():
    advanced_collectible = AdvancedCollectible[len(AdvancedCollectible) - 1]

    number_of_advanced_collectibles = advanced_collectible.tokenCounter()

    print("The number of tokens you've deployed is: " + str(number_of_advanced_collectibles))

    for token_id in range(number_of_advanced_collectibles):
        breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))

        if not advanced_collectible.tokenURI(token_id).startswith("https://"):
            print("Setting tokenURI of {}".format(token_id))

            set_tokenURI(token_id, advanced_collectible, dog_metadata_dic[breed])
        else:
            print("Skipping {}, we've already set that tokenURI".format(token_id))


def set_tokenURI(token_id, nft_contract, tokenURI):
    dev = accounts.add(config["wallets"]["from_key"])

    nft_contract.setTokenURI(token_id, tokenURI, {"from": dev})

    print("Awesome, you can now view your NFT at {}".format(
        OPENSEA_FORMAT.format(nft_contract.address, token_id)
        )
    )

    print("Please give up to 20 minutes, and hit the 'refresh metadata' button")
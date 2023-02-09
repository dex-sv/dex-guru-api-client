from enum import Enum


class NetworkChoices(str, Enum):
    ETH = "eth"
    OPTIMISM = "optimism"
    BSC = "bsc"
    POLYGON = "polygon"
    FANTOM = "fantom"
    ARBITRUM = "arbitrum"
    CELO = "celo"
    AVALANCHE = "avalanche"
    GNOSIS = "gnosis"
    CANTO = "canto"
    OSMOSIS = "osmosis"
    NOVA = "nova"

    def __str__(self) -> str:
        return str(self.value)

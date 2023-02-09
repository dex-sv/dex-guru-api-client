from enum import Enum


class SortChoices(str, Enum):
    ID = "id"
    ADDRESS = "address"
    SYMBOL = "symbol"
    NAME = "name"
    DESCRIPTION = "description"
    TXNS24H = "txns24h"
    TXNS24HCHANGE = "txns24hChange"
    VERIFIED = "verified"
    DECIMALS = "decimals"
    VOLUME24H = "volume24h"
    VOLUME24HUSD = "volume24hUSD"
    VOLUME24HETH = "volume24hETH"
    VOLUMECHANGE24H = "volumeChange24h"
    LIQUIDITYUSD = "liquidityUSD"
    LIQUIDITYETH = "liquidityETH"
    LIQUIDITYCHANGE24H = "liquidityChange24h"
    PRICEUSD = "priceUSD"
    PRICEETH = "priceETH"
    PRICEUSDCHANGE24H = "priceUSDChange24h"
    PRICEETHCHANGE24H = "priceETHChange24h"
    TIMESTAMP = "timestamp"
    BLOCKNUMBER = "blockNumber"
    AMM = "amm"
    NETWORK = "network"

    def __str__(self) -> str:
        return str(self.value)

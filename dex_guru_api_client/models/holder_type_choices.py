from enum import Enum


class HolderTypeChoices(str, Enum):
    WALLET = "wallet"
    SMART_CONTRACT = "smart_contract"
    LIQUIDITY_POOL = "liquidity_pool"
    MEV_BOT = "mev_bot"

    def __str__(self) -> str:
        return str(self.value)

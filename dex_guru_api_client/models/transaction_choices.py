from enum import Enum


class TransactionChoices(str, Enum):
    SWAP = "swap"
    BURN = "burn"
    MINT = "mint"
    TRANSFER = "transfer"

    def __str__(self) -> str:
        return str(self.value)

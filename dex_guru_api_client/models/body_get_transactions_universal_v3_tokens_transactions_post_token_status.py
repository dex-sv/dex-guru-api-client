from enum import Enum


class BodyGetTransactionsUniversalV3TokensTransactionsPostTokenStatus(str, Enum):
    ALL = "all"
    BUY = "buy"
    SELL = "sell"

    def __str__(self) -> str:
        return str(self.value)

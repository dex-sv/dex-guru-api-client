from enum import Enum


class BodyGetTransactionsUniversalCountV3TokensTransactionsCountPostTokenStatus(str, Enum):
    ALL = "all"
    BUY = "buy"
    SELL = "sell"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class MarketTypeChoices(str, Enum):
    TOKEN = "token"
    LP = "lp"
    ACCOUNT = "account"

    def __str__(self) -> str:
        return str(self.value)

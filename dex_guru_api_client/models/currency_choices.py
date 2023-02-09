from enum import Enum


class CurrencyChoices(str, Enum):
    USD = "USD"
    ETH = "ETH"
    S = "S"
    N = "N"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class RestHolderPNLHoldersMakingMoney(str, Enum):
    IN = "in"
    OUT = "out"
    AT_MONEY = "at_money"

    def __str__(self) -> str:
        return str(self.value)

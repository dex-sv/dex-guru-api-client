from enum import Enum


class FilterTokenTradeSizeOperator(str, Enum):
    GT = "gt"
    LT = "lt"
    EQ = "eq"

    def __str__(self) -> str:
        return str(self.value)

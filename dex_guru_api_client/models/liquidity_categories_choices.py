from enum import Enum


class LiquidityCategoriesChoices(str, Enum):
    ROOSTER = "rooster"
    TIGER = "tiger"
    ELEPHANT = "elephant"

    def __str__(self) -> str:
        return str(self.value)

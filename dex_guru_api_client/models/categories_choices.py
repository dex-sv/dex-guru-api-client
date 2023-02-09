from enum import Enum


class CategoriesChoices(str, Enum):
    NOOB = "noob"
    CASUAL = "casual"
    MEDIUM = "medium"
    HEAVY = "heavy"
    BOT = "bot"

    def __str__(self) -> str:
        return str(self.value)

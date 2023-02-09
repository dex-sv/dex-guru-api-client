from enum import Enum


class ChainNodeStatusChoices(str, Enum):
    OK = "OK"
    ERROR = "ERROR"

    def __str__(self) -> str:
        return str(self.value)

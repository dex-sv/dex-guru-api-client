from enum import Enum


class GetProfileHoldersWithPnlV2TokensTokenIdProfileHoldersPnlGetPeriod(str, Enum):
    DAY = "day"
    WEEK = "week"
    MONTH = "month"
    ALL_TIME = "all_time"

    def __str__(self) -> str:
        return str(self.value)

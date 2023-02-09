from enum import Enum


class TokenHoldersCategoriesOvertimeV2TokensTokenIdHoldersCategoriesChartGetPeriod(str, Enum):
    WEEK = "week"
    MONTH = "month"
    ALL_TIME = "all_time"

    def __str__(self) -> str:
        return str(self.value)

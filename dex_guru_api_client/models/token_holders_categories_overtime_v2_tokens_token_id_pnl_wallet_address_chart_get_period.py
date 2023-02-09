from enum import Enum


class TokenHoldersCategoriesOvertimeV2TokensTokenIdPnlWalletAddressChartGetPeriod(str, Enum):
    DAY = "day"
    WEEK = "week"
    MONTH = "month"
    QUARTER = "quarter"
    ALL_TIME = "all_time"

    def __str__(self) -> str:
        return str(self.value)

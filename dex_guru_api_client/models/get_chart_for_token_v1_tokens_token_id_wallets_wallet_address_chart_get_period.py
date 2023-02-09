from enum import Enum


class GetChartForTokenV1TokensTokenIdWalletsWalletAddressChartGetPeriod(str, Enum):
    DAY = "day"
    WEEK = "week"
    MONTH = "month"
    ALL_TIME = "all_time"

    def __str__(self) -> str:
        return str(self.value)

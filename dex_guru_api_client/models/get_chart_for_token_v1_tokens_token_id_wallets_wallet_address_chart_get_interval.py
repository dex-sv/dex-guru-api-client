from enum import Enum


class GetChartForTokenV1TokensTokenIdWalletsWalletAddressChartGetInterval(str, Enum):
    HOUR = "hour"
    DAY = "day"
    WEEK = "week"

    def __str__(self) -> str:
        return str(self.value)

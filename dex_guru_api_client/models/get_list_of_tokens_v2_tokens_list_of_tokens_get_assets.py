from enum import Enum


class GetListOfTokensV2TokensListOfTokensGetAssets(str, Enum):
    ALL = "all"
    NEW_LISTED = "new_listed"
    GAINERS = "gainers"
    LOSERS = "losers"

    def __str__(self) -> str:
        return str(self.value)

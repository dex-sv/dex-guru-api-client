from enum import Enum


class GetProfileHoldersWithPnlV2TokensTokenIdProfileHoldersPnlGetSortBy(str, Enum):
    REALIZED = "realized"
    UNREALIZED = "unrealized"
    TOP_BUYERS = "top_buyers"
    TOP_SELLERS = "top_sellers"

    def __str__(self) -> str:
        return str(self.value)

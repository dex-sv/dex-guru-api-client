from enum import Enum


class PoolSortChoices(str, Enum):
    VOLUME24H_STABLE = "volume24h_stable"
    VOLUME24H_NATIVE = "volume24h_native"
    LIQUIDITY_STABLE = "liquidity_stable"
    LIQUIDITY_NATIVE = "liquidity_native"

    def __str__(self) -> str:
        return str(self.value)

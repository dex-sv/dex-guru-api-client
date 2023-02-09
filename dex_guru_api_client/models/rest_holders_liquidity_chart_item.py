from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="RestHoldersLiquidityChartItem")


@attr.s(auto_attribs=True)
class RestHoldersLiquidityChartItem:
    """
    Attributes:
        timestamp (int):
        liquidity_providers_count (int):
        percent_liquidity_in_supply (float):
    """

    timestamp: int
    liquidity_providers_count: int
    percent_liquidity_in_supply: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp = self.timestamp
        liquidity_providers_count = self.liquidity_providers_count
        percent_liquidity_in_supply = self.percent_liquidity_in_supply

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "liquidityProvidersCount": liquidity_providers_count,
                "percentLiquidityInSupply": percent_liquidity_in_supply,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        timestamp = d.pop("timestamp")

        liquidity_providers_count = d.pop("liquidityProvidersCount")

        percent_liquidity_in_supply = d.pop("percentLiquidityInSupply")

        rest_holders_liquidity_chart_item = cls(
            timestamp=timestamp,
            liquidity_providers_count=liquidity_providers_count,
            percent_liquidity_in_supply=percent_liquidity_in_supply,
        )

        rest_holders_liquidity_chart_item.additional_properties = d
        return rest_holders_liquidity_chart_item

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

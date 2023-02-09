from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestChartPoint")


@attr.s(auto_attribs=True)
class RestChartPoint:
    """
    Attributes:
        timestamp (int):
        price (Union[Unset, float]):
        volume (Union[Unset, float]):
    """

    timestamp: int
    price: Union[Unset, float] = 0.0
    volume: Union[Unset, float] = 0.0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp = self.timestamp
        price = self.price
        volume = self.volume

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
            }
        )
        if price is not UNSET:
            field_dict["price"] = price
        if volume is not UNSET:
            field_dict["volume"] = volume

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        timestamp = d.pop("timestamp")

        price = d.pop("price", UNSET)

        volume = d.pop("volume", UNSET)

        rest_chart_point = cls(
            timestamp=timestamp,
            price=price,
            volume=volume,
        )

        rest_chart_point.additional_properties = d
        return rest_chart_point

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

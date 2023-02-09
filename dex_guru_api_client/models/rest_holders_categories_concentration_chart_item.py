from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestHoldersCategoriesConcentrationChartItem")


@attr.s(auto_attribs=True)
class RestHoldersCategoriesConcentrationChartItem:
    """
    Attributes:
        timestamp (int):
        casual (Union[Unset, int]):
        medium (Union[Unset, int]):
        heavy (Union[Unset, int]):
        other (Union[Unset, int]):
    """

    timestamp: int
    casual: Union[Unset, int] = 0
    medium: Union[Unset, int] = 0
    heavy: Union[Unset, int] = 0
    other: Union[Unset, int] = 0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp = self.timestamp
        casual = self.casual
        medium = self.medium
        heavy = self.heavy
        other = self.other

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
            }
        )
        if casual is not UNSET:
            field_dict["casual"] = casual
        if medium is not UNSET:
            field_dict["medium"] = medium
        if heavy is not UNSET:
            field_dict["heavy"] = heavy
        if other is not UNSET:
            field_dict["other"] = other

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        timestamp = d.pop("timestamp")

        casual = d.pop("casual", UNSET)

        medium = d.pop("medium", UNSET)

        heavy = d.pop("heavy", UNSET)

        other = d.pop("other", UNSET)

        rest_holders_categories_concentration_chart_item = cls(
            timestamp=timestamp,
            casual=casual,
            medium=medium,
            heavy=heavy,
            other=other,
        )

        rest_holders_categories_concentration_chart_item.additional_properties = d
        return rest_holders_categories_concentration_chart_item

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

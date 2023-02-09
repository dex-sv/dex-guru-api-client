from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestBalanceDistribution")


@attr.s(auto_attribs=True)
class RestBalanceDistribution:
    """
    Attributes:
        field_0_10 (Union[Unset, int]):
        field_10_50 (Union[Unset, int]):
        field_50_100 (Union[Unset, int]):
        field_100_250 (Union[Unset, int]):
        field_250_500 (Union[Unset, int]):
        field_500 (Union[Unset, int]):
        total (Union[Unset, int]):
    """

    field_0_10: Union[Unset, int] = 0
    field_10_50: Union[Unset, int] = 0
    field_50_100: Union[Unset, int] = 0
    field_100_250: Union[Unset, int] = 0
    field_250_500: Union[Unset, int] = 0
    field_500: Union[Unset, int] = 0
    total: Union[Unset, int] = 0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_0_10 = self.field_0_10
        field_10_50 = self.field_10_50
        field_50_100 = self.field_50_100
        field_100_250 = self.field_100_250
        field_250_500 = self.field_250_500
        field_500 = self.field_500
        total = self.total

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_0_10 is not UNSET:
            field_dict["0_10"] = field_0_10
        if field_10_50 is not UNSET:
            field_dict["10_50"] = field_10_50
        if field_50_100 is not UNSET:
            field_dict["50_100"] = field_50_100
        if field_100_250 is not UNSET:
            field_dict["100_250"] = field_100_250
        if field_250_500 is not UNSET:
            field_dict["250_500"] = field_250_500
        if field_500 is not UNSET:
            field_dict["500_"] = field_500
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field_0_10 = d.pop("0_10", UNSET)

        field_10_50 = d.pop("10_50", UNSET)

        field_50_100 = d.pop("50_100", UNSET)

        field_100_250 = d.pop("100_250", UNSET)

        field_250_500 = d.pop("250_500", UNSET)

        field_500 = d.pop("500_", UNSET)

        total = d.pop("total", UNSET)

        rest_balance_distribution = cls(
            field_0_10=field_0_10,
            field_10_50=field_10_50,
            field_50_100=field_50_100,
            field_100_250=field_100_250,
            field_250_500=field_250_500,
            field_500=field_500,
            total=total,
        )

        rest_balance_distribution.additional_properties = d
        return rest_balance_distribution

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

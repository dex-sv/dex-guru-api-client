from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="RestHoldingTimeDistribution")


@attr.s(auto_attribs=True)
class RestHoldingTimeDistribution:
    """
    Attributes:
        field_24 (int):
        field_1_7 (int):
        field_7_30 (int):
        field_30_90 (int):
        field_90_180 (int):
        field_180 (int):
    """

    field_24: int
    field_1_7: int
    field_7_30: int
    field_30_90: int
    field_90_180: int
    field_180: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_24 = self.field_24
        field_1_7 = self.field_1_7
        field_7_30 = self.field_7_30
        field_30_90 = self.field_30_90
        field_90_180 = self.field_90_180
        field_180 = self.field_180

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "24": field_24,
                "1_7": field_1_7,
                "7_30": field_7_30,
                "30_90": field_30_90,
                "90_180": field_90_180,
                "180": field_180,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field_24 = d.pop("24")

        field_1_7 = d.pop("1_7")

        field_7_30 = d.pop("7_30")

        field_30_90 = d.pop("30_90")

        field_90_180 = d.pop("90_180")

        field_180 = d.pop("180")

        rest_holding_time_distribution = cls(
            field_24=field_24,
            field_1_7=field_1_7,
            field_7_30=field_7_30,
            field_30_90=field_30_90,
            field_90_180=field_90_180,
            field_180=field_180,
        )

        rest_holding_time_distribution.additional_properties = d
        return rest_holding_time_distribution

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

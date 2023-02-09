from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="RestHoldingTime")


@attr.s(auto_attribs=True)
class RestHoldingTime:
    """
    Attributes:
        median_holding_time (int):
    """

    median_holding_time: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        median_holding_time = self.median_holding_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "medianHoldingTime": median_holding_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        median_holding_time = d.pop("medianHoldingTime")

        rest_holding_time = cls(
            median_holding_time=median_holding_time,
        )

        rest_holding_time.additional_properties = d
        return rest_holding_time

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

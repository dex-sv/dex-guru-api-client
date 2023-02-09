from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="RestMarketScreener")


@attr.s(auto_attribs=True)
class RestMarketScreener:
    """
    Attributes:
        casual (float):
        medium (float):
        heavy (float):
    """

    casual: float
    medium: float
    heavy: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        casual = self.casual
        medium = self.medium
        heavy = self.heavy

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "casual": casual,
                "medium": medium,
                "heavy": heavy,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        casual = d.pop("casual")

        medium = d.pop("medium")

        heavy = d.pop("heavy")

        rest_market_screener = cls(
            casual=casual,
            medium=medium,
            heavy=heavy,
        )

        rest_market_screener.additional_properties = d
        return rest_market_screener

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

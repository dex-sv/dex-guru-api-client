from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="RestLiquidityShare")


@attr.s(auto_attribs=True)
class RestLiquidityShare:
    """
    Attributes:
        lp_provider_category (str):
        share (float):
    """

    lp_provider_category: str
    share: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        lp_provider_category = self.lp_provider_category
        share = self.share

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lp_provider_category": lp_provider_category,
                "share": share,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        lp_provider_category = d.pop("lp_provider_category")

        share = d.pop("share")

        rest_liquidity_share = cls(
            lp_provider_category=lp_provider_category,
            share=share,
        )

        rest_liquidity_share.additional_properties = d
        return rest_liquidity_share

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

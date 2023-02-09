from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestPriceVolume")


@attr.s(auto_attribs=True)
class RestPriceVolume:
    """
    Attributes:
        price_usd (Union[Unset, float]):
        volume_usd (Union[Unset, float]):
        price_eth (Union[Unset, float]):
        volume_eth (Union[Unset, float]):
    """

    price_usd: Union[Unset, float] = 0.0
    volume_usd: Union[Unset, float] = 0.0
    price_eth: Union[Unset, float] = 0.0
    volume_eth: Union[Unset, float] = 0.0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        price_usd = self.price_usd
        volume_usd = self.volume_usd
        price_eth = self.price_eth
        volume_eth = self.volume_eth

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if price_usd is not UNSET:
            field_dict["priceUSD"] = price_usd
        if volume_usd is not UNSET:
            field_dict["volumeUSD"] = volume_usd
        if price_eth is not UNSET:
            field_dict["priceETH"] = price_eth
        if volume_eth is not UNSET:
            field_dict["volumeETH"] = volume_eth

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        price_usd = d.pop("priceUSD", UNSET)

        volume_usd = d.pop("volumeUSD", UNSET)

        price_eth = d.pop("priceETH", UNSET)

        volume_eth = d.pop("volumeETH", UNSET)

        rest_price_volume = cls(
            price_usd=price_usd,
            volume_usd=volume_usd,
            price_eth=price_eth,
            volume_eth=volume_eth,
        )

        rest_price_volume.additional_properties = d
        return rest_price_volume

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

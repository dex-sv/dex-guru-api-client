from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestTrendingPriceMovingPeriod")


@attr.s(auto_attribs=True)
class RestTrendingPriceMovingPeriod:
    """
    Attributes:
        price_move (Union[Unset, float]):
        volume_move (Union[Unset, float]):
    """

    price_move: Union[Unset, float] = 0.0
    volume_move: Union[Unset, float] = 0.0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        price_move = self.price_move
        volume_move = self.volume_move

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if price_move is not UNSET:
            field_dict["priceMove"] = price_move
        if volume_move is not UNSET:
            field_dict["volumeMove"] = volume_move

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        price_move = d.pop("priceMove", UNSET)

        volume_move = d.pop("volumeMove", UNSET)

        rest_trending_price_moving_period = cls(
            price_move=price_move,
            volume_move=volume_move,
        )

        rest_trending_price_moving_period.additional_properties = d
        return rest_trending_price_moving_period

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

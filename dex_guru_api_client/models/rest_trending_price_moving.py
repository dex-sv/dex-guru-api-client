from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_trending_price_moving_period import RestTrendingPriceMovingPeriod


T = TypeVar("T", bound="RestTrendingPriceMoving")


@attr.s(auto_attribs=True)
class RestTrendingPriceMoving:
    """
    Attributes:
        day (Union[Unset, RestTrendingPriceMovingPeriod]):
        week (Union[Unset, RestTrendingPriceMovingPeriod]):
        month (Union[Unset, RestTrendingPriceMovingPeriod]):
    """

    day: Union[Unset, "RestTrendingPriceMovingPeriod"] = UNSET
    week: Union[Unset, "RestTrendingPriceMovingPeriod"] = UNSET
    month: Union[Unset, "RestTrendingPriceMovingPeriod"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        day: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.day, Unset):
            day = self.day.to_dict()

        week: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.week, Unset):
            week = self.week.to_dict()

        month: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.month, Unset):
            month = self.month.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if day is not UNSET:
            field_dict["day"] = day
        if week is not UNSET:
            field_dict["week"] = week
        if month is not UNSET:
            field_dict["month"] = month

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.rest_trending_price_moving_period import RestTrendingPriceMovingPeriod

        d = src_dict.copy()
        _day = d.pop("day", UNSET)
        day: Union[Unset, RestTrendingPriceMovingPeriod]
        if isinstance(_day, Unset):
            day = UNSET
        else:
            day = RestTrendingPriceMovingPeriod.from_dict(_day)

        _week = d.pop("week", UNSET)
        week: Union[Unset, RestTrendingPriceMovingPeriod]
        if isinstance(_week, Unset):
            week = UNSET
        else:
            week = RestTrendingPriceMovingPeriod.from_dict(_week)

        _month = d.pop("month", UNSET)
        month: Union[Unset, RestTrendingPriceMovingPeriod]
        if isinstance(_month, Unset):
            month = UNSET
        else:
            month = RestTrendingPriceMovingPeriod.from_dict(_month)

        rest_trending_price_moving = cls(
            day=day,
            week=week,
            month=month,
        )

        rest_trending_price_moving.additional_properties = d
        return rest_trending_price_moving

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

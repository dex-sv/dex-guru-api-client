from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestBalanceMark")


@attr.s(auto_attribs=True)
class RestBalanceMark:
    """
    Attributes:
        price (Union[Unset, float]):
        balance (Union[Unset, float]):
        timestamp (Union[Unset, int]):
    """

    price: Union[Unset, float] = 0.0
    balance: Union[Unset, float] = 0.0
    timestamp: Union[Unset, int] = 0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        price = self.price
        balance = self.balance
        timestamp = self.timestamp

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if price is not UNSET:
            field_dict["price"] = price
        if balance is not UNSET:
            field_dict["balance"] = balance
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        price = d.pop("price", UNSET)

        balance = d.pop("balance", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        rest_balance_mark = cls(
            price=price,
            balance=balance,
            timestamp=timestamp,
        )

        rest_balance_mark.additional_properties = d
        return rest_balance_mark

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

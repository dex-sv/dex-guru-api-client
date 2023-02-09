from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.filter_trade_size_usd_operator import FilterTradeSizeUSDOperator
from ..types import UNSET, Unset

T = TypeVar("T", bound="FilterTradeSizeUSD")


@attr.s(auto_attribs=True)
class FilterTradeSizeUSD:
    """
    Attributes:
        amount (float):
        operator (Union[Unset, FilterTradeSizeUSDOperator]):  Default: FilterTradeSizeUSDOperator.GT.
    """

    amount: float
    operator: Union[Unset, FilterTradeSizeUSDOperator] = FilterTradeSizeUSDOperator.GT
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount
        operator: Union[Unset, str] = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
            }
        )
        if operator is not UNSET:
            field_dict["operator"] = operator

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amount = d.pop("amount")

        _operator = d.pop("operator", UNSET)
        operator: Union[Unset, FilterTradeSizeUSDOperator]
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = FilterTradeSizeUSDOperator(_operator)

        filter_trade_size_usd = cls(
            amount=amount,
            operator=operator,
        )

        filter_trade_size_usd.additional_properties = d
        return filter_trade_size_usd

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

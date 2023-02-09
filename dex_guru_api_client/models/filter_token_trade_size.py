from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.filter_token_trade_size_operator import FilterTokenTradeSizeOperator
from ..types import UNSET, Unset

T = TypeVar("T", bound="FilterTokenTradeSize")


@attr.s(auto_attribs=True)
class FilterTokenTradeSize:
    """
    Attributes:
        token_address (str):
        amount (float):
        operator (Union[Unset, FilterTokenTradeSizeOperator]):  Default: FilterTokenTradeSizeOperator.GT.
    """

    token_address: str
    amount: float
    operator: Union[Unset, FilterTokenTradeSizeOperator] = FilterTokenTradeSizeOperator.GT
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        token_address = self.token_address
        amount = self.amount
        operator: Union[Unset, str] = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token_address": token_address,
                "amount": amount,
            }
        )
        if operator is not UNSET:
            field_dict["operator"] = operator

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        token_address = d.pop("token_address")

        amount = d.pop("amount")

        _operator = d.pop("operator", UNSET)
        operator: Union[Unset, FilterTokenTradeSizeOperator]
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = FilterTokenTradeSizeOperator(_operator)

        filter_token_trade_size = cls(
            token_address=token_address,
            amount=amount,
            operator=operator,
        )

        filter_token_trade_size.additional_properties = d
        return filter_token_trade_size

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

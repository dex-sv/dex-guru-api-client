from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="RestLpToken")


@attr.s(auto_attribs=True)
class RestLpToken:
    """
    Attributes:
        address (str):
        symbol (str):
        amount (float):
        amount_stable (float):
        amount_native (float):
        price_stable (float):
        price_native (float):
    """

    address: str
    symbol: str
    amount: float
    amount_stable: float
    amount_native: float
    price_stable: float
    price_native: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address = self.address
        symbol = self.symbol
        amount = self.amount
        amount_stable = self.amount_stable
        amount_native = self.amount_native
        price_stable = self.price_stable
        price_native = self.price_native

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "address": address,
                "symbol": symbol,
                "amount": amount,
                "amountStable": amount_stable,
                "amountNative": amount_native,
                "priceStable": price_stable,
                "priceNative": price_native,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        address = d.pop("address")

        symbol = d.pop("symbol")

        amount = d.pop("amount")

        amount_stable = d.pop("amountStable")

        amount_native = d.pop("amountNative")

        price_stable = d.pop("priceStable")

        price_native = d.pop("priceNative")

        rest_lp_token = cls(
            address=address,
            symbol=symbol,
            amount=amount,
            amount_stable=amount_stable,
            amount_native=amount_native,
            price_stable=price_stable,
            price_native=price_native,
        )

        rest_lp_token.additional_properties = d
        return rest_lp_token

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

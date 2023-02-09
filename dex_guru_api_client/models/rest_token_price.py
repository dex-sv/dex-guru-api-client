from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="RestTokenPrice")


@attr.s(auto_attribs=True)
class RestTokenPrice:
    """
    Attributes:
        address (str):
        token_price_usd (float):
        token_price_eth (float):
    """

    address: str
    token_price_usd: float
    token_price_eth: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address = self.address
        token_price_usd = self.token_price_usd
        token_price_eth = self.token_price_eth

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "address": address,
                "token_price_usd": token_price_usd,
                "token_price_eth": token_price_eth,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        address = d.pop("address")

        token_price_usd = d.pop("token_price_usd")

        token_price_eth = d.pop("token_price_eth")

        rest_token_price = cls(
            address=address,
            token_price_usd=token_price_usd,
            token_price_eth=token_price_eth,
        )

        rest_token_price.additional_properties = d
        return rest_token_price

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

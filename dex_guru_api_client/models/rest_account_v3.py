from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestAccountV3")


@attr.s(auto_attribs=True)
class RestAccountV3:
    """
    Attributes:
        wallet_category (str):
        market_type (Union[Unset, str]):  Default: 'account'.
        address (Union[Unset, str]):
    """

    wallet_category: str
    market_type: Union[Unset, str] = "account"
    address: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        wallet_category = self.wallet_category
        market_type = self.market_type
        address = self.address

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "wallet_category": wallet_category,
            }
        )
        if market_type is not UNSET:
            field_dict["marketType"] = market_type
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        wallet_category = d.pop("wallet_category")

        market_type = d.pop("marketType", UNSET)

        address = d.pop("address", UNSET)

        rest_account_v3 = cls(
            wallet_category=wallet_category,
            market_type=market_type,
            address=address,
        )

        rest_account_v3.additional_properties = d
        return rest_account_v3

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

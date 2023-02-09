from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestTokenInventoryStatic")


@attr.s(auto_attribs=True)
class RestTokenInventoryStatic:
    """
    Attributes:
        id (Union[Unset, str]):
        address (Union[Unset, str]):
        name (Union[Unset, str]):
        symbol (Union[Unset, str]):
        decimals (Union[Unset, int]):
    """

    id: Union[Unset, str] = UNSET
    address: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    symbol: Union[Unset, str] = UNSET
    decimals: Union[Unset, int] = 0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        address = self.address
        name = self.name
        symbol = self.symbol
        decimals = self.decimals

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if address is not UNSET:
            field_dict["address"] = address
        if name is not UNSET:
            field_dict["name"] = name
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if decimals is not UNSET:
            field_dict["decimals"] = decimals

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        address = d.pop("address", UNSET)

        name = d.pop("name", UNSET)

        symbol = d.pop("symbol", UNSET)

        decimals = d.pop("decimals", UNSET)

        rest_token_inventory_static = cls(
            id=id,
            address=address,
            name=name,
            symbol=symbol,
            decimals=decimals,
        )

        rest_token_inventory_static.additional_properties = d
        return rest_token_inventory_static

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

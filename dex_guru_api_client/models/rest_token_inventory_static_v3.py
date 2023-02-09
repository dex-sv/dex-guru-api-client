from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestTokenInventoryStaticV3")


@attr.s(auto_attribs=True)
class RestTokenInventoryStaticV3:
    """
    Attributes:
        id (Union[Unset, str]):
        address (Union[Unset, str]):
        name (Union[Unset, str]):
        symbols (Union[List[str], Unset, str]):  Default: [].
        logo_uri (Union[List[str], Unset, str]):  Default: [].
        decimals (Union[Unset, int]):
    """

    id: Union[Unset, str] = UNSET
    address: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    symbols: Union[List[str], Unset, str] = []
    logo_uri: Union[List[str], Unset, str] = []
    decimals: Union[Unset, int] = 0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        address = self.address
        name = self.name
        symbols: Union[List[str], Unset, str]
        if isinstance(self.symbols, Unset):
            symbols = UNSET

        elif isinstance(self.symbols, list):
            symbols = UNSET
            if not isinstance(self.symbols, Unset):
                symbols = self.symbols

        else:
            symbols = self.symbols

        logo_uri: Union[List[str], Unset, str]
        if isinstance(self.logo_uri, Unset):
            logo_uri = UNSET

        elif isinstance(self.logo_uri, list):
            logo_uri = UNSET
            if not isinstance(self.logo_uri, Unset):
                logo_uri = self.logo_uri

        else:
            logo_uri = self.logo_uri

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
        if symbols is not UNSET:
            field_dict["symbols"] = symbols
        if logo_uri is not UNSET:
            field_dict["logoURI"] = logo_uri
        if decimals is not UNSET:
            field_dict["decimals"] = decimals

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        address = d.pop("address", UNSET)

        name = d.pop("name", UNSET)

        def _parse_symbols(data: object) -> Union[List[str], Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                symbols_type_0 = cast(List[str], data)

                return symbols_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], Unset, str], data)

        symbols = _parse_symbols(d.pop("symbols", UNSET))

        def _parse_logo_uri(data: object) -> Union[List[str], Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                logo_uri_type_0 = cast(List[str], data)

                return logo_uri_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], Unset, str], data)

        logo_uri = _parse_logo_uri(d.pop("logoURI", UNSET))

        decimals = d.pop("decimals", UNSET)

        rest_token_inventory_static_v3 = cls(
            id=id,
            address=address,
            name=name,
            symbols=symbols,
            logo_uri=logo_uri,
            decimals=decimals,
        )

        rest_token_inventory_static_v3.additional_properties = d
        return rest_token_inventory_static_v3

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

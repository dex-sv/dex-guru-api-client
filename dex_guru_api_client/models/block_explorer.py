from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="BlockExplorer")


@attr.s(auto_attribs=True)
class BlockExplorer:
    """
    Attributes:
        url (Union[Unset, str]):
        logo_uri (Union[Unset, str]):
        display_name (Union[Unset, str]):
        token_path (Union[Unset, str]):
        address_path (Union[Unset, str]):
    """

    url: Union[Unset, str] = UNSET
    logo_uri: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    token_path: Union[Unset, str] = UNSET
    address_path: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        logo_uri = self.logo_uri
        display_name = self.display_name
        token_path = self.token_path
        address_path = self.address_path

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if logo_uri is not UNSET:
            field_dict["logo_uri"] = logo_uri
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if token_path is not UNSET:
            field_dict["token_path"] = token_path
        if address_path is not UNSET:
            field_dict["address_path"] = address_path

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url", UNSET)

        logo_uri = d.pop("logo_uri", UNSET)

        display_name = d.pop("display_name", UNSET)

        token_path = d.pop("token_path", UNSET)

        address_path = d.pop("address_path", UNSET)

        block_explorer = cls(
            url=url,
            logo_uri=logo_uri,
            display_name=display_name,
            token_path=token_path,
            address_path=address_path,
        )

        block_explorer.additional_properties = d
        return block_explorer

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

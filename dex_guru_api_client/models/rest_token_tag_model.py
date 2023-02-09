from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestTokenTagModel")


@attr.s(auto_attribs=True)
class RestTokenTagModel:
    """
    Attributes:
        tag_name (str):
        short_name (str):
        description (str):
        id (Union[Unset, str]):
        logo_uri (Union[Unset, str]):
        tag_type (Union[Unset, str]):  Default: 'inclusive'.
    """

    tag_name: str
    short_name: str
    description: str
    id: Union[Unset, str] = UNSET
    logo_uri: Union[Unset, str] = UNSET
    tag_type: Union[Unset, str] = "inclusive"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tag_name = self.tag_name
        short_name = self.short_name
        description = self.description
        id = self.id
        logo_uri = self.logo_uri
        tag_type = self.tag_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tag_name": tag_name,
                "short_name": short_name,
                "description": description,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if logo_uri is not UNSET:
            field_dict["logo_uri"] = logo_uri
        if tag_type is not UNSET:
            field_dict["tag_type"] = tag_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tag_name = d.pop("tag_name")

        short_name = d.pop("short_name")

        description = d.pop("description")

        id = d.pop("id", UNSET)

        logo_uri = d.pop("logo_uri", UNSET)

        tag_type = d.pop("tag_type", UNSET)

        rest_token_tag_model = cls(
            tag_name=tag_name,
            short_name=short_name,
            description=description,
            id=id,
            logo_uri=logo_uri,
            tag_type=tag_type,
        )

        rest_token_tag_model.additional_properties = d
        return rest_token_tag_model

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

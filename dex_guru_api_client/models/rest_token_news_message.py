from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestTokenNewsMessage")


@attr.s(auto_attribs=True)
class RestTokenNewsMessage:
    """
    Attributes:
        id (Union[Unset, str]):
        text (Union[Unset, str]):
        name (Union[Unset, str]):
        pic (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    pic: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        text = self.text
        name = self.name
        pic = self.pic

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if text is not UNSET:
            field_dict["text"] = text
        if name is not UNSET:
            field_dict["name"] = name
        if pic is not UNSET:
            field_dict["pic"] = pic

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        text = d.pop("text", UNSET)

        name = d.pop("name", UNSET)

        pic = d.pop("pic", UNSET)

        rest_token_news_message = cls(
            id=id,
            text=text,
            name=name,
            pic=pic,
        )

        rest_token_news_message.additional_properties = d
        return rest_token_news_message

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

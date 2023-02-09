from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_token_history import RestTokenHistory


T = TypeVar("T", bound="RestTokensHistory")


@attr.s(auto_attribs=True)
class RestTokensHistory:
    """
    Attributes:
        total (Union[Unset, int]):
        data (Union[Unset, List['RestTokenHistory']]):
    """

    total: Union[Unset, int] = 0
    data: Union[Unset, List["RestTokenHistory"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total = self.total
        data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()

                data.append(data_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.rest_token_history import RestTokenHistory

        d = src_dict.copy()
        total = d.pop("total", UNSET)

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = RestTokenHistory.from_dict(data_item_data)

            data.append(data_item)

        rest_tokens_history = cls(
            total=total,
            data=data,
        )

        rest_tokens_history.additional_properties = d
        return rest_tokens_history

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

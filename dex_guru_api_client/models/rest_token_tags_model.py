from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.rest_token_tag_model import RestTokenTagModel


T = TypeVar("T", bound="RestTokenTagsModel")


@attr.s(auto_attribs=True)
class RestTokenTagsModel:
    """
    Attributes:
        total (int):
        data (List['RestTokenTagModel']):
    """

    total: int
    data: List["RestTokenTagModel"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total = self.total
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()

            data.append(data_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.rest_token_tag_model import RestTokenTagModel

        d = src_dict.copy()
        total = d.pop("total")

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = RestTokenTagModel.from_dict(data_item_data)

            data.append(data_item)

        rest_token_tags_model = cls(
            total=total,
            data=data,
        )

        rest_token_tags_model.additional_properties = d
        return rest_token_tags_model

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

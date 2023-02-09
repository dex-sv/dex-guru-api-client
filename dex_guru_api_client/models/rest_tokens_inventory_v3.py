from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_account_v3 import RestAccountV3
    from ..models.rest_token_inventory_v3 import RestTokenInventoryV3


T = TypeVar("T", bound="RestTokensInventoryV3")


@attr.s(auto_attribs=True)
class RestTokensInventoryV3:
    """
    Attributes:
        total (Union[Unset, int]):
        data (Union[Unset, List[Union['RestAccountV3', 'RestTokenInventoryV3']]]):
    """

    total: Union[Unset, int] = 0
    data: Union[Unset, List[Union["RestAccountV3", "RestTokenInventoryV3"]]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.rest_account_v3 import RestAccountV3

        total = self.total
        data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item: Dict[str, Any]

                if isinstance(data_item_data, RestAccountV3):
                    data_item = data_item_data.to_dict()

                else:
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
        from ..models.rest_account_v3 import RestAccountV3
        from ..models.rest_token_inventory_v3 import RestTokenInventoryV3

        d = src_dict.copy()
        total = d.pop("total", UNSET)

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:

            def _parse_data_item(data: object) -> Union["RestAccountV3", "RestTokenInventoryV3"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    data_item_type_0 = RestAccountV3.from_dict(data)

                    return data_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                data_item_type_1 = RestTokenInventoryV3.from_dict(data)

                return data_item_type_1

            data_item = _parse_data_item(data_item_data)

            data.append(data_item)

        rest_tokens_inventory_v3 = cls(
            total=total,
            data=data,
        )

        rest_tokens_inventory_v3.additional_properties = d
        return rest_tokens_inventory_v3

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

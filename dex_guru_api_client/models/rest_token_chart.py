from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_token_chart_item import RestTokenChartItem


T = TypeVar("T", bound="RestTokenChart")


@attr.s(auto_attribs=True)
class RestTokenChart:
    """
    Attributes:
        token_id (str):
        wallet_address (str):
        data (Union[Unset, List['RestTokenChartItem']]):
    """

    token_id: str
    wallet_address: str
    data: Union[Unset, List["RestTokenChartItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        token_id = self.token_id
        wallet_address = self.wallet_address
        data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()

                data.append(data_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tokenID": token_id,
                "walletAddress": wallet_address,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.rest_token_chart_item import RestTokenChartItem

        d = src_dict.copy()
        token_id = d.pop("tokenID")

        wallet_address = d.pop("walletAddress")

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = RestTokenChartItem.from_dict(data_item_data)

            data.append(data_item)

        rest_token_chart = cls(
            token_id=token_id,
            wallet_address=wallet_address,
            data=data,
        )

        rest_token_chart.additional_properties = d
        return rest_token_chart

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

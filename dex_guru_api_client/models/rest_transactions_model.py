from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_burn_model import RestBurnModel
    from ..models.rest_mint_model import RestMintModel
    from ..models.rest_swap_model import RestSwapModel
    from ..models.rest_transfer_model import RestTransferModel


T = TypeVar("T", bound="RestTransactionsModel")


@attr.s(auto_attribs=True)
class RestTransactionsModel:
    """
    Attributes:
        data (List[Union['RestBurnModel', 'RestMintModel', 'RestSwapModel', 'RestTransferModel']]):
        total (Union[Unset, int]):
    """

    data: List[Union["RestBurnModel", "RestMintModel", "RestSwapModel", "RestTransferModel"]]
    total: Union[Unset, int] = 0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.rest_burn_model import RestBurnModel
        from ..models.rest_mint_model import RestMintModel
        from ..models.rest_swap_model import RestSwapModel

        data = []
        for data_item_data in self.data:
            data_item: Dict[str, Any]

            if isinstance(data_item_data, RestSwapModel):
                data_item = data_item_data.to_dict()

            elif isinstance(data_item_data, RestBurnModel):
                data_item = data_item_data.to_dict()

            elif isinstance(data_item_data, RestMintModel):
                data_item = data_item_data.to_dict()

            else:
                data_item = data_item_data.to_dict()

            data.append(data_item)

        total = self.total

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.rest_burn_model import RestBurnModel
        from ..models.rest_mint_model import RestMintModel
        from ..models.rest_swap_model import RestSwapModel
        from ..models.rest_transfer_model import RestTransferModel

        d = src_dict.copy()
        data = []
        _data = d.pop("data")
        for data_item_data in _data:

            def _parse_data_item(
                data: object,
            ) -> Union["RestBurnModel", "RestMintModel", "RestSwapModel", "RestTransferModel"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    data_item_type_0 = RestSwapModel.from_dict(data)

                    return data_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    data_item_type_1 = RestBurnModel.from_dict(data)

                    return data_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    data_item_type_2 = RestMintModel.from_dict(data)

                    return data_item_type_2
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                data_item_type_3 = RestTransferModel.from_dict(data)

                return data_item_type_3

            data_item = _parse_data_item(data_item_data)

            data.append(data_item)

        total = d.pop("total", UNSET)

        rest_transactions_model = cls(
            data=data,
            total=total,
        )

        rest_transactions_model.additional_properties = d
        return rest_transactions_model

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

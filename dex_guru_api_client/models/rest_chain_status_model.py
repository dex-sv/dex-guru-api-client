from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.chain_node_status_choices import ChainNodeStatusChoices
from ..types import UNSET, Unset

T = TypeVar("T", bound="RestChainStatusModel")


@attr.s(auto_attribs=True)
class RestChainStatusModel:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        last_indexed_block (Union[Unset, int]):
        last_indexed_block_timestamp (Union[Unset, int]):
        node_status (Union[Unset, ChainNodeStatusChoices]): An enumeration. Default: ChainNodeStatusChoices.OK.
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    last_indexed_block: Union[Unset, int] = 0
    last_indexed_block_timestamp: Union[Unset, int] = 0
    node_status: Union[Unset, ChainNodeStatusChoices] = ChainNodeStatusChoices.OK
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        last_indexed_block = self.last_indexed_block
        last_indexed_block_timestamp = self.last_indexed_block_timestamp
        node_status: Union[Unset, str] = UNSET
        if not isinstance(self.node_status, Unset):
            node_status = self.node_status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if last_indexed_block is not UNSET:
            field_dict["last_indexed_block"] = last_indexed_block
        if last_indexed_block_timestamp is not UNSET:
            field_dict["last_indexed_block_timestamp"] = last_indexed_block_timestamp
        if node_status is not UNSET:
            field_dict["node_status"] = node_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        last_indexed_block = d.pop("last_indexed_block", UNSET)

        last_indexed_block_timestamp = d.pop("last_indexed_block_timestamp", UNSET)

        _node_status = d.pop("node_status", UNSET)
        node_status: Union[Unset, ChainNodeStatusChoices]
        if isinstance(_node_status, Unset):
            node_status = UNSET
        else:
            node_status = ChainNodeStatusChoices(_node_status)

        rest_chain_status_model = cls(
            id=id,
            name=name,
            last_indexed_block=last_indexed_block,
            last_indexed_block_timestamp=last_indexed_block_timestamp,
            node_status=node_status,
        )

        rest_chain_status_model.additional_properties = d
        return rest_chain_status_model

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

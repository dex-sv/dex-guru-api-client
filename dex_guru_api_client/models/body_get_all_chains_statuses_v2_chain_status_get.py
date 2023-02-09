from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="BodyGetAllChainsStatusesV2ChainStatusGet")


@attr.s(auto_attribs=True)
class BodyGetAllChainsStatusesV2ChainStatusGet:
    """
    Attributes:
        network (Union[Unset, str]): Comma separated list of any networks:
            eth,optimism,bsc,polygon,fantom,arbitrum,celo,avalanche,gnosis,canto,osmosis,nova
    """

    network: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        network = self.network

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if network is not UNSET:
            field_dict["network"] = network

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        network = d.pop("network", UNSET)

        body_get_all_chains_statuses_v2_chain_status_get = cls(
            network=network,
        )

        body_get_all_chains_statuses_v2_chain_status_get.additional_properties = d
        return body_get_all_chains_statuses_v2_chain_status_get

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

from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.amm_choices import AmmChoices
from ..models.network_choices import NetworkChoices
from ..types import UNSET, Unset

T = TypeVar("T", bound="BodyGetTokensPricesByIdsV2TokensPricePost")


@attr.s(auto_attribs=True)
class BodyGetTokensPricesByIdsV2TokensPricePost:
    """
    Attributes:
        ids (Union[Unset, List[str]]): List of ids
        amm (Union[Unset, AmmChoices]): An enumeration. Default: AmmChoices.ALL.
        network (Union[Unset, NetworkChoices]): An enumeration.
    """

    ids: Union[Unset, List[str]] = UNSET
    amm: Union[Unset, AmmChoices] = AmmChoices.ALL
    network: Union[Unset, NetworkChoices] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids

        amm: Union[Unset, str] = UNSET
        if not isinstance(self.amm, Unset):
            amm = self.amm.value

        network: Union[Unset, str] = UNSET
        if not isinstance(self.network, Unset):
            network = self.network.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ids is not UNSET:
            field_dict["ids"] = ids
        if amm is not UNSET:
            field_dict["amm"] = amm
        if network is not UNSET:
            field_dict["network"] = network

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ids = cast(List[str], d.pop("ids", UNSET))

        _amm = d.pop("amm", UNSET)
        amm: Union[Unset, AmmChoices]
        if isinstance(_amm, Unset):
            amm = UNSET
        else:
            amm = AmmChoices(_amm)

        _network = d.pop("network", UNSET)
        network: Union[Unset, NetworkChoices]
        if isinstance(_network, Unset):
            network = UNSET
        else:
            network = NetworkChoices(_network)

        body_get_tokens_prices_by_ids_v2_tokens_price_post = cls(
            ids=ids,
            amm=amm,
            network=network,
        )

        body_get_tokens_prices_by_ids_v2_tokens_price_post.additional_properties = d
        return body_get_tokens_prices_by_ids_v2_tokens_price_post

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

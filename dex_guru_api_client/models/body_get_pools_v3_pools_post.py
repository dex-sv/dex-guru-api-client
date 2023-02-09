from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.network_choices import NetworkChoices
from ..models.order_choices import OrderChoices
from ..models.pool_sort_choices import PoolSortChoices
from ..types import UNSET, Unset

T = TypeVar("T", bound="BodyGetPoolsV3PoolsPost")


@attr.s(auto_attribs=True)
class BodyGetPoolsV3PoolsPost:
    """
    Attributes:
        id (Union[Unset, str]): Token address
        network (Union[Unset, NetworkChoices]): An enumeration.
        amm (Union[Unset, str]): AMM name
        sort_by (Union[Unset, PoolSortChoices]): An enumeration. Default: PoolSortChoices.LIQUIDITY_STABLE.
        order (Union[Unset, OrderChoices]): An enumeration. Default: OrderChoices.DESC.
        limit (Union[Unset, int]): Limit records Default: 50.
    """

    id: Union[Unset, str] = UNSET
    network: Union[Unset, NetworkChoices] = UNSET
    amm: Union[Unset, str] = UNSET
    sort_by: Union[Unset, PoolSortChoices] = PoolSortChoices.LIQUIDITY_STABLE
    order: Union[Unset, OrderChoices] = OrderChoices.DESC
    limit: Union[Unset, int] = 50
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        network: Union[Unset, str] = UNSET
        if not isinstance(self.network, Unset):
            network = self.network.value

        amm = self.amm
        sort_by: Union[Unset, str] = UNSET
        if not isinstance(self.sort_by, Unset):
            sort_by = self.sort_by.value

        order: Union[Unset, str] = UNSET
        if not isinstance(self.order, Unset):
            order = self.order.value

        limit = self.limit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if network is not UNSET:
            field_dict["network"] = network
        if amm is not UNSET:
            field_dict["amm"] = amm
        if sort_by is not UNSET:
            field_dict["sort_by"] = sort_by
        if order is not UNSET:
            field_dict["order"] = order
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _network = d.pop("network", UNSET)
        network: Union[Unset, NetworkChoices]
        if isinstance(_network, Unset):
            network = UNSET
        else:
            network = NetworkChoices(_network)

        amm = d.pop("amm", UNSET)

        _sort_by = d.pop("sort_by", UNSET)
        sort_by: Union[Unset, PoolSortChoices]
        if isinstance(_sort_by, Unset):
            sort_by = UNSET
        else:
            sort_by = PoolSortChoices(_sort_by)

        _order = d.pop("order", UNSET)
        order: Union[Unset, OrderChoices]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = OrderChoices(_order)

        limit = d.pop("limit", UNSET)

        body_get_pools_v3_pools_post = cls(
            id=id,
            network=network,
            amm=amm,
            sort_by=sort_by,
            order=order,
            limit=limit,
        )

        body_get_pools_v3_pools_post.additional_properties = d
        return body_get_pools_v3_pools_post

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

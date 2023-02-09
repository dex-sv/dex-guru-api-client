from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.amm_choices import AmmChoices
from ..models.order_choices import OrderChoices
from ..models.sort_choices import SortChoices
from ..types import UNSET, Unset

T = TypeVar("T", bound="BodyGetTokensByParamsPostV2TokensPost")


@attr.s(auto_attribs=True)
class BodyGetTokensByParamsPostV2TokensPost:
    """
    Attributes:
        amm (Union[Unset, AmmChoices]): An enumeration.
        sort_by (Union[Unset, SortChoices]): An enumeration. Default: SortChoices.LIQUIDITYUSD.
        order (Union[Unset, OrderChoices]): An enumeration. Default: OrderChoices.ASC.
        range_field (Union[Unset, str]): Range field
        range_gt (Union[Unset, float]): Range gt
        range_lt (Union[Unset, float]): Range lt
        range_gte (Union[Unset, float]): Range gte
        range_lte (Union[Unset, float]): Range lte
        field (Union[Unset, str]): Field
        value (Union[Unset, str]): Value
        ids (Union[Unset, List[str]]): Comma separated list of ids
        limit (Union[Unset, int]): Limit records Default: 100.
        offset (Union[Unset, int]): Offset records
        network (Union[Unset, str]): Comma separated list of any networks:
            eth,optimism,bsc,polygon,fantom,arbitrum,celo,avalanche,gnosis,canto,osmosis,nova
    """

    amm: Union[Unset, AmmChoices] = UNSET
    sort_by: Union[Unset, SortChoices] = SortChoices.LIQUIDITYUSD
    order: Union[Unset, OrderChoices] = OrderChoices.ASC
    range_field: Union[Unset, str] = UNSET
    range_gt: Union[Unset, float] = UNSET
    range_lt: Union[Unset, float] = UNSET
    range_gte: Union[Unset, float] = UNSET
    range_lte: Union[Unset, float] = UNSET
    field: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    ids: Union[Unset, List[str]] = UNSET
    limit: Union[Unset, int] = 100
    offset: Union[Unset, int] = 0
    network: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amm: Union[Unset, str] = UNSET
        if not isinstance(self.amm, Unset):
            amm = self.amm.value

        sort_by: Union[Unset, str] = UNSET
        if not isinstance(self.sort_by, Unset):
            sort_by = self.sort_by.value

        order: Union[Unset, str] = UNSET
        if not isinstance(self.order, Unset):
            order = self.order.value

        range_field = self.range_field
        range_gt = self.range_gt
        range_lt = self.range_lt
        range_gte = self.range_gte
        range_lte = self.range_lte
        field = self.field
        value = self.value
        ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids

        limit = self.limit
        offset = self.offset
        network = self.network

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amm is not UNSET:
            field_dict["amm"] = amm
        if sort_by is not UNSET:
            field_dict["sort_by"] = sort_by
        if order is not UNSET:
            field_dict["order"] = order
        if range_field is not UNSET:
            field_dict["range_field"] = range_field
        if range_gt is not UNSET:
            field_dict["range_gt"] = range_gt
        if range_lt is not UNSET:
            field_dict["range_lt"] = range_lt
        if range_gte is not UNSET:
            field_dict["range_gte"] = range_gte
        if range_lte is not UNSET:
            field_dict["range_lte"] = range_lte
        if field is not UNSET:
            field_dict["field"] = field
        if value is not UNSET:
            field_dict["value"] = value
        if ids is not UNSET:
            field_dict["ids"] = ids
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset
        if network is not UNSET:
            field_dict["network"] = network

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _amm = d.pop("amm", UNSET)
        amm: Union[Unset, AmmChoices]
        if isinstance(_amm, Unset):
            amm = UNSET
        else:
            amm = AmmChoices(_amm)

        _sort_by = d.pop("sort_by", UNSET)
        sort_by: Union[Unset, SortChoices]
        if isinstance(_sort_by, Unset):
            sort_by = UNSET
        else:
            sort_by = SortChoices(_sort_by)

        _order = d.pop("order", UNSET)
        order: Union[Unset, OrderChoices]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = OrderChoices(_order)

        range_field = d.pop("range_field", UNSET)

        range_gt = d.pop("range_gt", UNSET)

        range_lt = d.pop("range_lt", UNSET)

        range_gte = d.pop("range_gte", UNSET)

        range_lte = d.pop("range_lte", UNSET)

        field = d.pop("field", UNSET)

        value = d.pop("value", UNSET)

        ids = cast(List[str], d.pop("ids", UNSET))

        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        network = d.pop("network", UNSET)

        body_get_tokens_by_params_post_v2_tokens_post = cls(
            amm=amm,
            sort_by=sort_by,
            order=order,
            range_field=range_field,
            range_gt=range_gt,
            range_lt=range_lt,
            range_gte=range_gte,
            range_lte=range_lte,
            field=field,
            value=value,
            ids=ids,
            limit=limit,
            offset=offset,
            network=network,
        )

        body_get_tokens_by_params_post_v2_tokens_post.additional_properties = d
        return body_get_tokens_by_params_post_v2_tokens_post

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

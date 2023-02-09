from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="BodyGetTrendingForTokensListV2TokensTrendingPost")


@attr.s(auto_attribs=True)
class BodyGetTrendingForTokensListV2TokensTrendingPost:
    """
    Attributes:
        ids (Union[Unset, List[str]]): List of ids
        limit (Union[Unset, int]): Limit of trending tokens list Default: 10.
        only_verified (Union[Unset, bool]): Only verified tokens Default: True.
        network (Union[Unset, str]): Comma separated list of any networks:
            eth,optimism,bsc,polygon,fantom,arbitrum,celo,avalanche,gnosis,canto,osmosis,nova
    """

    ids: Union[Unset, List[str]] = UNSET
    limit: Union[Unset, int] = 10
    only_verified: Union[Unset, bool] = True
    network: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids

        limit = self.limit
        only_verified = self.only_verified
        network = self.network

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ids is not UNSET:
            field_dict["ids"] = ids
        if limit is not UNSET:
            field_dict["limit"] = limit
        if only_verified is not UNSET:
            field_dict["only_verified"] = only_verified
        if network is not UNSET:
            field_dict["network"] = network

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ids = cast(List[str], d.pop("ids", UNSET))

        limit = d.pop("limit", UNSET)

        only_verified = d.pop("only_verified", UNSET)

        network = d.pop("network", UNSET)

        body_get_trending_for_tokens_list_v2_tokens_trending_post = cls(
            ids=ids,
            limit=limit,
            only_verified=only_verified,
            network=network,
        )

        body_get_trending_for_tokens_list_v2_tokens_trending_post.additional_properties = d
        return body_get_trending_for_tokens_list_v2_tokens_trending_post

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

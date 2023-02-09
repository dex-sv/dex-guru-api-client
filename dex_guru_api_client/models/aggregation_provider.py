from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aggregation_provider_spender_addresses_item import AggregationProviderSpenderAddressesItem


T = TypeVar("T", bound="AggregationProvider")


@attr.s(auto_attribs=True)
class AggregationProvider:
    """
    Attributes:
        url (Union[Unset, str]):
        spender_addresses (Union[Unset, List['AggregationProviderSpenderAddressesItem']]):
    """

    url: Union[Unset, str] = UNSET
    spender_addresses: Union[Unset, List["AggregationProviderSpenderAddressesItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        spender_addresses: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.spender_addresses, Unset):
            spender_addresses = []
            for spender_addresses_item_data in self.spender_addresses:
                spender_addresses_item = spender_addresses_item_data.to_dict()

                spender_addresses.append(spender_addresses_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if spender_addresses is not UNSET:
            field_dict["spender_addresses"] = spender_addresses

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.aggregation_provider_spender_addresses_item import AggregationProviderSpenderAddressesItem

        d = src_dict.copy()
        url = d.pop("url", UNSET)

        spender_addresses = []
        _spender_addresses = d.pop("spender_addresses", UNSET)
        for spender_addresses_item_data in _spender_addresses or []:
            spender_addresses_item = AggregationProviderSpenderAddressesItem.from_dict(spender_addresses_item_data)

            spender_addresses.append(spender_addresses_item)

        aggregation_provider = cls(
            url=url,
            spender_addresses=spender_addresses,
        )

        aggregation_provider.additional_properties = d
        return aggregation_provider

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

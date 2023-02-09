from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AggregationProviderDeprecated")


@attr.s(auto_attribs=True)
class AggregationProviderDeprecated:
    """
    Attributes:
        url (Union[Unset, str]):
        wrapper_url (Union[Unset, str]):
        gas_url (Union[Unset, str]):
        wrapper_gas_url (Union[Unset, str]):
        spender_address (Union[Unset, str]):
    """

    url: Union[Unset, str] = UNSET
    wrapper_url: Union[Unset, str] = UNSET
    gas_url: Union[Unset, str] = UNSET
    wrapper_gas_url: Union[Unset, str] = UNSET
    spender_address: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        wrapper_url = self.wrapper_url
        gas_url = self.gas_url
        wrapper_gas_url = self.wrapper_gas_url
        spender_address = self.spender_address

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if wrapper_url is not UNSET:
            field_dict["wrapper_url"] = wrapper_url
        if gas_url is not UNSET:
            field_dict["gas_url"] = gas_url
        if wrapper_gas_url is not UNSET:
            field_dict["wrapper_gas_url"] = wrapper_gas_url
        if spender_address is not UNSET:
            field_dict["spender_address"] = spender_address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url", UNSET)

        wrapper_url = d.pop("wrapper_url", UNSET)

        gas_url = d.pop("gas_url", UNSET)

        wrapper_gas_url = d.pop("wrapper_gas_url", UNSET)

        spender_address = d.pop("spender_address", UNSET)

        aggregation_provider_deprecated = cls(
            url=url,
            wrapper_url=wrapper_url,
            gas_url=gas_url,
            wrapper_gas_url=wrapper_gas_url,
            spender_address=spender_address,
        )

        aggregation_provider_deprecated.additional_properties = d
        return aggregation_provider_deprecated

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

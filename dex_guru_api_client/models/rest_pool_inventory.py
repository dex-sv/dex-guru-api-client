from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestPoolInventory")


@attr.s(auto_attribs=True)
class RestPoolInventory:
    """
    Attributes:
        id (Union[Unset, str]):
        amm (Union[Unset, str]):
        network (Union[Unset, str]):
        token_addresses (Union[Unset, List[str]]):
        symbols (Union[Unset, List[str]]):
        logo_ur_is (Union[Unset, List[str]]):
        fee_tier (Union[Unset, int]):
        liquidity_native (Union[Unset, float]):
        liquidity_stable (Union[Unset, float]):
        volume_24_h_native (Union[Unset, float]):
        volume_24_h_stable (Union[Unset, float]):
    """

    id: Union[Unset, str] = UNSET
    amm: Union[Unset, str] = UNSET
    network: Union[Unset, str] = UNSET
    token_addresses: Union[Unset, List[str]] = UNSET
    symbols: Union[Unset, List[str]] = UNSET
    logo_ur_is: Union[Unset, List[str]] = UNSET
    fee_tier: Union[Unset, int] = 0
    liquidity_native: Union[Unset, float] = 0.0
    liquidity_stable: Union[Unset, float] = 0.0
    volume_24_h_native: Union[Unset, float] = 0.0
    volume_24_h_stable: Union[Unset, float] = 0.0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        amm = self.amm
        network = self.network
        token_addresses: Union[Unset, List[str]] = UNSET
        if not isinstance(self.token_addresses, Unset):
            token_addresses = self.token_addresses

        symbols: Union[Unset, List[str]] = UNSET
        if not isinstance(self.symbols, Unset):
            symbols = self.symbols

        logo_ur_is: Union[Unset, List[str]] = UNSET
        if not isinstance(self.logo_ur_is, Unset):
            logo_ur_is = self.logo_ur_is

        fee_tier = self.fee_tier
        liquidity_native = self.liquidity_native
        liquidity_stable = self.liquidity_stable
        volume_24_h_native = self.volume_24_h_native
        volume_24_h_stable = self.volume_24_h_stable

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if amm is not UNSET:
            field_dict["amm"] = amm
        if network is not UNSET:
            field_dict["network"] = network
        if token_addresses is not UNSET:
            field_dict["tokenAddresses"] = token_addresses
        if symbols is not UNSET:
            field_dict["symbols"] = symbols
        if logo_ur_is is not UNSET:
            field_dict["logoURIs"] = logo_ur_is
        if fee_tier is not UNSET:
            field_dict["feeTier"] = fee_tier
        if liquidity_native is not UNSET:
            field_dict["liquidityNative"] = liquidity_native
        if liquidity_stable is not UNSET:
            field_dict["liquidityStable"] = liquidity_stable
        if volume_24_h_native is not UNSET:
            field_dict["volume24hNative"] = volume_24_h_native
        if volume_24_h_stable is not UNSET:
            field_dict["volume24hStable"] = volume_24_h_stable

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        amm = d.pop("amm", UNSET)

        network = d.pop("network", UNSET)

        token_addresses = cast(List[str], d.pop("tokenAddresses", UNSET))

        symbols = cast(List[str], d.pop("symbols", UNSET))

        logo_ur_is = cast(List[str], d.pop("logoURIs", UNSET))

        fee_tier = d.pop("feeTier", UNSET)

        liquidity_native = d.pop("liquidityNative", UNSET)

        liquidity_stable = d.pop("liquidityStable", UNSET)

        volume_24_h_native = d.pop("volume24hNative", UNSET)

        volume_24_h_stable = d.pop("volume24hStable", UNSET)

        rest_pool_inventory = cls(
            id=id,
            amm=amm,
            network=network,
            token_addresses=token_addresses,
            symbols=symbols,
            logo_ur_is=logo_ur_is,
            fee_tier=fee_tier,
            liquidity_native=liquidity_native,
            liquidity_stable=liquidity_stable,
            volume_24_h_native=volume_24_h_native,
            volume_24_h_stable=volume_24_h_stable,
        )

        rest_pool_inventory.additional_properties = d
        return rest_pool_inventory

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

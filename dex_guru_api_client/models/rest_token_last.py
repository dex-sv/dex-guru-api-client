from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestTokenLast")


@attr.s(auto_attribs=True)
class RestTokenLast:
    """
    Attributes:
        id (Union[Unset, str]):
        amm (Union[Unset, str]):
        network (Union[Unset, str]):
        timestamp (Union[Unset, int]):
        price_stable (Union[Unset, float]):
        price_native (Union[Unset, float]):
        price_stable_change (Union[Unset, float]):
        price_native_change (Union[Unset, float]):
        volume_stable (Union[Unset, float]):
        volume_native (Union[Unset, float]):
        volume_stable_change (Union[Unset, float]):
        volume_native_change (Union[Unset, float]):
        liquidity_stable (Union[Unset, float]):
        liquidity_native (Union[Unset, float]):
        liquidity_stable_change (Union[Unset, float]):
        liquidity_native_change (Union[Unset, float]):
        transactions (Union[Unset, int]):
        transactions_change (Union[Unset, float]):
    """

    id: Union[Unset, str] = UNSET
    amm: Union[Unset, str] = UNSET
    network: Union[Unset, str] = UNSET
    timestamp: Union[Unset, int] = UNSET
    price_stable: Union[Unset, float] = 0.0
    price_native: Union[Unset, float] = 0.0
    price_stable_change: Union[Unset, float] = 0.0
    price_native_change: Union[Unset, float] = 0.0
    volume_stable: Union[Unset, float] = 0.0
    volume_native: Union[Unset, float] = 0.0
    volume_stable_change: Union[Unset, float] = 0.0
    volume_native_change: Union[Unset, float] = 0.0
    liquidity_stable: Union[Unset, float] = 0.0
    liquidity_native: Union[Unset, float] = 0.0
    liquidity_stable_change: Union[Unset, float] = 0.0
    liquidity_native_change: Union[Unset, float] = 0.0
    transactions: Union[Unset, int] = 0
    transactions_change: Union[Unset, float] = 0.0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        amm = self.amm
        network = self.network
        timestamp = self.timestamp
        price_stable = self.price_stable
        price_native = self.price_native
        price_stable_change = self.price_stable_change
        price_native_change = self.price_native_change
        volume_stable = self.volume_stable
        volume_native = self.volume_native
        volume_stable_change = self.volume_stable_change
        volume_native_change = self.volume_native_change
        liquidity_stable = self.liquidity_stable
        liquidity_native = self.liquidity_native
        liquidity_stable_change = self.liquidity_stable_change
        liquidity_native_change = self.liquidity_native_change
        transactions = self.transactions
        transactions_change = self.transactions_change

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if amm is not UNSET:
            field_dict["AMM"] = amm
        if network is not UNSET:
            field_dict["network"] = network
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if price_stable is not UNSET:
            field_dict["priceStable"] = price_stable
        if price_native is not UNSET:
            field_dict["priceNative"] = price_native
        if price_stable_change is not UNSET:
            field_dict["priceStableChange"] = price_stable_change
        if price_native_change is not UNSET:
            field_dict["priceNativeChange"] = price_native_change
        if volume_stable is not UNSET:
            field_dict["volumeStable"] = volume_stable
        if volume_native is not UNSET:
            field_dict["volumeNative"] = volume_native
        if volume_stable_change is not UNSET:
            field_dict["volumeStableChange"] = volume_stable_change
        if volume_native_change is not UNSET:
            field_dict["volumeNativeChange"] = volume_native_change
        if liquidity_stable is not UNSET:
            field_dict["liquidityStable"] = liquidity_stable
        if liquidity_native is not UNSET:
            field_dict["liquidityNative"] = liquidity_native
        if liquidity_stable_change is not UNSET:
            field_dict["liquidityStableChange"] = liquidity_stable_change
        if liquidity_native_change is not UNSET:
            field_dict["liquidityNativeChange"] = liquidity_native_change
        if transactions is not UNSET:
            field_dict["transactions"] = transactions
        if transactions_change is not UNSET:
            field_dict["transactionsChange"] = transactions_change

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        amm = d.pop("AMM", UNSET)

        network = d.pop("network", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        price_stable = d.pop("priceStable", UNSET)

        price_native = d.pop("priceNative", UNSET)

        price_stable_change = d.pop("priceStableChange", UNSET)

        price_native_change = d.pop("priceNativeChange", UNSET)

        volume_stable = d.pop("volumeStable", UNSET)

        volume_native = d.pop("volumeNative", UNSET)

        volume_stable_change = d.pop("volumeStableChange", UNSET)

        volume_native_change = d.pop("volumeNativeChange", UNSET)

        liquidity_stable = d.pop("liquidityStable", UNSET)

        liquidity_native = d.pop("liquidityNative", UNSET)

        liquidity_stable_change = d.pop("liquidityStableChange", UNSET)

        liquidity_native_change = d.pop("liquidityNativeChange", UNSET)

        transactions = d.pop("transactions", UNSET)

        transactions_change = d.pop("transactionsChange", UNSET)

        rest_token_last = cls(
            id=id,
            amm=amm,
            network=network,
            timestamp=timestamp,
            price_stable=price_stable,
            price_native=price_native,
            price_stable_change=price_stable_change,
            price_native_change=price_native_change,
            volume_stable=volume_stable,
            volume_native=volume_native,
            volume_stable_change=volume_stable_change,
            volume_native_change=volume_native_change,
            liquidity_stable=liquidity_stable,
            liquidity_native=liquidity_native,
            liquidity_stable_change=liquidity_stable_change,
            liquidity_native_change=liquidity_native_change,
            transactions=transactions,
            transactions_change=transactions_change,
        )

        rest_token_last.additional_properties = d
        return rest_token_last

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

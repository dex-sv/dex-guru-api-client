from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestTokenHistoryV3")


@attr.s(auto_attribs=True)
class RestTokenHistoryV3:
    """
    Attributes:
        id (Union[Unset, str]):
        daily_txns (Union[Unset, int]):
        date (Union[Unset, int]):
        currency (Union[Unset, str]):
        daily_volume (Union[Unset, float]):
        total_liquidity (Union[Unset, float]):
        amm (Union[Unset, str]):
        network (Union[Unset, str]):
        price (Union[Unset, float]):
    """

    id: Union[Unset, str] = UNSET
    daily_txns: Union[Unset, int] = 0
    date: Union[Unset, int] = UNSET
    currency: Union[Unset, str] = UNSET
    daily_volume: Union[Unset, float] = 0.0
    total_liquidity: Union[Unset, float] = 0.0
    amm: Union[Unset, str] = UNSET
    network: Union[Unset, str] = UNSET
    price: Union[Unset, float] = 0.0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        daily_txns = self.daily_txns
        date = self.date
        currency = self.currency
        daily_volume = self.daily_volume
        total_liquidity = self.total_liquidity
        amm = self.amm
        network = self.network
        price = self.price

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if daily_txns is not UNSET:
            field_dict["dailyTxns"] = daily_txns
        if date is not UNSET:
            field_dict["date"] = date
        if currency is not UNSET:
            field_dict["currency"] = currency
        if daily_volume is not UNSET:
            field_dict["dailyVolume"] = daily_volume
        if total_liquidity is not UNSET:
            field_dict["totalLiquidity"] = total_liquidity
        if amm is not UNSET:
            field_dict["AMM"] = amm
        if network is not UNSET:
            field_dict["network"] = network
        if price is not UNSET:
            field_dict["price"] = price

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        daily_txns = d.pop("dailyTxns", UNSET)

        date = d.pop("date", UNSET)

        currency = d.pop("currency", UNSET)

        daily_volume = d.pop("dailyVolume", UNSET)

        total_liquidity = d.pop("totalLiquidity", UNSET)

        amm = d.pop("AMM", UNSET)

        network = d.pop("network", UNSET)

        price = d.pop("price", UNSET)

        rest_token_history_v3 = cls(
            id=id,
            daily_txns=daily_txns,
            date=date,
            currency=currency,
            daily_volume=daily_volume,
            total_liquidity=total_liquidity,
            amm=amm,
            network=network,
            price=price,
        )

        rest_token_history_v3.additional_properties = d
        return rest_token_history_v3

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

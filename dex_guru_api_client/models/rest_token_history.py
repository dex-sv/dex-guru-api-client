from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestTokenHistory")


@attr.s(auto_attribs=True)
class RestTokenHistory:
    """
    Attributes:
        id (Union[Unset, str]):
        daily_txns (Union[Unset, int]):
        date (Union[Unset, int]):
        daily_volume_usd (Union[Unset, float]):
        daily_volume_eth (Union[Unset, float]):
        total_liquidity_usd (Union[Unset, float]):
        total_liquidity_eth (Union[Unset, float]):
        volume (Union[Unset, float]):
        liquidity (Union[Unset, float]):
        amm (Union[Unset, str]):
        network (Union[Unset, str]):
        price_eth (Union[Unset, float]):
        price_usd (Union[Unset, float]):
    """

    id: Union[Unset, str] = UNSET
    daily_txns: Union[Unset, int] = 0
    date: Union[Unset, int] = UNSET
    daily_volume_usd: Union[Unset, float] = 0.0
    daily_volume_eth: Union[Unset, float] = 0.0
    total_liquidity_usd: Union[Unset, float] = 0.0
    total_liquidity_eth: Union[Unset, float] = 0.0
    volume: Union[Unset, float] = 0.0
    liquidity: Union[Unset, float] = 0.0
    amm: Union[Unset, str] = UNSET
    network: Union[Unset, str] = UNSET
    price_eth: Union[Unset, float] = 0.0
    price_usd: Union[Unset, float] = 0.0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        daily_txns = self.daily_txns
        date = self.date
        daily_volume_usd = self.daily_volume_usd
        daily_volume_eth = self.daily_volume_eth
        total_liquidity_usd = self.total_liquidity_usd
        total_liquidity_eth = self.total_liquidity_eth
        volume = self.volume
        liquidity = self.liquidity
        amm = self.amm
        network = self.network
        price_eth = self.price_eth
        price_usd = self.price_usd

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if daily_txns is not UNSET:
            field_dict["dailyTxns"] = daily_txns
        if date is not UNSET:
            field_dict["date"] = date
        if daily_volume_usd is not UNSET:
            field_dict["dailyVolumeUSD"] = daily_volume_usd
        if daily_volume_eth is not UNSET:
            field_dict["dailyVolumeETH"] = daily_volume_eth
        if total_liquidity_usd is not UNSET:
            field_dict["totalLiquidityUSD"] = total_liquidity_usd
        if total_liquidity_eth is not UNSET:
            field_dict["totalLiquidityETH"] = total_liquidity_eth
        if volume is not UNSET:
            field_dict["volume"] = volume
        if liquidity is not UNSET:
            field_dict["liquidity"] = liquidity
        if amm is not UNSET:
            field_dict["AMM"] = amm
        if network is not UNSET:
            field_dict["network"] = network
        if price_eth is not UNSET:
            field_dict["priceETH"] = price_eth
        if price_usd is not UNSET:
            field_dict["priceUSD"] = price_usd

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        daily_txns = d.pop("dailyTxns", UNSET)

        date = d.pop("date", UNSET)

        daily_volume_usd = d.pop("dailyVolumeUSD", UNSET)

        daily_volume_eth = d.pop("dailyVolumeETH", UNSET)

        total_liquidity_usd = d.pop("totalLiquidityUSD", UNSET)

        total_liquidity_eth = d.pop("totalLiquidityETH", UNSET)

        volume = d.pop("volume", UNSET)

        liquidity = d.pop("liquidity", UNSET)

        amm = d.pop("AMM", UNSET)

        network = d.pop("network", UNSET)

        price_eth = d.pop("priceETH", UNSET)

        price_usd = d.pop("priceUSD", UNSET)

        rest_token_history = cls(
            id=id,
            daily_txns=daily_txns,
            date=date,
            daily_volume_usd=daily_volume_usd,
            daily_volume_eth=daily_volume_eth,
            total_liquidity_usd=total_liquidity_usd,
            total_liquidity_eth=total_liquidity_eth,
            volume=volume,
            liquidity=liquidity,
            amm=amm,
            network=network,
            price_eth=price_eth,
            price_usd=price_usd,
        )

        rest_token_history.additional_properties = d
        return rest_token_history

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

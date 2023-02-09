from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestTopMarketCap")


@attr.s(auto_attribs=True)
class RestTopMarketCap:
    """
    Attributes:
        total_market_cap (Union[Unset, float]):
        total_market_cap_change_24_h (Union[Unset, float]):
        market_cap (Union[Unset, float]):
        market_cap_change_24_h (Union[Unset, float]):
        trading_volume_24_h (Union[Unset, float]):
        trading_volume_change_24_h (Union[Unset, float]):
        liquidity (Union[Unset, float]):
        liquidity_change_24_h (Union[Unset, float]):
        tokens (Union[Unset, int]): tokens count
        trading_pairs (Union[Unset, int]): trading pairs count
    """

    total_market_cap: Union[Unset, float] = 0.0
    total_market_cap_change_24_h: Union[Unset, float] = 0.0
    market_cap: Union[Unset, float] = 0.0
    market_cap_change_24_h: Union[Unset, float] = 0.0
    trading_volume_24_h: Union[Unset, float] = 0.0
    trading_volume_change_24_h: Union[Unset, float] = 0.0
    liquidity: Union[Unset, float] = 0.0
    liquidity_change_24_h: Union[Unset, float] = 0.0
    tokens: Union[Unset, int] = 0
    trading_pairs: Union[Unset, int] = 0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_market_cap = self.total_market_cap
        total_market_cap_change_24_h = self.total_market_cap_change_24_h
        market_cap = self.market_cap
        market_cap_change_24_h = self.market_cap_change_24_h
        trading_volume_24_h = self.trading_volume_24_h
        trading_volume_change_24_h = self.trading_volume_change_24_h
        liquidity = self.liquidity
        liquidity_change_24_h = self.liquidity_change_24_h
        tokens = self.tokens
        trading_pairs = self.trading_pairs

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_market_cap is not UNSET:
            field_dict["totalMarketCap"] = total_market_cap
        if total_market_cap_change_24_h is not UNSET:
            field_dict["totalMarketCapChange24h"] = total_market_cap_change_24_h
        if market_cap is not UNSET:
            field_dict["marketCap"] = market_cap
        if market_cap_change_24_h is not UNSET:
            field_dict["marketCapChange24h"] = market_cap_change_24_h
        if trading_volume_24_h is not UNSET:
            field_dict["tradingVolume24h"] = trading_volume_24_h
        if trading_volume_change_24_h is not UNSET:
            field_dict["tradingVolumeChange24h"] = trading_volume_change_24_h
        if liquidity is not UNSET:
            field_dict["liquidity"] = liquidity
        if liquidity_change_24_h is not UNSET:
            field_dict["liquidityChange24h"] = liquidity_change_24_h
        if tokens is not UNSET:
            field_dict["tokens"] = tokens
        if trading_pairs is not UNSET:
            field_dict["tradingPairs"] = trading_pairs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_market_cap = d.pop("totalMarketCap", UNSET)

        total_market_cap_change_24_h = d.pop("totalMarketCapChange24h", UNSET)

        market_cap = d.pop("marketCap", UNSET)

        market_cap_change_24_h = d.pop("marketCapChange24h", UNSET)

        trading_volume_24_h = d.pop("tradingVolume24h", UNSET)

        trading_volume_change_24_h = d.pop("tradingVolumeChange24h", UNSET)

        liquidity = d.pop("liquidity", UNSET)

        liquidity_change_24_h = d.pop("liquidityChange24h", UNSET)

        tokens = d.pop("tokens", UNSET)

        trading_pairs = d.pop("tradingPairs", UNSET)

        rest_top_market_cap = cls(
            total_market_cap=total_market_cap,
            total_market_cap_change_24_h=total_market_cap_change_24_h,
            market_cap=market_cap,
            market_cap_change_24_h=market_cap_change_24_h,
            trading_volume_24_h=trading_volume_24_h,
            trading_volume_change_24_h=trading_volume_change_24_h,
            liquidity=liquidity,
            liquidity_change_24_h=liquidity_change_24_h,
            tokens=tokens,
            trading_pairs=trading_pairs,
        )

        rest_top_market_cap.additional_properties = d
        return rest_top_market_cap

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

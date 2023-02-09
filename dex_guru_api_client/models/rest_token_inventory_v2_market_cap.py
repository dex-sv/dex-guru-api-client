import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_chart_point import RestChartPoint


T = TypeVar("T", bound="RestTokenInventoryV2MarketCap")


@attr.s(auto_attribs=True)
class RestTokenInventoryV2MarketCap:
    """
    Attributes:
        id (Union[Unset, str]):
        address (Union[Unset, str]):
        symbol (Union[Unset, str]):
        name (Union[Unset, str]): some description
        description (Union[Unset, str]):  Default: ''.
        txns24h (Union[Unset, int]):
        txns_24_h_change (Union[Unset, float]):
        verified (Union[Unset, bool]):
        decimals (Union[Unset, int]):
        volume24h (Union[Unset, float]):
        volume_24_h_usd (Union[Unset, float]):
        volume_24_h_eth (Union[Unset, float]):
        volume_change_24_h (Union[Unset, float]): DEPRECATED
        liquidity_usd (Union[Unset, float]):
        liquidity_eth (Union[Unset, float]):
        liquidity_change_24_h (Union[Unset, float]): DEPRECATED
        logo_uri (Union[Unset, str]):
        price_usd (Union[Unset, float]):
        price_eth (Union[Unset, float]):
        price_usd_change_24_h (Union[Unset, float]):
        price_eth_change_24_h (Union[Unset, float]):
        timestamp (Union[Unset, datetime.datetime, int, str]):
        block_number (Union[Unset, int]):
        amm (Union[Unset, str]):
        network (Union[Unset, str]):
        token_lists_names (Union[Unset, List[str]]):
        market_cap (Union[Unset, float]):
        market_cap_change_24_h (Union[Unset, float]):
        liquidity_usd_change_24_h (Union[Unset, float]):
        liquidity_eth_change_24_h (Union[Unset, float]):
        volume_usd_change_24_h (Union[Unset, float]):
        volume_eth_change_24_h (Union[Unset, float]):
        change_price_7_days (Union[Unset, float]):
        chart_price_usd_change_7_d (Union[Unset, List['RestChartPoint']]):
    """

    id: Union[Unset, str] = UNSET
    address: Union[Unset, str] = UNSET
    symbol: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = ""
    txns24h: Union[Unset, int] = 0
    txns_24_h_change: Union[Unset, float] = 0.0
    verified: Union[Unset, bool] = False
    decimals: Union[Unset, int] = 0
    volume24h: Union[Unset, float] = 0.0
    volume_24_h_usd: Union[Unset, float] = 0.0
    volume_24_h_eth: Union[Unset, float] = 0.0
    volume_change_24_h: Union[Unset, float] = 0.0
    liquidity_usd: Union[Unset, float] = 0.0
    liquidity_eth: Union[Unset, float] = 0.0
    liquidity_change_24_h: Union[Unset, float] = 0.0
    logo_uri: Union[Unset, str] = UNSET
    price_usd: Union[Unset, float] = 0.0
    price_eth: Union[Unset, float] = 0.0
    price_usd_change_24_h: Union[Unset, float] = 0.0
    price_eth_change_24_h: Union[Unset, float] = 0.0
    timestamp: Union[Unset, datetime.datetime, int, str] = UNSET
    block_number: Union[Unset, int] = UNSET
    amm: Union[Unset, str] = UNSET
    network: Union[Unset, str] = UNSET
    token_lists_names: Union[Unset, List[str]] = UNSET
    market_cap: Union[Unset, float] = 0.0
    market_cap_change_24_h: Union[Unset, float] = 0.0
    liquidity_usd_change_24_h: Union[Unset, float] = 0.0
    liquidity_eth_change_24_h: Union[Unset, float] = 0.0
    volume_usd_change_24_h: Union[Unset, float] = 0.0
    volume_eth_change_24_h: Union[Unset, float] = 0.0
    change_price_7_days: Union[Unset, float] = 0.0
    chart_price_usd_change_7_d: Union[Unset, List["RestChartPoint"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        address = self.address
        symbol = self.symbol
        name = self.name
        description = self.description
        txns24h = self.txns24h
        txns_24_h_change = self.txns_24_h_change
        verified = self.verified
        decimals = self.decimals
        volume24h = self.volume24h
        volume_24_h_usd = self.volume_24_h_usd
        volume_24_h_eth = self.volume_24_h_eth
        volume_change_24_h = self.volume_change_24_h
        liquidity_usd = self.liquidity_usd
        liquidity_eth = self.liquidity_eth
        liquidity_change_24_h = self.liquidity_change_24_h
        logo_uri = self.logo_uri
        price_usd = self.price_usd
        price_eth = self.price_eth
        price_usd_change_24_h = self.price_usd_change_24_h
        price_eth_change_24_h = self.price_eth_change_24_h
        timestamp: Union[Unset, int, str]
        if isinstance(self.timestamp, Unset):
            timestamp = UNSET

        elif isinstance(self.timestamp, datetime.datetime):
            timestamp = UNSET
            if not isinstance(self.timestamp, Unset):
                timestamp = self.timestamp.isoformat()

        else:
            timestamp = self.timestamp

        block_number = self.block_number
        amm = self.amm
        network = self.network
        token_lists_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.token_lists_names, Unset):
            token_lists_names = self.token_lists_names

        market_cap = self.market_cap
        market_cap_change_24_h = self.market_cap_change_24_h
        liquidity_usd_change_24_h = self.liquidity_usd_change_24_h
        liquidity_eth_change_24_h = self.liquidity_eth_change_24_h
        volume_usd_change_24_h = self.volume_usd_change_24_h
        volume_eth_change_24_h = self.volume_eth_change_24_h
        change_price_7_days = self.change_price_7_days
        chart_price_usd_change_7_d: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.chart_price_usd_change_7_d, Unset):
            chart_price_usd_change_7_d = []
            for chart_price_usd_change_7_d_item_data in self.chart_price_usd_change_7_d:
                chart_price_usd_change_7_d_item = chart_price_usd_change_7_d_item_data.to_dict()

                chart_price_usd_change_7_d.append(chart_price_usd_change_7_d_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if address is not UNSET:
            field_dict["address"] = address
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if txns24h is not UNSET:
            field_dict["txns24h"] = txns24h
        if txns_24_h_change is not UNSET:
            field_dict["txns24hChange"] = txns_24_h_change
        if verified is not UNSET:
            field_dict["verified"] = verified
        if decimals is not UNSET:
            field_dict["decimals"] = decimals
        if volume24h is not UNSET:
            field_dict["volume24h"] = volume24h
        if volume_24_h_usd is not UNSET:
            field_dict["volume24hUSD"] = volume_24_h_usd
        if volume_24_h_eth is not UNSET:
            field_dict["volume24hETH"] = volume_24_h_eth
        if volume_change_24_h is not UNSET:
            field_dict["volumeChange24h"] = volume_change_24_h
        if liquidity_usd is not UNSET:
            field_dict["liquidityUSD"] = liquidity_usd
        if liquidity_eth is not UNSET:
            field_dict["liquidityETH"] = liquidity_eth
        if liquidity_change_24_h is not UNSET:
            field_dict["liquidityChange24h"] = liquidity_change_24_h
        if logo_uri is not UNSET:
            field_dict["logoURI"] = logo_uri
        if price_usd is not UNSET:
            field_dict["priceUSD"] = price_usd
        if price_eth is not UNSET:
            field_dict["priceETH"] = price_eth
        if price_usd_change_24_h is not UNSET:
            field_dict["priceUSDChange24h"] = price_usd_change_24_h
        if price_eth_change_24_h is not UNSET:
            field_dict["priceETHChange24h"] = price_eth_change_24_h
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if block_number is not UNSET:
            field_dict["blockNumber"] = block_number
        if amm is not UNSET:
            field_dict["AMM"] = amm
        if network is not UNSET:
            field_dict["network"] = network
        if token_lists_names is not UNSET:
            field_dict["tokenListsNames"] = token_lists_names
        if market_cap is not UNSET:
            field_dict["marketCap"] = market_cap
        if market_cap_change_24_h is not UNSET:
            field_dict["marketCapChange24h"] = market_cap_change_24_h
        if liquidity_usd_change_24_h is not UNSET:
            field_dict["liquidityUSDChange24h"] = liquidity_usd_change_24_h
        if liquidity_eth_change_24_h is not UNSET:
            field_dict["liquidityETHChange24h"] = liquidity_eth_change_24_h
        if volume_usd_change_24_h is not UNSET:
            field_dict["volumeUSDChange24h"] = volume_usd_change_24_h
        if volume_eth_change_24_h is not UNSET:
            field_dict["volumeETHChange24h"] = volume_eth_change_24_h
        if change_price_7_days is not UNSET:
            field_dict["changePrice7days"] = change_price_7_days
        if chart_price_usd_change_7_d is not UNSET:
            field_dict["chartPriceUSDChange7d"] = chart_price_usd_change_7_d

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.rest_chart_point import RestChartPoint

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        address = d.pop("address", UNSET)

        symbol = d.pop("symbol", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        txns24h = d.pop("txns24h", UNSET)

        txns_24_h_change = d.pop("txns24hChange", UNSET)

        verified = d.pop("verified", UNSET)

        decimals = d.pop("decimals", UNSET)

        volume24h = d.pop("volume24h", UNSET)

        volume_24_h_usd = d.pop("volume24hUSD", UNSET)

        volume_24_h_eth = d.pop("volume24hETH", UNSET)

        volume_change_24_h = d.pop("volumeChange24h", UNSET)

        liquidity_usd = d.pop("liquidityUSD", UNSET)

        liquidity_eth = d.pop("liquidityETH", UNSET)

        liquidity_change_24_h = d.pop("liquidityChange24h", UNSET)

        logo_uri = d.pop("logoURI", UNSET)

        price_usd = d.pop("priceUSD", UNSET)

        price_eth = d.pop("priceETH", UNSET)

        price_usd_change_24_h = d.pop("priceUSDChange24h", UNSET)

        price_eth_change_24_h = d.pop("priceETHChange24h", UNSET)

        def _parse_timestamp(data: object) -> Union[Unset, datetime.datetime, int, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _timestamp_type_2 = data
                timestamp_type_2: Union[Unset, datetime.datetime]
                if isinstance(_timestamp_type_2, Unset):
                    timestamp_type_2 = UNSET
                else:
                    timestamp_type_2 = isoparse(_timestamp_type_2)

                return timestamp_type_2
            except:  # noqa: E722
                pass
            return cast(Union[Unset, datetime.datetime, int, str], data)

        timestamp = _parse_timestamp(d.pop("timestamp", UNSET))

        block_number = d.pop("blockNumber", UNSET)

        amm = d.pop("AMM", UNSET)

        network = d.pop("network", UNSET)

        token_lists_names = cast(List[str], d.pop("tokenListsNames", UNSET))

        market_cap = d.pop("marketCap", UNSET)

        market_cap_change_24_h = d.pop("marketCapChange24h", UNSET)

        liquidity_usd_change_24_h = d.pop("liquidityUSDChange24h", UNSET)

        liquidity_eth_change_24_h = d.pop("liquidityETHChange24h", UNSET)

        volume_usd_change_24_h = d.pop("volumeUSDChange24h", UNSET)

        volume_eth_change_24_h = d.pop("volumeETHChange24h", UNSET)

        change_price_7_days = d.pop("changePrice7days", UNSET)

        chart_price_usd_change_7_d = []
        _chart_price_usd_change_7_d = d.pop("chartPriceUSDChange7d", UNSET)
        for chart_price_usd_change_7_d_item_data in _chart_price_usd_change_7_d or []:
            chart_price_usd_change_7_d_item = RestChartPoint.from_dict(chart_price_usd_change_7_d_item_data)

            chart_price_usd_change_7_d.append(chart_price_usd_change_7_d_item)

        rest_token_inventory_v2_market_cap = cls(
            id=id,
            address=address,
            symbol=symbol,
            name=name,
            description=description,
            txns24h=txns24h,
            txns_24_h_change=txns_24_h_change,
            verified=verified,
            decimals=decimals,
            volume24h=volume24h,
            volume_24_h_usd=volume_24_h_usd,
            volume_24_h_eth=volume_24_h_eth,
            volume_change_24_h=volume_change_24_h,
            liquidity_usd=liquidity_usd,
            liquidity_eth=liquidity_eth,
            liquidity_change_24_h=liquidity_change_24_h,
            logo_uri=logo_uri,
            price_usd=price_usd,
            price_eth=price_eth,
            price_usd_change_24_h=price_usd_change_24_h,
            price_eth_change_24_h=price_eth_change_24_h,
            timestamp=timestamp,
            block_number=block_number,
            amm=amm,
            network=network,
            token_lists_names=token_lists_names,
            market_cap=market_cap,
            market_cap_change_24_h=market_cap_change_24_h,
            liquidity_usd_change_24_h=liquidity_usd_change_24_h,
            liquidity_eth_change_24_h=liquidity_eth_change_24_h,
            volume_usd_change_24_h=volume_usd_change_24_h,
            volume_eth_change_24_h=volume_eth_change_24_h,
            change_price_7_days=change_price_7_days,
            chart_price_usd_change_7_d=chart_price_usd_change_7_d,
        )

        rest_token_inventory_v2_market_cap.additional_properties = d
        return rest_token_inventory_v2_market_cap

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

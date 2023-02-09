import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestTokenInventoryV3")


@attr.s(auto_attribs=True)
class RestTokenInventoryV3:
    """
    Attributes:
        market_type (Union[Unset, str]):  Default: 'token'.
        address (Union[Unset, str]):
        id (Union[Unset, str]):
        symbols (Union[Unset, List[str]]):
        underlying_addresses (Union[Unset, List[str]]):
        name (Union[Unset, str]):
        description (Union[Unset, str]):  Default: ''.
        txns24h (Union[Unset, int]):
        txns_24_h_change (Union[Unset, float]):
        verified (Union[Unset, bool]):
        decimals (Union[Unset, int]):
        volume24h (Union[Unset, float]):
        volume_24_h_usd (Union[Unset, float]):
        volume_24_h_eth (Union[Unset, float]):
        liquidity_usd (Union[Unset, float]):
        liquidity_eth (Union[Unset, float]):
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
        logo_uri (Union[Unset, List[str]]):
    """

    market_type: Union[Unset, str] = "token"
    address: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    symbols: Union[Unset, List[str]] = UNSET
    underlying_addresses: Union[Unset, List[str]] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = ""
    txns24h: Union[Unset, int] = 0
    txns_24_h_change: Union[Unset, float] = 0.0
    verified: Union[Unset, bool] = False
    decimals: Union[Unset, int] = 0
    volume24h: Union[Unset, float] = 0.0
    volume_24_h_usd: Union[Unset, float] = 0.0
    volume_24_h_eth: Union[Unset, float] = 0.0
    liquidity_usd: Union[Unset, float] = 0.0
    liquidity_eth: Union[Unset, float] = 0.0
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
    logo_uri: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        market_type = self.market_type
        address = self.address
        id = self.id
        symbols: Union[Unset, List[str]] = UNSET
        if not isinstance(self.symbols, Unset):
            symbols = self.symbols

        underlying_addresses: Union[Unset, List[str]] = UNSET
        if not isinstance(self.underlying_addresses, Unset):
            underlying_addresses = self.underlying_addresses

        name = self.name
        description = self.description
        txns24h = self.txns24h
        txns_24_h_change = self.txns_24_h_change
        verified = self.verified
        decimals = self.decimals
        volume24h = self.volume24h
        volume_24_h_usd = self.volume_24_h_usd
        volume_24_h_eth = self.volume_24_h_eth
        liquidity_usd = self.liquidity_usd
        liquidity_eth = self.liquidity_eth
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
        logo_uri: Union[Unset, List[str]] = UNSET
        if not isinstance(self.logo_uri, Unset):
            logo_uri = self.logo_uri

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if market_type is not UNSET:
            field_dict["marketType"] = market_type
        if address is not UNSET:
            field_dict["address"] = address
        if id is not UNSET:
            field_dict["id"] = id
        if symbols is not UNSET:
            field_dict["symbols"] = symbols
        if underlying_addresses is not UNSET:
            field_dict["underlyingAddresses"] = underlying_addresses
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
        if liquidity_usd is not UNSET:
            field_dict["liquidityUSD"] = liquidity_usd
        if liquidity_eth is not UNSET:
            field_dict["liquidityETH"] = liquidity_eth
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
        if logo_uri is not UNSET:
            field_dict["logoURI"] = logo_uri

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        market_type = d.pop("marketType", UNSET)

        address = d.pop("address", UNSET)

        id = d.pop("id", UNSET)

        symbols = cast(List[str], d.pop("symbols", UNSET))

        underlying_addresses = cast(List[str], d.pop("underlyingAddresses", UNSET))

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        txns24h = d.pop("txns24h", UNSET)

        txns_24_h_change = d.pop("txns24hChange", UNSET)

        verified = d.pop("verified", UNSET)

        decimals = d.pop("decimals", UNSET)

        volume24h = d.pop("volume24h", UNSET)

        volume_24_h_usd = d.pop("volume24hUSD", UNSET)

        volume_24_h_eth = d.pop("volume24hETH", UNSET)

        liquidity_usd = d.pop("liquidityUSD", UNSET)

        liquidity_eth = d.pop("liquidityETH", UNSET)

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

        logo_uri = cast(List[str], d.pop("logoURI", UNSET))

        rest_token_inventory_v3 = cls(
            market_type=market_type,
            address=address,
            id=id,
            symbols=symbols,
            underlying_addresses=underlying_addresses,
            name=name,
            description=description,
            txns24h=txns24h,
            txns_24_h_change=txns_24_h_change,
            verified=verified,
            decimals=decimals,
            volume24h=volume24h,
            volume_24_h_usd=volume_24_h_usd,
            volume_24_h_eth=volume_24_h_eth,
            liquidity_usd=liquidity_usd,
            liquidity_eth=liquidity_eth,
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
            logo_uri=logo_uri,
        )

        rest_token_inventory_v3.additional_properties = d
        return rest_token_inventory_v3

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

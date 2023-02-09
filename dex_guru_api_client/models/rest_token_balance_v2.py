from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.market_type_choices import MarketTypeChoices
from ..types import UNSET, Unset

T = TypeVar("T", bound="RestTokenBalanceV2")


@attr.s(auto_attribs=True)
class RestTokenBalanceV2:
    """
    Attributes:
        token_id (Union[Unset, str]):
        network (Union[Unset, str]):
        balance (Union[Unset, float]):
        balance_usd (Union[Unset, float]):
        change_7_days (Union[Unset, float]):
        deals_avg_price (Union[Unset, float]):
        market_price (Union[Unset, float]):
        profit (Union[Unset, str]):
        logo_uri (Union[Unset, List[str]]):
        symbols (Union[Unset, List[str]]): Mainly needed for LP tokens
        market_type (Union[Unset, MarketTypeChoices]): Market type for inventory. Two types - token and LP token.
            New replacement for TokenTypeChoices. Default: MarketTypeChoices.TOKEN.
        amm (Union[Unset, str]): Mainly needed for LP tokens
        addresses (Union[Unset, List[str]]): Mainly needed for LP tokens
        in_amount_week_sum (Union[Unset, float]):
        out_amount_week_sum (Union[Unset, float]):
    """

    token_id: Union[Unset, str] = UNSET
    network: Union[Unset, str] = UNSET
    balance: Union[Unset, float] = 0.0
    balance_usd: Union[Unset, float] = 0.0
    change_7_days: Union[Unset, float] = UNSET
    deals_avg_price: Union[Unset, float] = UNSET
    market_price: Union[Unset, float] = 0.0
    profit: Union[Unset, str] = UNSET
    logo_uri: Union[Unset, List[str]] = UNSET
    symbols: Union[Unset, List[str]] = UNSET
    market_type: Union[Unset, MarketTypeChoices] = MarketTypeChoices.TOKEN
    amm: Union[Unset, str] = UNSET
    addresses: Union[Unset, List[str]] = UNSET
    in_amount_week_sum: Union[Unset, float] = 0.0
    out_amount_week_sum: Union[Unset, float] = 0.0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        token_id = self.token_id
        network = self.network
        balance = self.balance
        balance_usd = self.balance_usd
        change_7_days = self.change_7_days
        deals_avg_price = self.deals_avg_price
        market_price = self.market_price
        profit = self.profit
        logo_uri: Union[Unset, List[str]] = UNSET
        if not isinstance(self.logo_uri, Unset):
            logo_uri = self.logo_uri

        symbols: Union[Unset, List[str]] = UNSET
        if not isinstance(self.symbols, Unset):
            symbols = self.symbols

        market_type: Union[Unset, str] = UNSET
        if not isinstance(self.market_type, Unset):
            market_type = self.market_type.value

        amm = self.amm
        addresses: Union[Unset, List[str]] = UNSET
        if not isinstance(self.addresses, Unset):
            addresses = self.addresses

        in_amount_week_sum = self.in_amount_week_sum
        out_amount_week_sum = self.out_amount_week_sum

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token_id is not UNSET:
            field_dict["tokenID"] = token_id
        if network is not UNSET:
            field_dict["network"] = network
        if balance is not UNSET:
            field_dict["balance"] = balance
        if balance_usd is not UNSET:
            field_dict["balanceUSD"] = balance_usd
        if change_7_days is not UNSET:
            field_dict["change7Days"] = change_7_days
        if deals_avg_price is not UNSET:
            field_dict["dealsAVGPrice"] = deals_avg_price
        if market_price is not UNSET:
            field_dict["marketPrice"] = market_price
        if profit is not UNSET:
            field_dict["profit"] = profit
        if logo_uri is not UNSET:
            field_dict["logoURI"] = logo_uri
        if symbols is not UNSET:
            field_dict["symbols"] = symbols
        if market_type is not UNSET:
            field_dict["marketType"] = market_type
        if amm is not UNSET:
            field_dict["amm"] = amm
        if addresses is not UNSET:
            field_dict["addresses"] = addresses
        if in_amount_week_sum is not UNSET:
            field_dict["inAmountWeekSum"] = in_amount_week_sum
        if out_amount_week_sum is not UNSET:
            field_dict["outAmountWeekSum"] = out_amount_week_sum

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        token_id = d.pop("tokenID", UNSET)

        network = d.pop("network", UNSET)

        balance = d.pop("balance", UNSET)

        balance_usd = d.pop("balanceUSD", UNSET)

        change_7_days = d.pop("change7Days", UNSET)

        deals_avg_price = d.pop("dealsAVGPrice", UNSET)

        market_price = d.pop("marketPrice", UNSET)

        profit = d.pop("profit", UNSET)

        logo_uri = cast(List[str], d.pop("logoURI", UNSET))

        symbols = cast(List[str], d.pop("symbols", UNSET))

        _market_type = d.pop("marketType", UNSET)
        market_type: Union[Unset, MarketTypeChoices]
        if isinstance(_market_type, Unset):
            market_type = UNSET
        else:
            market_type = MarketTypeChoices(_market_type)

        amm = d.pop("amm", UNSET)

        addresses = cast(List[str], d.pop("addresses", UNSET))

        in_amount_week_sum = d.pop("inAmountWeekSum", UNSET)

        out_amount_week_sum = d.pop("outAmountWeekSum", UNSET)

        rest_token_balance_v2 = cls(
            token_id=token_id,
            network=network,
            balance=balance,
            balance_usd=balance_usd,
            change_7_days=change_7_days,
            deals_avg_price=deals_avg_price,
            market_price=market_price,
            profit=profit,
            logo_uri=logo_uri,
            symbols=symbols,
            market_type=market_type,
            amm=amm,
            addresses=addresses,
            in_amount_week_sum=in_amount_week_sum,
            out_amount_week_sum=out_amount_week_sum,
        )

        rest_token_balance_v2.additional_properties = d
        return rest_token_balance_v2

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

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestTokenBalance")


@attr.s(auto_attribs=True)
class RestTokenBalance:
    """
    Attributes:
        token_id (Union[Unset, str]):
        address (Union[Unset, str]):
        network (Union[Unset, str]):
        logo_uri (Union[Unset, str]):
        symbol (Union[Unset, str]):
        balance (Union[Unset, float]):
        balance_usd (Union[Unset, float]):
        change_7_days (Union[Unset, float]):
        deals_avg_price (Union[Unset, float]):
        market_price (Union[Unset, float]):
        profit (Union[Unset, str]):
        in_amount_week_sum (Union[Unset, float]):
        out_amount_week_sum (Union[Unset, float]):
    """

    token_id: Union[Unset, str] = UNSET
    address: Union[Unset, str] = UNSET
    network: Union[Unset, str] = UNSET
    logo_uri: Union[Unset, str] = UNSET
    symbol: Union[Unset, str] = UNSET
    balance: Union[Unset, float] = 0.0
    balance_usd: Union[Unset, float] = 0.0
    change_7_days: Union[Unset, float] = UNSET
    deals_avg_price: Union[Unset, float] = UNSET
    market_price: Union[Unset, float] = 0.0
    profit: Union[Unset, str] = UNSET
    in_amount_week_sum: Union[Unset, float] = 0.0
    out_amount_week_sum: Union[Unset, float] = 0.0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        token_id = self.token_id
        address = self.address
        network = self.network
        logo_uri = self.logo_uri
        symbol = self.symbol
        balance = self.balance
        balance_usd = self.balance_usd
        change_7_days = self.change_7_days
        deals_avg_price = self.deals_avg_price
        market_price = self.market_price
        profit = self.profit
        in_amount_week_sum = self.in_amount_week_sum
        out_amount_week_sum = self.out_amount_week_sum

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token_id is not UNSET:
            field_dict["tokenID"] = token_id
        if address is not UNSET:
            field_dict["address"] = address
        if network is not UNSET:
            field_dict["network"] = network
        if logo_uri is not UNSET:
            field_dict["logoURI"] = logo_uri
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
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
        if in_amount_week_sum is not UNSET:
            field_dict["inAmountWeekSum"] = in_amount_week_sum
        if out_amount_week_sum is not UNSET:
            field_dict["outAmountWeekSum"] = out_amount_week_sum

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        token_id = d.pop("tokenID", UNSET)

        address = d.pop("address", UNSET)

        network = d.pop("network", UNSET)

        logo_uri = d.pop("logoURI", UNSET)

        symbol = d.pop("symbol", UNSET)

        balance = d.pop("balance", UNSET)

        balance_usd = d.pop("balanceUSD", UNSET)

        change_7_days = d.pop("change7Days", UNSET)

        deals_avg_price = d.pop("dealsAVGPrice", UNSET)

        market_price = d.pop("marketPrice", UNSET)

        profit = d.pop("profit", UNSET)

        in_amount_week_sum = d.pop("inAmountWeekSum", UNSET)

        out_amount_week_sum = d.pop("outAmountWeekSum", UNSET)

        rest_token_balance = cls(
            token_id=token_id,
            address=address,
            network=network,
            logo_uri=logo_uri,
            symbol=symbol,
            balance=balance,
            balance_usd=balance_usd,
            change_7_days=change_7_days,
            deals_avg_price=deals_avg_price,
            market_price=market_price,
            profit=profit,
            in_amount_week_sum=in_amount_week_sum,
            out_amount_week_sum=out_amount_week_sum,
        )

        rest_token_balance.additional_properties = d
        return rest_token_balance

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

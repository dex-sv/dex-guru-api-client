from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.holder_type_choices import HolderTypeChoices
from ..models.rest_holder_pnl_holders_making_money import RestHolderPNLHoldersMakingMoney
from ..types import UNSET, Unset

T = TypeVar("T", bound="RestHolderPNL")


@attr.s(auto_attribs=True)
class RestHolderPNL:
    """
    Attributes:
        wallet_address (str):
        realized (float):
        unrealized (float):
        buy_volume (float):
        buy_volume_usd (float):
        tokens_out (float):
        tokens_out_usd (float):
        sell_volume (float):
        sell_volume_usd (float):
        balance (float):
        balance_usd (float):
        wallets_categories (Union[Unset, List[str]]):
        holder_type (Union[Unset, HolderTypeChoices]): An enumeration.
        label (Union[Unset, str]):
        profit (Union[Unset, RestHolderPNLHoldersMakingMoney]):  Default: RestHolderPNLHoldersMakingMoney.AT_MONEY.
    """

    wallet_address: str
    realized: float
    unrealized: float
    buy_volume: float
    buy_volume_usd: float
    tokens_out: float
    tokens_out_usd: float
    sell_volume: float
    sell_volume_usd: float
    balance: float
    balance_usd: float
    wallets_categories: Union[Unset, List[str]] = UNSET
    holder_type: Union[Unset, HolderTypeChoices] = UNSET
    label: Union[Unset, str] = UNSET
    profit: Union[Unset, RestHolderPNLHoldersMakingMoney] = RestHolderPNLHoldersMakingMoney.AT_MONEY
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        wallet_address = self.wallet_address
        realized = self.realized
        unrealized = self.unrealized
        buy_volume = self.buy_volume
        buy_volume_usd = self.buy_volume_usd
        tokens_out = self.tokens_out
        tokens_out_usd = self.tokens_out_usd
        sell_volume = self.sell_volume
        sell_volume_usd = self.sell_volume_usd
        balance = self.balance
        balance_usd = self.balance_usd
        wallets_categories: Union[Unset, List[str]] = UNSET
        if not isinstance(self.wallets_categories, Unset):
            wallets_categories = self.wallets_categories

        holder_type: Union[Unset, str] = UNSET
        if not isinstance(self.holder_type, Unset):
            holder_type = self.holder_type.value

        label = self.label
        profit: Union[Unset, str] = UNSET
        if not isinstance(self.profit, Unset):
            profit = self.profit.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "wallet_address": wallet_address,
                "realized": realized,
                "unrealized": unrealized,
                "buy_volume": buy_volume,
                "buy_volume_usd": buy_volume_usd,
                "tokens_out": tokens_out,
                "tokens_out_usd": tokens_out_usd,
                "sell_volume": sell_volume,
                "sell_volume_usd": sell_volume_usd,
                "balance": balance,
                "balance_usd": balance_usd,
            }
        )
        if wallets_categories is not UNSET:
            field_dict["wallets_categories"] = wallets_categories
        if holder_type is not UNSET:
            field_dict["holder_type"] = holder_type
        if label is not UNSET:
            field_dict["label"] = label
        if profit is not UNSET:
            field_dict["profit"] = profit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        wallet_address = d.pop("wallet_address")

        realized = d.pop("realized")

        unrealized = d.pop("unrealized")

        buy_volume = d.pop("buy_volume")

        buy_volume_usd = d.pop("buy_volume_usd")

        tokens_out = d.pop("tokens_out")

        tokens_out_usd = d.pop("tokens_out_usd")

        sell_volume = d.pop("sell_volume")

        sell_volume_usd = d.pop("sell_volume_usd")

        balance = d.pop("balance")

        balance_usd = d.pop("balance_usd")

        wallets_categories = cast(List[str], d.pop("wallets_categories", UNSET))

        _holder_type = d.pop("holder_type", UNSET)
        holder_type: Union[Unset, HolderTypeChoices]
        if isinstance(_holder_type, Unset):
            holder_type = UNSET
        else:
            holder_type = HolderTypeChoices(_holder_type)

        label = d.pop("label", UNSET)

        _profit = d.pop("profit", UNSET)
        profit: Union[Unset, RestHolderPNLHoldersMakingMoney]
        if isinstance(_profit, Unset):
            profit = UNSET
        else:
            profit = RestHolderPNLHoldersMakingMoney(_profit)

        rest_holder_pnl = cls(
            wallet_address=wallet_address,
            realized=realized,
            unrealized=unrealized,
            buy_volume=buy_volume,
            buy_volume_usd=buy_volume_usd,
            tokens_out=tokens_out,
            tokens_out_usd=tokens_out_usd,
            sell_volume=sell_volume,
            sell_volume_usd=sell_volume_usd,
            balance=balance,
            balance_usd=balance_usd,
            wallets_categories=wallets_categories,
            holder_type=holder_type,
            label=label,
            profit=profit,
        )

        rest_holder_pnl.additional_properties = d
        return rest_holder_pnl

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

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.amm_choices import AmmChoices
from ..models.body_get_token_transactions_v2_tokens_token_id_transactions_post_token_status import (
    BodyGetTokenTransactionsV2TokensTokenIdTransactionsPostTokenStatus,
)
from ..models.categories_choices import CategoriesChoices
from ..models.liquidity_categories_choices import LiquidityCategoriesChoices
from ..models.order_choices import OrderChoices
from ..models.sort_choices import SortChoices
from ..models.transaction_choices import TransactionChoices
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_date import FilterDate
    from ..models.filter_token_trade_size import FilterTokenTradeSize
    from ..models.filter_trade_size_usd import FilterTradeSizeUSD


T = TypeVar("T", bound="BodyGetTokenTransactionsV2TokensTokenIdTransactionsPost")


@attr.s(auto_attribs=True)
class BodyGetTokenTransactionsV2TokensTokenIdTransactionsPost:
    """
    Attributes:
        transaction_type (Union[Unset, List[TransactionChoices]]):
        amm (Union[Unset, AmmChoices]): An enumeration.
        trade_size_usd (Union[Unset, FilterTradeSizeUSD]):
        exchange_token_trade (Union[Unset, FilterTokenTradeSize]):
        account (Union[Unset, str]): Wallet address
        pool_address (Union[Unset, str]): Pool address
        date (Union[Unset, FilterDate]): You can pass YYYY-MM-DD or YYYY-MM-DDTHH:MM[:SS] or timestamp
        sort_by (Union[Unset, SortChoices]): An enumeration. Default: SortChoices.TIMESTAMP.
        order (Union[Unset, OrderChoices]): An enumeration. Default: OrderChoices.DESC.
        limit (Union[Unset, int]): Limit records Default: 10.
        offset (Union[Unset, int]): Offset records
        with_full_totals (Union[Unset, bool]): Provide totals for pagination
        current_token_position (Union[Unset, int]): Specify current token position
        token_status (Union[Unset, BodyGetTokenTransactionsV2TokensTokenIdTransactionsPostTokenStatus]): Filter by token
            status Default: BodyGetTokenTransactionsV2TokensTokenIdTransactionsPostTokenStatus.ALL.
        wallet_category (Union[Unset, List[CategoriesChoices]]): Filter by wallet category
        liquidity_category (Union[Unset, List[LiquidityCategoriesChoices]]): Filter by liquidity category
        transfer_from_address (Union[Unset, str]): Wallet address from which the transfer was
        transfer_to_address (Union[Unset, str]): Wallet address to which the transfer was
    """

    transaction_type: Union[Unset, List[TransactionChoices]] = UNSET
    amm: Union[Unset, AmmChoices] = UNSET
    trade_size_usd: Union[Unset, "FilterTradeSizeUSD"] = UNSET
    exchange_token_trade: Union[Unset, "FilterTokenTradeSize"] = UNSET
    account: Union[Unset, str] = UNSET
    pool_address: Union[Unset, str] = UNSET
    date: Union[Unset, "FilterDate"] = UNSET
    sort_by: Union[Unset, SortChoices] = SortChoices.TIMESTAMP
    order: Union[Unset, OrderChoices] = OrderChoices.DESC
    limit: Union[Unset, int] = 10
    offset: Union[Unset, int] = 0
    with_full_totals: Union[Unset, bool] = UNSET
    current_token_position: Union[Unset, int] = UNSET
    token_status: Union[
        Unset, BodyGetTokenTransactionsV2TokensTokenIdTransactionsPostTokenStatus
    ] = BodyGetTokenTransactionsV2TokensTokenIdTransactionsPostTokenStatus.ALL
    wallet_category: Union[Unset, List[CategoriesChoices]] = UNSET
    liquidity_category: Union[Unset, List[LiquidityCategoriesChoices]] = UNSET
    transfer_from_address: Union[Unset, str] = UNSET
    transfer_to_address: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        transaction_type: Union[Unset, List[str]] = UNSET
        if not isinstance(self.transaction_type, Unset):
            transaction_type = []
            for transaction_type_item_data in self.transaction_type:
                transaction_type_item = transaction_type_item_data.value

                transaction_type.append(transaction_type_item)

        amm: Union[Unset, str] = UNSET
        if not isinstance(self.amm, Unset):
            amm = self.amm.value

        trade_size_usd: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.trade_size_usd, Unset):
            trade_size_usd = self.trade_size_usd.to_dict()

        exchange_token_trade: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.exchange_token_trade, Unset):
            exchange_token_trade = self.exchange_token_trade.to_dict()

        account = self.account
        pool_address = self.pool_address
        date: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.to_dict()

        sort_by: Union[Unset, str] = UNSET
        if not isinstance(self.sort_by, Unset):
            sort_by = self.sort_by.value

        order: Union[Unset, str] = UNSET
        if not isinstance(self.order, Unset):
            order = self.order.value

        limit = self.limit
        offset = self.offset
        with_full_totals = self.with_full_totals
        current_token_position = self.current_token_position
        token_status: Union[Unset, str] = UNSET
        if not isinstance(self.token_status, Unset):
            token_status = self.token_status.value

        wallet_category: Union[Unset, List[str]] = UNSET
        if not isinstance(self.wallet_category, Unset):
            wallet_category = []
            for wallet_category_item_data in self.wallet_category:
                wallet_category_item = wallet_category_item_data.value

                wallet_category.append(wallet_category_item)

        liquidity_category: Union[Unset, List[str]] = UNSET
        if not isinstance(self.liquidity_category, Unset):
            liquidity_category = []
            for liquidity_category_item_data in self.liquidity_category:
                liquidity_category_item = liquidity_category_item_data.value

                liquidity_category.append(liquidity_category_item)

        transfer_from_address = self.transfer_from_address
        transfer_to_address = self.transfer_to_address

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if transaction_type is not UNSET:
            field_dict["transaction_type"] = transaction_type
        if amm is not UNSET:
            field_dict["amm"] = amm
        if trade_size_usd is not UNSET:
            field_dict["trade_size_usd"] = trade_size_usd
        if exchange_token_trade is not UNSET:
            field_dict["exchange_token_trade"] = exchange_token_trade
        if account is not UNSET:
            field_dict["account"] = account
        if pool_address is not UNSET:
            field_dict["pool_address"] = pool_address
        if date is not UNSET:
            field_dict["date"] = date
        if sort_by is not UNSET:
            field_dict["sort_by"] = sort_by
        if order is not UNSET:
            field_dict["order"] = order
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset
        if with_full_totals is not UNSET:
            field_dict["with_full_totals"] = with_full_totals
        if current_token_position is not UNSET:
            field_dict["current_token_position"] = current_token_position
        if token_status is not UNSET:
            field_dict["token_status"] = token_status
        if wallet_category is not UNSET:
            field_dict["wallet_category"] = wallet_category
        if liquidity_category is not UNSET:
            field_dict["liquidity_category"] = liquidity_category
        if transfer_from_address is not UNSET:
            field_dict["transfer_from_address"] = transfer_from_address
        if transfer_to_address is not UNSET:
            field_dict["transfer_to_address"] = transfer_to_address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.filter_date import FilterDate
        from ..models.filter_token_trade_size import FilterTokenTradeSize
        from ..models.filter_trade_size_usd import FilterTradeSizeUSD

        d = src_dict.copy()
        transaction_type = []
        _transaction_type = d.pop("transaction_type", UNSET)
        for transaction_type_item_data in _transaction_type or []:
            transaction_type_item = TransactionChoices(transaction_type_item_data)

            transaction_type.append(transaction_type_item)

        _amm = d.pop("amm", UNSET)
        amm: Union[Unset, AmmChoices]
        if isinstance(_amm, Unset):
            amm = UNSET
        else:
            amm = AmmChoices(_amm)

        _trade_size_usd = d.pop("trade_size_usd", UNSET)
        trade_size_usd: Union[Unset, FilterTradeSizeUSD]
        if isinstance(_trade_size_usd, Unset):
            trade_size_usd = UNSET
        else:
            trade_size_usd = FilterTradeSizeUSD.from_dict(_trade_size_usd)

        _exchange_token_trade = d.pop("exchange_token_trade", UNSET)
        exchange_token_trade: Union[Unset, FilterTokenTradeSize]
        if isinstance(_exchange_token_trade, Unset):
            exchange_token_trade = UNSET
        else:
            exchange_token_trade = FilterTokenTradeSize.from_dict(_exchange_token_trade)

        account = d.pop("account", UNSET)

        pool_address = d.pop("pool_address", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, FilterDate]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = FilterDate.from_dict(_date)

        _sort_by = d.pop("sort_by", UNSET)
        sort_by: Union[Unset, SortChoices]
        if isinstance(_sort_by, Unset):
            sort_by = UNSET
        else:
            sort_by = SortChoices(_sort_by)

        _order = d.pop("order", UNSET)
        order: Union[Unset, OrderChoices]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = OrderChoices(_order)

        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        with_full_totals = d.pop("with_full_totals", UNSET)

        current_token_position = d.pop("current_token_position", UNSET)

        _token_status = d.pop("token_status", UNSET)
        token_status: Union[Unset, BodyGetTokenTransactionsV2TokensTokenIdTransactionsPostTokenStatus]
        if isinstance(_token_status, Unset):
            token_status = UNSET
        else:
            token_status = BodyGetTokenTransactionsV2TokensTokenIdTransactionsPostTokenStatus(_token_status)

        wallet_category = []
        _wallet_category = d.pop("wallet_category", UNSET)
        for wallet_category_item_data in _wallet_category or []:
            wallet_category_item = CategoriesChoices(wallet_category_item_data)

            wallet_category.append(wallet_category_item)

        liquidity_category = []
        _liquidity_category = d.pop("liquidity_category", UNSET)
        for liquidity_category_item_data in _liquidity_category or []:
            liquidity_category_item = LiquidityCategoriesChoices(liquidity_category_item_data)

            liquidity_category.append(liquidity_category_item)

        transfer_from_address = d.pop("transfer_from_address", UNSET)

        transfer_to_address = d.pop("transfer_to_address", UNSET)

        body_get_token_transactions_v2_tokens_token_id_transactions_post = cls(
            transaction_type=transaction_type,
            amm=amm,
            trade_size_usd=trade_size_usd,
            exchange_token_trade=exchange_token_trade,
            account=account,
            pool_address=pool_address,
            date=date,
            sort_by=sort_by,
            order=order,
            limit=limit,
            offset=offset,
            with_full_totals=with_full_totals,
            current_token_position=current_token_position,
            token_status=token_status,
            wallet_category=wallet_category,
            liquidity_category=liquidity_category,
            transfer_from_address=transfer_from_address,
            transfer_to_address=transfer_to_address,
        )

        body_get_token_transactions_v2_tokens_token_id_transactions_post.additional_properties = d
        return body_get_token_transactions_v2_tokens_token_id_transactions_post

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

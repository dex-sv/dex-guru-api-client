from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.amm_choices import AmmChoices
from ..models.body_get_transactions_universal_v3_tokens_transactions_post_token_status import (
    BodyGetTransactionsUniversalV3TokensTransactionsPostTokenStatus,
)
from ..models.categories_choices import CategoriesChoices
from ..models.liquidity_categories_choices import LiquidityCategoriesChoices
from ..models.network_choices import NetworkChoices
from ..models.order_choices import OrderChoices
from ..models.transaction_choices import TransactionChoices
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_date import FilterDate
    from ..models.filter_trade_size_usd import FilterTradeSizeUSD


T = TypeVar("T", bound="BodyGetTransactionsUniversalV3TokensTransactionsPost")


@attr.s(auto_attribs=True)
class BodyGetTransactionsUniversalV3TokensTransactionsPost:
    """
    Attributes:
        current_token_id (Union[Unset, str]):
        transaction_types (Union[Unset, List[TransactionChoices]]): [swap, burn, mint, transfer]
        amm (Union[Unset, AmmChoices]): An enumeration.
        network (Union[Unset, NetworkChoices]): An enumeration.
        trade_size_usd (Union[Unset, FilterTradeSizeUSD]):
        token_id (Union[Unset, str]): Second optional token_id
        account (Union[Unset, str]): Wallet address
        second_account (Union[Unset, str]): Second wallet address
        pool_address (Union[Unset, str]): Pool address
        date (Union[Unset, FilterDate]): You can pass YYYY-MM-DD or YYYY-MM-DDTHH:MM[:SS] or timestamp
        sort_by (Union[Unset, str]): Field to sort by Default: 'timestamp'.
        order (Union[Unset, OrderChoices]): An enumeration. Default: OrderChoices.DESC.
        limit (Union[Unset, int]): Limit records Default: 10.
        offset (Union[Unset, int]): Offset records
        with_full_totals (Union[Unset, bool]): Provide totals for pagination
        transfer_from_address (Union[Unset, str]): Wallet address from which the transfer was
        transfer_to_address (Union[Unset, str]): Wallet address to which the transfer was
        token_status (Union[Unset, BodyGetTransactionsUniversalV3TokensTransactionsPostTokenStatus]): Filter by token
            status Default: BodyGetTransactionsUniversalV3TokensTransactionsPostTokenStatus.ALL.
        wallet_category (Union[Unset, List[Union[CategoriesChoices, LiquidityCategoriesChoices]]]): Filter by wallet
            category
        transaction_address (Union[Unset, str]): Transaction hash
    """

    current_token_id: Union[Unset, str] = UNSET
    transaction_types: Union[Unset, List[TransactionChoices]] = UNSET
    amm: Union[Unset, AmmChoices] = UNSET
    network: Union[Unset, NetworkChoices] = UNSET
    trade_size_usd: Union[Unset, "FilterTradeSizeUSD"] = UNSET
    token_id: Union[Unset, str] = UNSET
    account: Union[Unset, str] = UNSET
    second_account: Union[Unset, str] = UNSET
    pool_address: Union[Unset, str] = UNSET
    date: Union[Unset, "FilterDate"] = UNSET
    sort_by: Union[Unset, str] = "timestamp"
    order: Union[Unset, OrderChoices] = OrderChoices.DESC
    limit: Union[Unset, int] = 10
    offset: Union[Unset, int] = 0
    with_full_totals: Union[Unset, bool] = False
    transfer_from_address: Union[Unset, str] = UNSET
    transfer_to_address: Union[Unset, str] = UNSET
    token_status: Union[
        Unset, BodyGetTransactionsUniversalV3TokensTransactionsPostTokenStatus
    ] = BodyGetTransactionsUniversalV3TokensTransactionsPostTokenStatus.ALL
    wallet_category: Union[Unset, List[Union[CategoriesChoices, LiquidityCategoriesChoices]]] = UNSET
    transaction_address: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        current_token_id = self.current_token_id
        transaction_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.transaction_types, Unset):
            transaction_types = []
            for transaction_types_item_data in self.transaction_types:
                transaction_types_item = transaction_types_item_data.value

                transaction_types.append(transaction_types_item)

        amm: Union[Unset, str] = UNSET
        if not isinstance(self.amm, Unset):
            amm = self.amm.value

        network: Union[Unset, str] = UNSET
        if not isinstance(self.network, Unset):
            network = self.network.value

        trade_size_usd: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.trade_size_usd, Unset):
            trade_size_usd = self.trade_size_usd.to_dict()

        token_id = self.token_id
        account = self.account
        second_account = self.second_account
        pool_address = self.pool_address
        date: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.to_dict()

        sort_by = self.sort_by
        order: Union[Unset, str] = UNSET
        if not isinstance(self.order, Unset):
            order = self.order.value

        limit = self.limit
        offset = self.offset
        with_full_totals = self.with_full_totals
        transfer_from_address = self.transfer_from_address
        transfer_to_address = self.transfer_to_address
        token_status: Union[Unset, str] = UNSET
        if not isinstance(self.token_status, Unset):
            token_status = self.token_status.value

        wallet_category: Union[Unset, List[str]] = UNSET
        if not isinstance(self.wallet_category, Unset):
            wallet_category = []
            for wallet_category_item_data in self.wallet_category:
                wallet_category_item: str

                if isinstance(wallet_category_item_data, CategoriesChoices):
                    wallet_category_item = wallet_category_item_data.value

                else:
                    wallet_category_item = wallet_category_item_data.value

                wallet_category.append(wallet_category_item)

        transaction_address = self.transaction_address

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_token_id is not UNSET:
            field_dict["current_token_id"] = current_token_id
        if transaction_types is not UNSET:
            field_dict["transaction_types"] = transaction_types
        if amm is not UNSET:
            field_dict["amm"] = amm
        if network is not UNSET:
            field_dict["network"] = network
        if trade_size_usd is not UNSET:
            field_dict["trade_size_usd"] = trade_size_usd
        if token_id is not UNSET:
            field_dict["token_id"] = token_id
        if account is not UNSET:
            field_dict["account"] = account
        if second_account is not UNSET:
            field_dict["second_account"] = second_account
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
        if transfer_from_address is not UNSET:
            field_dict["transfer_from_address"] = transfer_from_address
        if transfer_to_address is not UNSET:
            field_dict["transfer_to_address"] = transfer_to_address
        if token_status is not UNSET:
            field_dict["token_status"] = token_status
        if wallet_category is not UNSET:
            field_dict["wallet_category"] = wallet_category
        if transaction_address is not UNSET:
            field_dict["transaction_address"] = transaction_address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.filter_date import FilterDate
        from ..models.filter_trade_size_usd import FilterTradeSizeUSD

        d = src_dict.copy()
        current_token_id = d.pop("current_token_id", UNSET)

        transaction_types = []
        _transaction_types = d.pop("transaction_types", UNSET)
        for transaction_types_item_data in _transaction_types or []:
            transaction_types_item = TransactionChoices(transaction_types_item_data)

            transaction_types.append(transaction_types_item)

        _amm = d.pop("amm", UNSET)
        amm: Union[Unset, AmmChoices]
        if isinstance(_amm, Unset):
            amm = UNSET
        else:
            amm = AmmChoices(_amm)

        _network = d.pop("network", UNSET)
        network: Union[Unset, NetworkChoices]
        if isinstance(_network, Unset):
            network = UNSET
        else:
            network = NetworkChoices(_network)

        _trade_size_usd = d.pop("trade_size_usd", UNSET)
        trade_size_usd: Union[Unset, FilterTradeSizeUSD]
        if isinstance(_trade_size_usd, Unset):
            trade_size_usd = UNSET
        else:
            trade_size_usd = FilterTradeSizeUSD.from_dict(_trade_size_usd)

        token_id = d.pop("token_id", UNSET)

        account = d.pop("account", UNSET)

        second_account = d.pop("second_account", UNSET)

        pool_address = d.pop("pool_address", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, FilterDate]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = FilterDate.from_dict(_date)

        sort_by = d.pop("sort_by", UNSET)

        _order = d.pop("order", UNSET)
        order: Union[Unset, OrderChoices]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = OrderChoices(_order)

        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        with_full_totals = d.pop("with_full_totals", UNSET)

        transfer_from_address = d.pop("transfer_from_address", UNSET)

        transfer_to_address = d.pop("transfer_to_address", UNSET)

        _token_status = d.pop("token_status", UNSET)
        token_status: Union[Unset, BodyGetTransactionsUniversalV3TokensTransactionsPostTokenStatus]
        if isinstance(_token_status, Unset):
            token_status = UNSET
        else:
            token_status = BodyGetTransactionsUniversalV3TokensTransactionsPostTokenStatus(_token_status)

        wallet_category = []
        _wallet_category = d.pop("wallet_category", UNSET)
        for wallet_category_item_data in _wallet_category or []:

            def _parse_wallet_category_item(data: object) -> Union[CategoriesChoices, LiquidityCategoriesChoices]:
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    wallet_category_item_type_0 = CategoriesChoices(data)

                    return wallet_category_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, str):
                    raise TypeError()
                wallet_category_item_type_1 = LiquidityCategoriesChoices(data)

                return wallet_category_item_type_1

            wallet_category_item = _parse_wallet_category_item(wallet_category_item_data)

            wallet_category.append(wallet_category_item)

        transaction_address = d.pop("transaction_address", UNSET)

        body_get_transactions_universal_v3_tokens_transactions_post = cls(
            current_token_id=current_token_id,
            transaction_types=transaction_types,
            amm=amm,
            network=network,
            trade_size_usd=trade_size_usd,
            token_id=token_id,
            account=account,
            second_account=second_account,
            pool_address=pool_address,
            date=date,
            sort_by=sort_by,
            order=order,
            limit=limit,
            offset=offset,
            with_full_totals=with_full_totals,
            transfer_from_address=transfer_from_address,
            transfer_to_address=transfer_to_address,
            token_status=token_status,
            wallet_category=wallet_category,
            transaction_address=transaction_address,
        )

        body_get_transactions_universal_v3_tokens_transactions_post.additional_properties = d
        return body_get_transactions_universal_v3_tokens_transactions_post

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

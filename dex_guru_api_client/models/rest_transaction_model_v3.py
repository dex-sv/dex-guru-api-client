from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.transaction_choices import TransactionChoices
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_lp_token import RestLpToken


T = TypeVar("T", bound="RestTransactionModelV3")


@attr.s(auto_attribs=True)
class RestTransactionModelV3:
    """
    Attributes:
        type (str):
        network (str):
        timestamp (int):
        transaction_type (TransactionChoices): An enumeration.
        transaction_address (str):
        token_addresses (List[str]):
        symbols (List[str]):
        wallets (List[str]):
        amounts (List[float]):
        amount_stable (float):
        amounts_stable (List[float]):
        prices_stable (List[float]):
        wallets_categories (Union[List[str], Unset, str]):
        amount_native (Union[Unset, float]):
        amounts_native (Union[Unset, List[float]]):
        prices_native (Union[Unset, List[float]]):
        pool_address (Union[Unset, str]):
        from_address (Union[Unset, str]):
        to_address (Union[Unset, str]):
        lp_token (Union[Unset, RestLpToken]):
    """

    type: str
    network: str
    timestamp: int
    transaction_type: TransactionChoices
    transaction_address: str
    token_addresses: List[str]
    symbols: List[str]
    wallets: List[str]
    amounts: List[float]
    amount_stable: float
    amounts_stable: List[float]
    prices_stable: List[float]
    wallets_categories: Union[List[str], Unset, str] = UNSET
    amount_native: Union[Unset, float] = UNSET
    amounts_native: Union[Unset, List[float]] = UNSET
    prices_native: Union[Unset, List[float]] = UNSET
    pool_address: Union[Unset, str] = UNSET
    from_address: Union[Unset, str] = UNSET
    to_address: Union[Unset, str] = UNSET
    lp_token: Union[Unset, "RestLpToken"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        network = self.network
        timestamp = self.timestamp
        transaction_type = self.transaction_type.value

        transaction_address = self.transaction_address
        token_addresses = self.token_addresses

        symbols = self.symbols

        wallets = self.wallets

        amounts = self.amounts

        amount_stable = self.amount_stable
        amounts_stable = self.amounts_stable

        prices_stable = self.prices_stable

        wallets_categories: Union[List[str], Unset, str]
        if isinstance(self.wallets_categories, Unset):
            wallets_categories = UNSET

        elif isinstance(self.wallets_categories, list):
            wallets_categories = UNSET
            if not isinstance(self.wallets_categories, Unset):
                wallets_categories = self.wallets_categories

        else:
            wallets_categories = self.wallets_categories

        amount_native = self.amount_native
        amounts_native: Union[Unset, List[float]] = UNSET
        if not isinstance(self.amounts_native, Unset):
            amounts_native = self.amounts_native

        prices_native: Union[Unset, List[float]] = UNSET
        if not isinstance(self.prices_native, Unset):
            prices_native = self.prices_native

        pool_address = self.pool_address
        from_address = self.from_address
        to_address = self.to_address
        lp_token: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lp_token, Unset):
            lp_token = self.lp_token.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "network": network,
                "timestamp": timestamp,
                "transactionType": transaction_type,
                "transactionAddress": transaction_address,
                "tokenAddresses": token_addresses,
                "symbols": symbols,
                "wallets": wallets,
                "amounts": amounts,
                "amountStable": amount_stable,
                "amountsStable": amounts_stable,
                "pricesStable": prices_stable,
            }
        )
        if wallets_categories is not UNSET:
            field_dict["walletsCategories"] = wallets_categories
        if amount_native is not UNSET:
            field_dict["amountNative"] = amount_native
        if amounts_native is not UNSET:
            field_dict["amountsNative"] = amounts_native
        if prices_native is not UNSET:
            field_dict["pricesNative"] = prices_native
        if pool_address is not UNSET:
            field_dict["poolAddress"] = pool_address
        if from_address is not UNSET:
            field_dict["fromAddress"] = from_address
        if to_address is not UNSET:
            field_dict["toAddress"] = to_address
        if lp_token is not UNSET:
            field_dict["lpToken"] = lp_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.rest_lp_token import RestLpToken

        d = src_dict.copy()
        type = d.pop("type")

        network = d.pop("network")

        timestamp = d.pop("timestamp")

        transaction_type = TransactionChoices(d.pop("transactionType"))

        transaction_address = d.pop("transactionAddress")

        token_addresses = cast(List[str], d.pop("tokenAddresses"))

        symbols = cast(List[str], d.pop("symbols"))

        wallets = cast(List[str], d.pop("wallets"))

        amounts = cast(List[float], d.pop("amounts"))

        amount_stable = d.pop("amountStable")

        amounts_stable = cast(List[float], d.pop("amountsStable"))

        prices_stable = cast(List[float], d.pop("pricesStable"))

        def _parse_wallets_categories(data: object) -> Union[List[str], Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                wallets_categories_type_0 = cast(List[str], data)

                return wallets_categories_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], Unset, str], data)

        wallets_categories = _parse_wallets_categories(d.pop("walletsCategories", UNSET))

        amount_native = d.pop("amountNative", UNSET)

        amounts_native = cast(List[float], d.pop("amountsNative", UNSET))

        prices_native = cast(List[float], d.pop("pricesNative", UNSET))

        pool_address = d.pop("poolAddress", UNSET)

        from_address = d.pop("fromAddress", UNSET)

        to_address = d.pop("toAddress", UNSET)

        _lp_token = d.pop("lpToken", UNSET)
        lp_token: Union[Unset, RestLpToken]
        if isinstance(_lp_token, Unset):
            lp_token = UNSET
        else:
            lp_token = RestLpToken.from_dict(_lp_token)

        rest_transaction_model_v3 = cls(
            type=type,
            network=network,
            timestamp=timestamp,
            transaction_type=transaction_type,
            transaction_address=transaction_address,
            token_addresses=token_addresses,
            symbols=symbols,
            wallets=wallets,
            amounts=amounts,
            amount_stable=amount_stable,
            amounts_stable=amounts_stable,
            prices_stable=prices_stable,
            wallets_categories=wallets_categories,
            amount_native=amount_native,
            amounts_native=amounts_native,
            prices_native=prices_native,
            pool_address=pool_address,
            from_address=from_address,
            to_address=to_address,
            lp_token=lp_token,
        )

        rest_transaction_model_v3.additional_properties = d
        return rest_transaction_model_v3

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

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.holder_type_choices import HolderTypeChoices
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_token_balance_v2 import RestTokenBalanceV2


T = TypeVar("T", bound="RestTraderProfileV2")


@attr.s(auto_attribs=True)
class RestTraderProfileV2:
    """
    Attributes:
        wallet_address (str):
        assets_value (float):
        trading_volume (float):
        wallets_categories (Union[Unset, List[str]]):
        holder_type (Union[Unset, HolderTypeChoices]): An enumeration.
        label (Union[Unset, str]):
        assets_value_change_24h (Union[Unset, float]):
        trading_volume_change_30d (Union[Unset, float]):
        balances (Union[Unset, List['RestTokenBalanceV2']]):
    """

    wallet_address: str
    assets_value: float
    trading_volume: float
    wallets_categories: Union[Unset, List[str]] = UNSET
    holder_type: Union[Unset, HolderTypeChoices] = UNSET
    label: Union[Unset, str] = UNSET
    assets_value_change_24h: Union[Unset, float] = UNSET
    trading_volume_change_30d: Union[Unset, float] = UNSET
    balances: Union[Unset, List["RestTokenBalanceV2"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        wallet_address = self.wallet_address
        assets_value = self.assets_value
        trading_volume = self.trading_volume
        wallets_categories: Union[Unset, List[str]] = UNSET
        if not isinstance(self.wallets_categories, Unset):
            wallets_categories = self.wallets_categories

        holder_type: Union[Unset, str] = UNSET
        if not isinstance(self.holder_type, Unset):
            holder_type = self.holder_type.value

        label = self.label
        assets_value_change_24h = self.assets_value_change_24h
        trading_volume_change_30d = self.trading_volume_change_30d
        balances: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.balances, Unset):
            balances = []
            for balances_item_data in self.balances:
                balances_item = balances_item_data.to_dict()

                balances.append(balances_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "walletAddress": wallet_address,
                "assetsValue": assets_value,
                "tradingVolume": trading_volume,
            }
        )
        if wallets_categories is not UNSET:
            field_dict["walletsCategories"] = wallets_categories
        if holder_type is not UNSET:
            field_dict["holderType"] = holder_type
        if label is not UNSET:
            field_dict["label"] = label
        if assets_value_change_24h is not UNSET:
            field_dict["assetsValueChange24H"] = assets_value_change_24h
        if trading_volume_change_30d is not UNSET:
            field_dict["tradingVolumeChange30D"] = trading_volume_change_30d
        if balances is not UNSET:
            field_dict["balances"] = balances

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.rest_token_balance_v2 import RestTokenBalanceV2

        d = src_dict.copy()
        wallet_address = d.pop("walletAddress")

        assets_value = d.pop("assetsValue")

        trading_volume = d.pop("tradingVolume")

        wallets_categories = cast(List[str], d.pop("walletsCategories", UNSET))

        _holder_type = d.pop("holderType", UNSET)
        holder_type: Union[Unset, HolderTypeChoices]
        if isinstance(_holder_type, Unset):
            holder_type = UNSET
        else:
            holder_type = HolderTypeChoices(_holder_type)

        label = d.pop("label", UNSET)

        assets_value_change_24h = d.pop("assetsValueChange24H", UNSET)

        trading_volume_change_30d = d.pop("tradingVolumeChange30D", UNSET)

        balances = []
        _balances = d.pop("balances", UNSET)
        for balances_item_data in _balances or []:
            balances_item = RestTokenBalanceV2.from_dict(balances_item_data)

            balances.append(balances_item)

        rest_trader_profile_v2 = cls(
            wallet_address=wallet_address,
            assets_value=assets_value,
            trading_volume=trading_volume,
            wallets_categories=wallets_categories,
            holder_type=holder_type,
            label=label,
            assets_value_change_24h=assets_value_change_24h,
            trading_volume_change_30d=trading_volume_change_30d,
            balances=balances,
        )

        rest_trader_profile_v2.additional_properties = d
        return rest_trader_profile_v2

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

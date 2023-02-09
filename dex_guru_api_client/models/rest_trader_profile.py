from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_token_balance import RestTokenBalance


T = TypeVar("T", bound="RestTraderProfile")


@attr.s(auto_attribs=True)
class RestTraderProfile:
    """
    Attributes:
        wallet_address (str):
        wallet_category (str):
        assets_value (float):
        trading_volume (float):
        assets_value_change_24h (Union[Unset, float]):
        trading_volume_change_30d (Union[Unset, float]):
        balances (Union[Unset, List['RestTokenBalance']]):
    """

    wallet_address: str
    wallet_category: str
    assets_value: float
    trading_volume: float
    assets_value_change_24h: Union[Unset, float] = UNSET
    trading_volume_change_30d: Union[Unset, float] = UNSET
    balances: Union[Unset, List["RestTokenBalance"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        wallet_address = self.wallet_address
        wallet_category = self.wallet_category
        assets_value = self.assets_value
        trading_volume = self.trading_volume
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
                "walletCategory": wallet_category,
                "assetsValue": assets_value,
                "tradingVolume": trading_volume,
            }
        )
        if assets_value_change_24h is not UNSET:
            field_dict["assetsValueChange24H"] = assets_value_change_24h
        if trading_volume_change_30d is not UNSET:
            field_dict["tradingVolumeChange30D"] = trading_volume_change_30d
        if balances is not UNSET:
            field_dict["balances"] = balances

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.rest_token_balance import RestTokenBalance

        d = src_dict.copy()
        wallet_address = d.pop("walletAddress")

        wallet_category = d.pop("walletCategory")

        assets_value = d.pop("assetsValue")

        trading_volume = d.pop("tradingVolume")

        assets_value_change_24h = d.pop("assetsValueChange24H", UNSET)

        trading_volume_change_30d = d.pop("tradingVolumeChange30D", UNSET)

        balances = []
        _balances = d.pop("balances", UNSET)
        for balances_item_data in _balances or []:
            balances_item = RestTokenBalance.from_dict(balances_item_data)

            balances.append(balances_item)

        rest_trader_profile = cls(
            wallet_address=wallet_address,
            wallet_category=wallet_category,
            assets_value=assets_value,
            trading_volume=trading_volume,
            assets_value_change_24h=assets_value_change_24h,
            trading_volume_change_30d=trading_volume_change_30d,
            balances=balances,
        )

        rest_trader_profile.additional_properties = d
        return rest_trader_profile

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

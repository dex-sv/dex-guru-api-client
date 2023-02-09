from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aggregation_provider import AggregationProvider
    from ..models.aggregation_provider_deprecated import AggregationProviderDeprecated
    from ..models.block_explorer import BlockExplorer
    from ..models.rest_amm_model import RestAmmModel
    from ..models.rest_token_inventory_static_v3 import RestTokenInventoryStaticV3


T = TypeVar("T", bound="RestChainModelV3")


@attr.s(auto_attribs=True)
class RestChainModelV3:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        type (Union[Unset, str]):
        logo_uri (Union[Unset, str]):
        enabled (Union[Unset, bool]):  Default: True.
        rpc_url (Union[Unset, str]):
        gas_buffer (Union[Unset, int]):
        balances_wss_request (Union[Unset, str]):
        color (Union[Unset, str]):  Default: '#ffffff'.
        primary_token_address (Union[Unset, str]):
        secondary_token_address (Union[Unset, str]):
        amms (Union[Unset, List['RestAmmModel']]):
        most_liquid_tokens (Union[Unset, List['RestTokenInventoryStaticV3']]):
        native_token (Union[Unset, RestTokenInventoryStaticV3]):
        block_explorer (Union[Unset, BlockExplorer]):
        zerox_api (Union[Unset, AggregationProviderDeprecated]):
        one_inch_api (Union[Unset, AggregationProviderDeprecated]):
        market_order (Union[Unset, AggregationProvider]):
        limit_order (Union[Unset, AggregationProvider]):
        gas_url (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    logo_uri: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = True
    rpc_url: Union[Unset, str] = UNSET
    gas_buffer: Union[Unset, int] = UNSET
    balances_wss_request: Union[Unset, str] = UNSET
    color: Union[Unset, str] = "#ffffff"
    primary_token_address: Union[Unset, str] = UNSET
    secondary_token_address: Union[Unset, str] = UNSET
    amms: Union[Unset, List["RestAmmModel"]] = UNSET
    most_liquid_tokens: Union[Unset, List["RestTokenInventoryStaticV3"]] = UNSET
    native_token: Union[Unset, "RestTokenInventoryStaticV3"] = UNSET
    block_explorer: Union[Unset, "BlockExplorer"] = UNSET
    zerox_api: Union[Unset, "AggregationProviderDeprecated"] = UNSET
    one_inch_api: Union[Unset, "AggregationProviderDeprecated"] = UNSET
    market_order: Union[Unset, "AggregationProvider"] = UNSET
    limit_order: Union[Unset, "AggregationProvider"] = UNSET
    gas_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        description = self.description
        type = self.type
        logo_uri = self.logo_uri
        enabled = self.enabled
        rpc_url = self.rpc_url
        gas_buffer = self.gas_buffer
        balances_wss_request = self.balances_wss_request
        color = self.color
        primary_token_address = self.primary_token_address
        secondary_token_address = self.secondary_token_address
        amms: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.amms, Unset):
            amms = []
            for amms_item_data in self.amms:
                amms_item = amms_item_data.to_dict()

                amms.append(amms_item)

        most_liquid_tokens: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.most_liquid_tokens, Unset):
            most_liquid_tokens = []
            for most_liquid_tokens_item_data in self.most_liquid_tokens:
                most_liquid_tokens_item = most_liquid_tokens_item_data.to_dict()

                most_liquid_tokens.append(most_liquid_tokens_item)

        native_token: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.native_token, Unset):
            native_token = self.native_token.to_dict()

        block_explorer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.block_explorer, Unset):
            block_explorer = self.block_explorer.to_dict()

        zerox_api: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.zerox_api, Unset):
            zerox_api = self.zerox_api.to_dict()

        one_inch_api: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.one_inch_api, Unset):
            one_inch_api = self.one_inch_api.to_dict()

        market_order: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.market_order, Unset):
            market_order = self.market_order.to_dict()

        limit_order: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.limit_order, Unset):
            limit_order = self.limit_order.to_dict()

        gas_url = self.gas_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if type is not UNSET:
            field_dict["type"] = type
        if logo_uri is not UNSET:
            field_dict["logo_uri"] = logo_uri
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if rpc_url is not UNSET:
            field_dict["rpc_url"] = rpc_url
        if gas_buffer is not UNSET:
            field_dict["gas_buffer"] = gas_buffer
        if balances_wss_request is not UNSET:
            field_dict["balances_wss_request"] = balances_wss_request
        if color is not UNSET:
            field_dict["color"] = color
        if primary_token_address is not UNSET:
            field_dict["primary_token_address"] = primary_token_address
        if secondary_token_address is not UNSET:
            field_dict["secondary_token_address"] = secondary_token_address
        if amms is not UNSET:
            field_dict["amms"] = amms
        if most_liquid_tokens is not UNSET:
            field_dict["most_liquid_tokens"] = most_liquid_tokens
        if native_token is not UNSET:
            field_dict["native_token"] = native_token
        if block_explorer is not UNSET:
            field_dict["block_explorer"] = block_explorer
        if zerox_api is not UNSET:
            field_dict["zerox_api"] = zerox_api
        if one_inch_api is not UNSET:
            field_dict["one_inch_api"] = one_inch_api
        if market_order is not UNSET:
            field_dict["market_order"] = market_order
        if limit_order is not UNSET:
            field_dict["limit_order"] = limit_order
        if gas_url is not UNSET:
            field_dict["gas_url"] = gas_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.aggregation_provider import AggregationProvider
        from ..models.aggregation_provider_deprecated import AggregationProviderDeprecated
        from ..models.block_explorer import BlockExplorer
        from ..models.rest_amm_model import RestAmmModel
        from ..models.rest_token_inventory_static_v3 import RestTokenInventoryStaticV3

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        type = d.pop("type", UNSET)

        logo_uri = d.pop("logo_uri", UNSET)

        enabled = d.pop("enabled", UNSET)

        rpc_url = d.pop("rpc_url", UNSET)

        gas_buffer = d.pop("gas_buffer", UNSET)

        balances_wss_request = d.pop("balances_wss_request", UNSET)

        color = d.pop("color", UNSET)

        primary_token_address = d.pop("primary_token_address", UNSET)

        secondary_token_address = d.pop("secondary_token_address", UNSET)

        amms = []
        _amms = d.pop("amms", UNSET)
        for amms_item_data in _amms or []:
            amms_item = RestAmmModel.from_dict(amms_item_data)

            amms.append(amms_item)

        most_liquid_tokens = []
        _most_liquid_tokens = d.pop("most_liquid_tokens", UNSET)
        for most_liquid_tokens_item_data in _most_liquid_tokens or []:
            most_liquid_tokens_item = RestTokenInventoryStaticV3.from_dict(most_liquid_tokens_item_data)

            most_liquid_tokens.append(most_liquid_tokens_item)

        _native_token = d.pop("native_token", UNSET)
        native_token: Union[Unset, RestTokenInventoryStaticV3]
        if isinstance(_native_token, Unset):
            native_token = UNSET
        else:
            native_token = RestTokenInventoryStaticV3.from_dict(_native_token)

        _block_explorer = d.pop("block_explorer", UNSET)
        block_explorer: Union[Unset, BlockExplorer]
        if isinstance(_block_explorer, Unset):
            block_explorer = UNSET
        else:
            block_explorer = BlockExplorer.from_dict(_block_explorer)

        _zerox_api = d.pop("zerox_api", UNSET)
        zerox_api: Union[Unset, AggregationProviderDeprecated]
        if isinstance(_zerox_api, Unset):
            zerox_api = UNSET
        else:
            zerox_api = AggregationProviderDeprecated.from_dict(_zerox_api)

        _one_inch_api = d.pop("one_inch_api", UNSET)
        one_inch_api: Union[Unset, AggregationProviderDeprecated]
        if isinstance(_one_inch_api, Unset):
            one_inch_api = UNSET
        else:
            one_inch_api = AggregationProviderDeprecated.from_dict(_one_inch_api)

        _market_order = d.pop("market_order", UNSET)
        market_order: Union[Unset, AggregationProvider]
        if isinstance(_market_order, Unset):
            market_order = UNSET
        else:
            market_order = AggregationProvider.from_dict(_market_order)

        _limit_order = d.pop("limit_order", UNSET)
        limit_order: Union[Unset, AggregationProvider]
        if isinstance(_limit_order, Unset):
            limit_order = UNSET
        else:
            limit_order = AggregationProvider.from_dict(_limit_order)

        gas_url = d.pop("gas_url", UNSET)

        rest_chain_model_v3 = cls(
            id=id,
            name=name,
            description=description,
            type=type,
            logo_uri=logo_uri,
            enabled=enabled,
            rpc_url=rpc_url,
            gas_buffer=gas_buffer,
            balances_wss_request=balances_wss_request,
            color=color,
            primary_token_address=primary_token_address,
            secondary_token_address=secondary_token_address,
            amms=amms,
            most_liquid_tokens=most_liquid_tokens,
            native_token=native_token,
            block_explorer=block_explorer,
            zerox_api=zerox_api,
            one_inch_api=one_inch_api,
            market_order=market_order,
            limit_order=limit_order,
            gas_url=gas_url,
        )

        rest_chain_model_v3.additional_properties = d
        return rest_chain_model_v3

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

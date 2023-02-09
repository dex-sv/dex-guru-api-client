from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_amm_model import RestAmmModel
    from ..models.rest_token_inventory_static import RestTokenInventoryStatic


T = TypeVar("T", bound="RestChainModel")


@attr.s(auto_attribs=True)
class RestChainModel:
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
        most_liquid_tokens (Union[Unset, List['RestTokenInventoryStatic']]):
        color (Union[Unset, str]):  Default: '#ffffff'.
        amms (Union[Unset, List['RestAmmModel']]):
        native_token (Union[Unset, RestTokenInventoryStatic]):
        block_explorer_url (Union[Unset, str]):
        block_explorer_logo_uri (Union[Unset, str]):
        block_explorer_display_name (Union[Unset, str]):
        block_explorer_token_path (Union[Unset, str]):
        block_explorer_address_path (Union[Unset, str]):
        primary_token_address (Union[Unset, str]):
        secondary_token_address (Union[Unset, str]):
        zerox_api_url (Union[Unset, str]):
        zerox_api_wrapper_url (Union[Unset, str]):
        zerox_api_gas_url (Union[Unset, str]):
        zerox_api_wrapper_gas_url (Union[Unset, str]):
        zerox_spender_address (Union[Unset, str]):
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
    most_liquid_tokens: Union[Unset, List["RestTokenInventoryStatic"]] = UNSET
    color: Union[Unset, str] = "#ffffff"
    amms: Union[Unset, List["RestAmmModel"]] = UNSET
    native_token: Union[Unset, "RestTokenInventoryStatic"] = UNSET
    block_explorer_url: Union[Unset, str] = UNSET
    block_explorer_logo_uri: Union[Unset, str] = UNSET
    block_explorer_display_name: Union[Unset, str] = UNSET
    block_explorer_token_path: Union[Unset, str] = UNSET
    block_explorer_address_path: Union[Unset, str] = UNSET
    primary_token_address: Union[Unset, str] = UNSET
    secondary_token_address: Union[Unset, str] = UNSET
    zerox_api_url: Union[Unset, str] = UNSET
    zerox_api_wrapper_url: Union[Unset, str] = UNSET
    zerox_api_gas_url: Union[Unset, str] = UNSET
    zerox_api_wrapper_gas_url: Union[Unset, str] = UNSET
    zerox_spender_address: Union[Unset, str] = UNSET
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
        most_liquid_tokens: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.most_liquid_tokens, Unset):
            most_liquid_tokens = []
            for most_liquid_tokens_item_data in self.most_liquid_tokens:
                most_liquid_tokens_item = most_liquid_tokens_item_data.to_dict()

                most_liquid_tokens.append(most_liquid_tokens_item)

        color = self.color
        amms: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.amms, Unset):
            amms = []
            for amms_item_data in self.amms:
                amms_item = amms_item_data.to_dict()

                amms.append(amms_item)

        native_token: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.native_token, Unset):
            native_token = self.native_token.to_dict()

        block_explorer_url = self.block_explorer_url
        block_explorer_logo_uri = self.block_explorer_logo_uri
        block_explorer_display_name = self.block_explorer_display_name
        block_explorer_token_path = self.block_explorer_token_path
        block_explorer_address_path = self.block_explorer_address_path
        primary_token_address = self.primary_token_address
        secondary_token_address = self.secondary_token_address
        zerox_api_url = self.zerox_api_url
        zerox_api_wrapper_url = self.zerox_api_wrapper_url
        zerox_api_gas_url = self.zerox_api_gas_url
        zerox_api_wrapper_gas_url = self.zerox_api_wrapper_gas_url
        zerox_spender_address = self.zerox_spender_address

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
        if most_liquid_tokens is not UNSET:
            field_dict["most_liquid_tokens"] = most_liquid_tokens
        if color is not UNSET:
            field_dict["color"] = color
        if amms is not UNSET:
            field_dict["amms"] = amms
        if native_token is not UNSET:
            field_dict["native_token"] = native_token
        if block_explorer_url is not UNSET:
            field_dict["block_explorer_url"] = block_explorer_url
        if block_explorer_logo_uri is not UNSET:
            field_dict["block_explorer_logo_uri"] = block_explorer_logo_uri
        if block_explorer_display_name is not UNSET:
            field_dict["block_explorer_display_name"] = block_explorer_display_name
        if block_explorer_token_path is not UNSET:
            field_dict["block_explorer_token_path"] = block_explorer_token_path
        if block_explorer_address_path is not UNSET:
            field_dict["block_explorer_address_path"] = block_explorer_address_path
        if primary_token_address is not UNSET:
            field_dict["primary_token_address"] = primary_token_address
        if secondary_token_address is not UNSET:
            field_dict["secondary_token_address"] = secondary_token_address
        if zerox_api_url is not UNSET:
            field_dict["zerox_api_url"] = zerox_api_url
        if zerox_api_wrapper_url is not UNSET:
            field_dict["zerox_api_wrapper_url"] = zerox_api_wrapper_url
        if zerox_api_gas_url is not UNSET:
            field_dict["zerox_api_gas_url"] = zerox_api_gas_url
        if zerox_api_wrapper_gas_url is not UNSET:
            field_dict["zerox_api_wrapper_gas_url"] = zerox_api_wrapper_gas_url
        if zerox_spender_address is not UNSET:
            field_dict["zerox_spender_address"] = zerox_spender_address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.rest_amm_model import RestAmmModel
        from ..models.rest_token_inventory_static import RestTokenInventoryStatic

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

        most_liquid_tokens = []
        _most_liquid_tokens = d.pop("most_liquid_tokens", UNSET)
        for most_liquid_tokens_item_data in _most_liquid_tokens or []:
            most_liquid_tokens_item = RestTokenInventoryStatic.from_dict(most_liquid_tokens_item_data)

            most_liquid_tokens.append(most_liquid_tokens_item)

        color = d.pop("color", UNSET)

        amms = []
        _amms = d.pop("amms", UNSET)
        for amms_item_data in _amms or []:
            amms_item = RestAmmModel.from_dict(amms_item_data)

            amms.append(amms_item)

        _native_token = d.pop("native_token", UNSET)
        native_token: Union[Unset, RestTokenInventoryStatic]
        if isinstance(_native_token, Unset):
            native_token = UNSET
        else:
            native_token = RestTokenInventoryStatic.from_dict(_native_token)

        block_explorer_url = d.pop("block_explorer_url", UNSET)

        block_explorer_logo_uri = d.pop("block_explorer_logo_uri", UNSET)

        block_explorer_display_name = d.pop("block_explorer_display_name", UNSET)

        block_explorer_token_path = d.pop("block_explorer_token_path", UNSET)

        block_explorer_address_path = d.pop("block_explorer_address_path", UNSET)

        primary_token_address = d.pop("primary_token_address", UNSET)

        secondary_token_address = d.pop("secondary_token_address", UNSET)

        zerox_api_url = d.pop("zerox_api_url", UNSET)

        zerox_api_wrapper_url = d.pop("zerox_api_wrapper_url", UNSET)

        zerox_api_gas_url = d.pop("zerox_api_gas_url", UNSET)

        zerox_api_wrapper_gas_url = d.pop("zerox_api_wrapper_gas_url", UNSET)

        zerox_spender_address = d.pop("zerox_spender_address", UNSET)

        rest_chain_model = cls(
            id=id,
            name=name,
            description=description,
            type=type,
            logo_uri=logo_uri,
            enabled=enabled,
            rpc_url=rpc_url,
            gas_buffer=gas_buffer,
            balances_wss_request=balances_wss_request,
            most_liquid_tokens=most_liquid_tokens,
            color=color,
            amms=amms,
            native_token=native_token,
            block_explorer_url=block_explorer_url,
            block_explorer_logo_uri=block_explorer_logo_uri,
            block_explorer_display_name=block_explorer_display_name,
            block_explorer_token_path=block_explorer_token_path,
            block_explorer_address_path=block_explorer_address_path,
            primary_token_address=primary_token_address,
            secondary_token_address=secondary_token_address,
            zerox_api_url=zerox_api_url,
            zerox_api_wrapper_url=zerox_api_wrapper_url,
            zerox_api_gas_url=zerox_api_gas_url,
            zerox_api_wrapper_gas_url=zerox_api_wrapper_gas_url,
            zerox_spender_address=zerox_spender_address,
        )

        rest_chain_model.additional_properties = d
        return rest_chain_model

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

from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestAmmModel")


@attr.s(auto_attribs=True)
class RestAmmModel:
    """
    Attributes:
        id (Union[Unset, str]):
        chain_id (Union[Unset, int]):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        type (Union[Unset, str]):
        enabled (Union[Unset, bool]):  Default: True.
        last_pair_index (Union[Unset, int]):
        logo_uri (Union[Unset, str]):
        border_color (Union[Unset, str]):
        start_gradient_color (Union[Unset, str]):
        end_gradient_color (Union[Unset, str]):
        display_name (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    chain_id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = True
    last_pair_index: Union[Unset, int] = 0
    logo_uri: Union[Unset, str] = UNSET
    border_color: Union[Unset, str] = UNSET
    start_gradient_color: Union[Unset, str] = UNSET
    end_gradient_color: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        chain_id = self.chain_id
        name = self.name
        description = self.description
        type = self.type
        enabled = self.enabled
        last_pair_index = self.last_pair_index
        logo_uri = self.logo_uri
        border_color = self.border_color
        start_gradient_color: Union[Unset, str]
        if isinstance(self.start_gradient_color, Unset):
            start_gradient_color = UNSET

        else:
            start_gradient_color = self.start_gradient_color

        end_gradient_color: Union[Unset, str]
        if isinstance(self.end_gradient_color, Unset):
            end_gradient_color = UNSET

        else:
            end_gradient_color = self.end_gradient_color

        display_name = self.display_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if chain_id is not UNSET:
            field_dict["chain_id"] = chain_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if type is not UNSET:
            field_dict["type"] = type
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if last_pair_index is not UNSET:
            field_dict["last_pair_index"] = last_pair_index
        if logo_uri is not UNSET:
            field_dict["logo_uri"] = logo_uri
        if border_color is not UNSET:
            field_dict["border_color"] = border_color
        if start_gradient_color is not UNSET:
            field_dict["start_gradient_color"] = start_gradient_color
        if end_gradient_color is not UNSET:
            field_dict["end_gradient_color"] = end_gradient_color
        if display_name is not UNSET:
            field_dict["display_name"] = display_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        chain_id = d.pop("chain_id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        type = d.pop("type", UNSET)

        enabled = d.pop("enabled", UNSET)

        last_pair_index = d.pop("last_pair_index", UNSET)

        logo_uri = d.pop("logo_uri", UNSET)

        border_color = d.pop("border_color", UNSET)

        def _parse_start_gradient_color(data: object) -> Union[Unset, str]:
            if isinstance(data, Unset):
                return data
            return cast(Union[Unset, str], data)

        start_gradient_color = _parse_start_gradient_color(d.pop("start_gradient_color", UNSET))

        def _parse_end_gradient_color(data: object) -> Union[Unset, str]:
            if isinstance(data, Unset):
                return data
            return cast(Union[Unset, str], data)

        end_gradient_color = _parse_end_gradient_color(d.pop("end_gradient_color", UNSET))

        display_name = d.pop("display_name", UNSET)

        rest_amm_model = cls(
            id=id,
            chain_id=chain_id,
            name=name,
            description=description,
            type=type,
            enabled=enabled,
            last_pair_index=last_pair_index,
            logo_uri=logo_uri,
            border_color=border_color,
            start_gradient_color=start_gradient_color,
            end_gradient_color=end_gradient_color,
            display_name=display_name,
        )

        rest_amm_model.additional_properties = d
        return rest_amm_model

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

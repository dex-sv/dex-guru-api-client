from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.transaction_choices import TransactionChoices
from ..types import UNSET, Unset

T = TypeVar("T", bound="BodyGetLastTransactionsV3TokensTransactionsLastPost")


@attr.s(auto_attribs=True)
class BodyGetLastTransactionsV3TokensTransactionsLastPost:
    """
    Attributes:
        transaction_types (Union[Unset, List[TransactionChoices]]): TransactionTypes
        current_token_id (Union[Unset, str]): Token ID
    """

    transaction_types: Union[Unset, List[TransactionChoices]] = UNSET
    current_token_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        transaction_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.transaction_types, Unset):
            transaction_types = []
            for transaction_types_item_data in self.transaction_types:
                transaction_types_item = transaction_types_item_data.value

                transaction_types.append(transaction_types_item)

        current_token_id = self.current_token_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if transaction_types is not UNSET:
            field_dict["transaction_types"] = transaction_types
        if current_token_id is not UNSET:
            field_dict["current_token_id"] = current_token_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        transaction_types = []
        _transaction_types = d.pop("transaction_types", UNSET)
        for transaction_types_item_data in _transaction_types or []:
            transaction_types_item = TransactionChoices(transaction_types_item_data)

            transaction_types.append(transaction_types_item)

        current_token_id = d.pop("current_token_id", UNSET)

        body_get_last_transactions_v3_tokens_transactions_last_post = cls(
            transaction_types=transaction_types,
            current_token_id=current_token_id,
        )

        body_get_last_transactions_v3_tokens_transactions_last_post.additional_properties = d
        return body_get_last_transactions_v3_tokens_transactions_last_post

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

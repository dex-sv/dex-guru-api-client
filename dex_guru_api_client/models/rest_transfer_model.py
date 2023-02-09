from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.transaction_choices import TransactionChoices
from ..types import UNSET, Unset

T = TypeVar("T", bound="RestTransferModel")


@attr.s(auto_attribs=True)
class RestTransferModel:
    """
    Attributes:
        id (str):
        block_number (int):
        symbol (str):
        transaction_address (str):
        timestamp (int):
        network (str):
        token_address (str):
        amount (float):
        amount_usd (float):
        from_wallet_address (str):
        to_wallet_address (str):
        transaction_type (Union[Unset, TransactionChoices]): An enumeration. Default: TransactionChoices.TRANSFER.
    """

    id: str
    block_number: int
    symbol: str
    transaction_address: str
    timestamp: int
    network: str
    token_address: str
    amount: float
    amount_usd: float
    from_wallet_address: str
    to_wallet_address: str
    transaction_type: Union[Unset, TransactionChoices] = TransactionChoices.TRANSFER
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        block_number = self.block_number
        symbol = self.symbol
        transaction_address = self.transaction_address
        timestamp = self.timestamp
        network = self.network
        token_address = self.token_address
        amount = self.amount
        amount_usd = self.amount_usd
        from_wallet_address = self.from_wallet_address
        to_wallet_address = self.to_wallet_address
        transaction_type: Union[Unset, str] = UNSET
        if not isinstance(self.transaction_type, Unset):
            transaction_type = self.transaction_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "blockNumber": block_number,
                "symbol": symbol,
                "transactionAddress": transaction_address,
                "timestamp": timestamp,
                "network": network,
                "tokenAddress": token_address,
                "amount": amount,
                "amountUSD": amount_usd,
                "fromWalletAddress": from_wallet_address,
                "toWalletAddress": to_wallet_address,
            }
        )
        if transaction_type is not UNSET:
            field_dict["transaction_type"] = transaction_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        block_number = d.pop("blockNumber")

        symbol = d.pop("symbol")

        transaction_address = d.pop("transactionAddress")

        timestamp = d.pop("timestamp")

        network = d.pop("network")

        token_address = d.pop("tokenAddress")

        amount = d.pop("amount")

        amount_usd = d.pop("amountUSD")

        from_wallet_address = d.pop("fromWalletAddress")

        to_wallet_address = d.pop("toWalletAddress")

        _transaction_type = d.pop("transaction_type", UNSET)
        transaction_type: Union[Unset, TransactionChoices]
        if isinstance(_transaction_type, Unset):
            transaction_type = UNSET
        else:
            transaction_type = TransactionChoices(_transaction_type)

        rest_transfer_model = cls(
            id=id,
            block_number=block_number,
            symbol=symbol,
            transaction_address=transaction_address,
            timestamp=timestamp,
            network=network,
            token_address=token_address,
            amount=amount,
            amount_usd=amount_usd,
            from_wallet_address=from_wallet_address,
            to_wallet_address=to_wallet_address,
            transaction_type=transaction_type,
        )

        rest_transfer_model.additional_properties = d
        return rest_transfer_model

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

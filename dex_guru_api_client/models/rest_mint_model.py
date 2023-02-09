from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.transaction_choices import TransactionChoices
from ..types import UNSET, Unset

T = TypeVar("T", bound="RestMintModel")


@attr.s(auto_attribs=True)
class RestMintModel:
    """
    Attributes:
        id (str):
        transaction_address (str):
        timestamp (int):
        block_number (int):
        amount0 (float):
        amount1 (float):
        amount_usd (float):
        amount_0usd (float):
        amount_1usd (float):
        amount_eth (float):
        amount_0eth (float):
        amount_1eth (float):
        pair_address (str):
        pair_liquidity_usd (float):
        pair_liquidity_eth (float):
        token_0_address (str):
        token_1_address (str):
        token_0_symbol (str):
        token_1_symbol (str):
        token_0_price_usd (float):
        token_1_price_usd (float):
        token_0_price_eth (float):
        token_1_price_eth (float):
        wallet_address (str):
        amm (str):
        network (str):
        to (Union[Unset, str]):
        sender (Union[Unset, str]):
        wallet_category (Union[Unset, str]):
        transaction_type (Union[Unset, TransactionChoices]): An enumeration. Default: TransactionChoices.MINT.
    """

    id: str
    transaction_address: str
    timestamp: int
    block_number: int
    amount0: float
    amount1: float
    amount_usd: float
    amount_0usd: float
    amount_1usd: float
    amount_eth: float
    amount_0eth: float
    amount_1eth: float
    pair_address: str
    pair_liquidity_usd: float
    pair_liquidity_eth: float
    token_0_address: str
    token_1_address: str
    token_0_symbol: str
    token_1_symbol: str
    token_0_price_usd: float
    token_1_price_usd: float
    token_0_price_eth: float
    token_1_price_eth: float
    wallet_address: str
    amm: str
    network: str
    to: Union[Unset, str] = UNSET
    sender: Union[Unset, str] = UNSET
    wallet_category: Union[Unset, str] = UNSET
    transaction_type: Union[Unset, TransactionChoices] = TransactionChoices.MINT
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        transaction_address = self.transaction_address
        timestamp = self.timestamp
        block_number = self.block_number
        amount0 = self.amount0
        amount1 = self.amount1
        amount_usd = self.amount_usd
        amount_0usd = self.amount_0usd
        amount_1usd = self.amount_1usd
        amount_eth = self.amount_eth
        amount_0eth = self.amount_0eth
        amount_1eth = self.amount_1eth
        pair_address = self.pair_address
        pair_liquidity_usd = self.pair_liquidity_usd
        pair_liquidity_eth = self.pair_liquidity_eth
        token_0_address = self.token_0_address
        token_1_address = self.token_1_address
        token_0_symbol = self.token_0_symbol
        token_1_symbol = self.token_1_symbol
        token_0_price_usd = self.token_0_price_usd
        token_1_price_usd = self.token_1_price_usd
        token_0_price_eth = self.token_0_price_eth
        token_1_price_eth = self.token_1_price_eth
        wallet_address = self.wallet_address
        amm = self.amm
        network = self.network
        to = self.to
        sender = self.sender
        wallet_category = self.wallet_category
        transaction_type: Union[Unset, str] = UNSET
        if not isinstance(self.transaction_type, Unset):
            transaction_type = self.transaction_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "transactionAddress": transaction_address,
                "timestamp": timestamp,
                "blockNumber": block_number,
                "amount0": amount0,
                "amount1": amount1,
                "amountUSD": amount_usd,
                "amount0USD": amount_0usd,
                "amount1USD": amount_1usd,
                "amountETH": amount_eth,
                "amount0ETH": amount_0eth,
                "amount1ETH": amount_1eth,
                "pairAddress": pair_address,
                "pairLiquidityUSD": pair_liquidity_usd,
                "pairLiquidityETH": pair_liquidity_eth,
                "token0Address": token_0_address,
                "token1Address": token_1_address,
                "token0Symbol": token_0_symbol,
                "token1Symbol": token_1_symbol,
                "token0PriceUSD": token_0_price_usd,
                "token1PriceUSD": token_1_price_usd,
                "token0PriceETH": token_0_price_eth,
                "token1PriceETH": token_1_price_eth,
                "walletAddress": wallet_address,
                "AMM": amm,
                "network": network,
            }
        )
        if to is not UNSET:
            field_dict["to"] = to
        if sender is not UNSET:
            field_dict["sender"] = sender
        if wallet_category is not UNSET:
            field_dict["walletCategory"] = wallet_category
        if transaction_type is not UNSET:
            field_dict["transaction_type"] = transaction_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        transaction_address = d.pop("transactionAddress")

        timestamp = d.pop("timestamp")

        block_number = d.pop("blockNumber")

        amount0 = d.pop("amount0")

        amount1 = d.pop("amount1")

        amount_usd = d.pop("amountUSD")

        amount_0usd = d.pop("amount0USD")

        amount_1usd = d.pop("amount1USD")

        amount_eth = d.pop("amountETH")

        amount_0eth = d.pop("amount0ETH")

        amount_1eth = d.pop("amount1ETH")

        pair_address = d.pop("pairAddress")

        pair_liquidity_usd = d.pop("pairLiquidityUSD")

        pair_liquidity_eth = d.pop("pairLiquidityETH")

        token_0_address = d.pop("token0Address")

        token_1_address = d.pop("token1Address")

        token_0_symbol = d.pop("token0Symbol")

        token_1_symbol = d.pop("token1Symbol")

        token_0_price_usd = d.pop("token0PriceUSD")

        token_1_price_usd = d.pop("token1PriceUSD")

        token_0_price_eth = d.pop("token0PriceETH")

        token_1_price_eth = d.pop("token1PriceETH")

        wallet_address = d.pop("walletAddress")

        amm = d.pop("AMM")

        network = d.pop("network")

        to = d.pop("to", UNSET)

        sender = d.pop("sender", UNSET)

        wallet_category = d.pop("walletCategory", UNSET)

        _transaction_type = d.pop("transaction_type", UNSET)
        transaction_type: Union[Unset, TransactionChoices]
        if isinstance(_transaction_type, Unset):
            transaction_type = UNSET
        else:
            transaction_type = TransactionChoices(_transaction_type)

        rest_mint_model = cls(
            id=id,
            transaction_address=transaction_address,
            timestamp=timestamp,
            block_number=block_number,
            amount0=amount0,
            amount1=amount1,
            amount_usd=amount_usd,
            amount_0usd=amount_0usd,
            amount_1usd=amount_1usd,
            amount_eth=amount_eth,
            amount_0eth=amount_0eth,
            amount_1eth=amount_1eth,
            pair_address=pair_address,
            pair_liquidity_usd=pair_liquidity_usd,
            pair_liquidity_eth=pair_liquidity_eth,
            token_0_address=token_0_address,
            token_1_address=token_1_address,
            token_0_symbol=token_0_symbol,
            token_1_symbol=token_1_symbol,
            token_0_price_usd=token_0_price_usd,
            token_1_price_usd=token_1_price_usd,
            token_0_price_eth=token_0_price_eth,
            token_1_price_eth=token_1_price_eth,
            wallet_address=wallet_address,
            amm=amm,
            network=network,
            to=to,
            sender=sender,
            wallet_category=wallet_category,
            transaction_type=transaction_type,
        )

        rest_mint_model.additional_properties = d
        return rest_mint_model

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

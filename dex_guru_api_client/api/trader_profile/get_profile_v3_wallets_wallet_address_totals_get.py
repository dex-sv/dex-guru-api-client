from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.http_validation_error import HTTPValidationError
from ...models.market_type_choices import MarketTypeChoices
from ...models.rest_trader_profile_v2 import RestTraderProfileV2
from ...types import UNSET, Response, Unset


def _get_kwargs(
    wallet_address: str,
    *,
    client: Client,
    is_verified: Union[Unset, None, bool] = False,
    market_type: Union[Unset, None, List[MarketTypeChoices]] = UNSET,
    network: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v3/wallets/{wallet_address}/totals".format(client.base_url, wallet_address=wallet_address)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["is_verified"] = is_verified

    json_market_type: Union[Unset, None, List[str]] = UNSET
    if not isinstance(market_type, Unset):
        if market_type is None:
            json_market_type = None
        else:
            json_market_type = []
            for market_type_item_data in market_type:
                market_type_item = market_type_item_data.value

                json_market_type.append(market_type_item)

    params["market_type"] = json_market_type

    params["network"] = network

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[HTTPValidationError, RestTraderProfileV2]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RestTraderProfileV2.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[HTTPValidationError, RestTraderProfileV2]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    wallet_address: str,
    *,
    client: Client,
    is_verified: Union[Unset, None, bool] = False,
    market_type: Union[Unset, None, List[MarketTypeChoices]] = UNSET,
    network: Union[Unset, None, str] = UNSET,
) -> Response[Union[HTTPValidationError, RestTraderProfileV2]]:
    """Get Profile

    Args:
        wallet_address (str):
        is_verified (Union[Unset, None, bool]): Show only verified tokens
        market_type (Union[Unset, None, List[MarketTypeChoices]]): Filter for tokens by market
            types
        network (Union[Unset, None, str]): Current network in market selector

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTraderProfileV2]]
    """

    kwargs = _get_kwargs(
        wallet_address=wallet_address,
        client=client,
        is_verified=is_verified,
        market_type=market_type,
        network=network,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    wallet_address: str,
    *,
    client: Client,
    is_verified: Union[Unset, None, bool] = False,
    market_type: Union[Unset, None, List[MarketTypeChoices]] = UNSET,
    network: Union[Unset, None, str] = UNSET,
) -> Optional[Union[HTTPValidationError, RestTraderProfileV2]]:
    """Get Profile

    Args:
        wallet_address (str):
        is_verified (Union[Unset, None, bool]): Show only verified tokens
        market_type (Union[Unset, None, List[MarketTypeChoices]]): Filter for tokens by market
            types
        network (Union[Unset, None, str]): Current network in market selector

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTraderProfileV2]]
    """

    return sync_detailed(
        wallet_address=wallet_address,
        client=client,
        is_verified=is_verified,
        market_type=market_type,
        network=network,
    ).parsed


async def asyncio_detailed(
    wallet_address: str,
    *,
    client: Client,
    is_verified: Union[Unset, None, bool] = False,
    market_type: Union[Unset, None, List[MarketTypeChoices]] = UNSET,
    network: Union[Unset, None, str] = UNSET,
) -> Response[Union[HTTPValidationError, RestTraderProfileV2]]:
    """Get Profile

    Args:
        wallet_address (str):
        is_verified (Union[Unset, None, bool]): Show only verified tokens
        market_type (Union[Unset, None, List[MarketTypeChoices]]): Filter for tokens by market
            types
        network (Union[Unset, None, str]): Current network in market selector

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTraderProfileV2]]
    """

    kwargs = _get_kwargs(
        wallet_address=wallet_address,
        client=client,
        is_verified=is_verified,
        market_type=market_type,
        network=network,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    wallet_address: str,
    *,
    client: Client,
    is_verified: Union[Unset, None, bool] = False,
    market_type: Union[Unset, None, List[MarketTypeChoices]] = UNSET,
    network: Union[Unset, None, str] = UNSET,
) -> Optional[Union[HTTPValidationError, RestTraderProfileV2]]:
    """Get Profile

    Args:
        wallet_address (str):
        is_verified (Union[Unset, None, bool]): Show only verified tokens
        market_type (Union[Unset, None, List[MarketTypeChoices]]): Filter for tokens by market
            types
        network (Union[Unset, None, str]): Current network in market selector

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTraderProfileV2]]
    """

    return (
        await asyncio_detailed(
            wallet_address=wallet_address,
            client=client,
            is_verified=is_verified,
            market_type=market_type,
            network=network,
        )
    ).parsed

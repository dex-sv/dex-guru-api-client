from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.http_validation_error import HTTPValidationError
from ...models.rest_trader_profile import RestTraderProfile
from ...types import UNSET, Response, Unset


def _get_kwargs(
    wallet_address: str,
    *,
    client: Client,
    is_verified: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/v2/wallets/{wallet_address}/totals".format(client.base_url, wallet_address=wallet_address)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["is_verified"] = is_verified

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
) -> Optional[Union[HTTPValidationError, RestTraderProfile]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RestTraderProfile.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, RestTraderProfile]]:
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
) -> Response[Union[HTTPValidationError, RestTraderProfile]]:
    """Get Profile

    Args:
        wallet_address (str):
        is_verified (Union[Unset, None, bool]): Show only verified tokens

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTraderProfile]]
    """

    kwargs = _get_kwargs(
        wallet_address=wallet_address,
        client=client,
        is_verified=is_verified,
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
) -> Optional[Union[HTTPValidationError, RestTraderProfile]]:
    """Get Profile

    Args:
        wallet_address (str):
        is_verified (Union[Unset, None, bool]): Show only verified tokens

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTraderProfile]]
    """

    return sync_detailed(
        wallet_address=wallet_address,
        client=client,
        is_verified=is_verified,
    ).parsed


async def asyncio_detailed(
    wallet_address: str,
    *,
    client: Client,
    is_verified: Union[Unset, None, bool] = False,
) -> Response[Union[HTTPValidationError, RestTraderProfile]]:
    """Get Profile

    Args:
        wallet_address (str):
        is_verified (Union[Unset, None, bool]): Show only verified tokens

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTraderProfile]]
    """

    kwargs = _get_kwargs(
        wallet_address=wallet_address,
        client=client,
        is_verified=is_verified,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    wallet_address: str,
    *,
    client: Client,
    is_verified: Union[Unset, None, bool] = False,
) -> Optional[Union[HTTPValidationError, RestTraderProfile]]:
    """Get Profile

    Args:
        wallet_address (str):
        is_verified (Union[Unset, None, bool]): Show only verified tokens

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTraderProfile]]
    """

    return (
        await asyncio_detailed(
            wallet_address=wallet_address,
            client=client,
            is_verified=is_verified,
        )
    ).parsed

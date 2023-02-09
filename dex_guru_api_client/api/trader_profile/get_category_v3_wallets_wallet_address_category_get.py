from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.http_validation_error import HTTPValidationError
from ...models.rest_account_category_v2 import RestAccountCategoryV2
from ...types import Response


def _get_kwargs(
    wallet_address: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/v3/wallets/{wallet_address}/category".format(client.base_url, wallet_address=wallet_address)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[HTTPValidationError, RestAccountCategoryV2]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RestAccountCategoryV2.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, RestAccountCategoryV2]]:
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
) -> Response[Union[HTTPValidationError, RestAccountCategoryV2]]:
    """Get Category

    Args:
        wallet_address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestAccountCategoryV2]]
    """

    kwargs = _get_kwargs(
        wallet_address=wallet_address,
        client=client,
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
) -> Optional[Union[HTTPValidationError, RestAccountCategoryV2]]:
    """Get Category

    Args:
        wallet_address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestAccountCategoryV2]]
    """

    return sync_detailed(
        wallet_address=wallet_address,
        client=client,
    ).parsed


async def asyncio_detailed(
    wallet_address: str,
    *,
    client: Client,
) -> Response[Union[HTTPValidationError, RestAccountCategoryV2]]:
    """Get Category

    Args:
        wallet_address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestAccountCategoryV2]]
    """

    kwargs = _get_kwargs(
        wallet_address=wallet_address,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    wallet_address: str,
    *,
    client: Client,
) -> Optional[Union[HTTPValidationError, RestAccountCategoryV2]]:
    """Get Category

    Args:
        wallet_address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestAccountCategoryV2]]
    """

    return (
        await asyncio_detailed(
            wallet_address=wallet_address,
            client=client,
        )
    ).parsed

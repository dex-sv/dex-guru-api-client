from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.currency_choices import CurrencyChoices
from ...models.http_validation_error import HTTPValidationError
from ...models.rest_tokens_inventory_v2 import RestTokensInventoryV2
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    currency: Union[Unset, None, CurrencyChoices] = CurrencyChoices.USD,
    limit: Union[Unset, None, int] = 30,
    offset: Union[Unset, None, int] = 0,
    only_verified: Union[Unset, None, bool] = True,
    network: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v2/tokens/top/gainers".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_currency: Union[Unset, None, str] = UNSET
    if not isinstance(currency, Unset):
        json_currency = currency.value if currency else None

    params["currency"] = json_currency

    params["limit"] = limit

    params["offset"] = offset

    params["only_verified"] = only_verified

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
) -> Optional[Union[HTTPValidationError, RestTokensInventoryV2]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RestTokensInventoryV2.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, RestTokensInventoryV2]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    currency: Union[Unset, None, CurrencyChoices] = CurrencyChoices.USD,
    limit: Union[Unset, None, int] = 30,
    offset: Union[Unset, None, int] = 0,
    only_verified: Union[Unset, None, bool] = True,
    network: Union[Unset, None, str] = UNSET,
) -> Response[Union[HTTPValidationError, RestTokensInventoryV2]]:
    """Get Tokens Gainers

    Args:
        currency (Union[Unset, None, CurrencyChoices]): An enumeration. Default:
            CurrencyChoices.USD.
        limit (Union[Unset, None, int]): Limit records Default: 30.
        offset (Union[Unset, None, int]): Offset records
        only_verified (Union[Unset, None, bool]): Only verified tokens Default: True.
        network (Union[Unset, None, str]): Comma separated list of any networks:
            eth,optimism,bsc,polygon,fantom,arbitrum,celo,avalanche,gnosis,canto,osmosis,nova

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTokensInventoryV2]]
    """

    kwargs = _get_kwargs(
        client=client,
        currency=currency,
        limit=limit,
        offset=offset,
        only_verified=only_verified,
        network=network,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    currency: Union[Unset, None, CurrencyChoices] = CurrencyChoices.USD,
    limit: Union[Unset, None, int] = 30,
    offset: Union[Unset, None, int] = 0,
    only_verified: Union[Unset, None, bool] = True,
    network: Union[Unset, None, str] = UNSET,
) -> Optional[Union[HTTPValidationError, RestTokensInventoryV2]]:
    """Get Tokens Gainers

    Args:
        currency (Union[Unset, None, CurrencyChoices]): An enumeration. Default:
            CurrencyChoices.USD.
        limit (Union[Unset, None, int]): Limit records Default: 30.
        offset (Union[Unset, None, int]): Offset records
        only_verified (Union[Unset, None, bool]): Only verified tokens Default: True.
        network (Union[Unset, None, str]): Comma separated list of any networks:
            eth,optimism,bsc,polygon,fantom,arbitrum,celo,avalanche,gnosis,canto,osmosis,nova

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTokensInventoryV2]]
    """

    return sync_detailed(
        client=client,
        currency=currency,
        limit=limit,
        offset=offset,
        only_verified=only_verified,
        network=network,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    currency: Union[Unset, None, CurrencyChoices] = CurrencyChoices.USD,
    limit: Union[Unset, None, int] = 30,
    offset: Union[Unset, None, int] = 0,
    only_verified: Union[Unset, None, bool] = True,
    network: Union[Unset, None, str] = UNSET,
) -> Response[Union[HTTPValidationError, RestTokensInventoryV2]]:
    """Get Tokens Gainers

    Args:
        currency (Union[Unset, None, CurrencyChoices]): An enumeration. Default:
            CurrencyChoices.USD.
        limit (Union[Unset, None, int]): Limit records Default: 30.
        offset (Union[Unset, None, int]): Offset records
        only_verified (Union[Unset, None, bool]): Only verified tokens Default: True.
        network (Union[Unset, None, str]): Comma separated list of any networks:
            eth,optimism,bsc,polygon,fantom,arbitrum,celo,avalanche,gnosis,canto,osmosis,nova

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTokensInventoryV2]]
    """

    kwargs = _get_kwargs(
        client=client,
        currency=currency,
        limit=limit,
        offset=offset,
        only_verified=only_verified,
        network=network,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    currency: Union[Unset, None, CurrencyChoices] = CurrencyChoices.USD,
    limit: Union[Unset, None, int] = 30,
    offset: Union[Unset, None, int] = 0,
    only_verified: Union[Unset, None, bool] = True,
    network: Union[Unset, None, str] = UNSET,
) -> Optional[Union[HTTPValidationError, RestTokensInventoryV2]]:
    """Get Tokens Gainers

    Args:
        currency (Union[Unset, None, CurrencyChoices]): An enumeration. Default:
            CurrencyChoices.USD.
        limit (Union[Unset, None, int]): Limit records Default: 30.
        offset (Union[Unset, None, int]): Offset records
        only_verified (Union[Unset, None, bool]): Only verified tokens Default: True.
        network (Union[Unset, None, str]): Comma separated list of any networks:
            eth,optimism,bsc,polygon,fantom,arbitrum,celo,avalanche,gnosis,canto,osmosis,nova

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTokensInventoryV2]]
    """

    return (
        await asyncio_detailed(
            client=client,
            currency=currency,
            limit=limit,
            offset=offset,
            only_verified=only_verified,
            network=network,
        )
    ).parsed

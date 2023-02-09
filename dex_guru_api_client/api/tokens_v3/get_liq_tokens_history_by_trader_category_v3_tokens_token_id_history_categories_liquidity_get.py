from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.currency_choices import CurrencyChoices
from ...models.http_validation_error import HTTPValidationError
from ...models.rest_liq_history_by_categories import RestLiqHistoryByCategories
from ...types import UNSET, Response, Unset


def _get_kwargs(
    token_id: str,
    *,
    client: Client,
    begin_timestamp: Union[Unset, None, int] = UNSET,
    end_timestamp: Union[Unset, None, int] = UNSET,
    currency: Union[Unset, None, CurrencyChoices] = CurrencyChoices.USD,
) -> Dict[str, Any]:
    url = "{}/v3/tokens/{token_id}/history/categories/liquidity".format(client.base_url, token_id=token_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["begin_timestamp"] = begin_timestamp

    params["end_timestamp"] = end_timestamp

    json_currency: Union[Unset, None, str] = UNSET
    if not isinstance(currency, Unset):
        json_currency = currency.value if currency else None

    params["currency"] = json_currency

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
) -> Optional[Union[HTTPValidationError, RestLiqHistoryByCategories]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RestLiqHistoryByCategories.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, RestLiqHistoryByCategories]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    token_id: str,
    *,
    client: Client,
    begin_timestamp: Union[Unset, None, int] = UNSET,
    end_timestamp: Union[Unset, None, int] = UNSET,
    currency: Union[Unset, None, CurrencyChoices] = CurrencyChoices.USD,
) -> Response[Union[HTTPValidationError, RestLiqHistoryByCategories]]:
    """Get Liq Tokens History By Trader Category

    Args:
        token_id (str): Token ID
        begin_timestamp (Union[Unset, None, int]):
        end_timestamp (Union[Unset, None, int]):
        currency (Union[Unset, None, CurrencyChoices]): An enumeration. Default:
            CurrencyChoices.USD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestLiqHistoryByCategories]]
    """

    kwargs = _get_kwargs(
        token_id=token_id,
        client=client,
        begin_timestamp=begin_timestamp,
        end_timestamp=end_timestamp,
        currency=currency,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    token_id: str,
    *,
    client: Client,
    begin_timestamp: Union[Unset, None, int] = UNSET,
    end_timestamp: Union[Unset, None, int] = UNSET,
    currency: Union[Unset, None, CurrencyChoices] = CurrencyChoices.USD,
) -> Optional[Union[HTTPValidationError, RestLiqHistoryByCategories]]:
    """Get Liq Tokens History By Trader Category

    Args:
        token_id (str): Token ID
        begin_timestamp (Union[Unset, None, int]):
        end_timestamp (Union[Unset, None, int]):
        currency (Union[Unset, None, CurrencyChoices]): An enumeration. Default:
            CurrencyChoices.USD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestLiqHistoryByCategories]]
    """

    return sync_detailed(
        token_id=token_id,
        client=client,
        begin_timestamp=begin_timestamp,
        end_timestamp=end_timestamp,
        currency=currency,
    ).parsed


async def asyncio_detailed(
    token_id: str,
    *,
    client: Client,
    begin_timestamp: Union[Unset, None, int] = UNSET,
    end_timestamp: Union[Unset, None, int] = UNSET,
    currency: Union[Unset, None, CurrencyChoices] = CurrencyChoices.USD,
) -> Response[Union[HTTPValidationError, RestLiqHistoryByCategories]]:
    """Get Liq Tokens History By Trader Category

    Args:
        token_id (str): Token ID
        begin_timestamp (Union[Unset, None, int]):
        end_timestamp (Union[Unset, None, int]):
        currency (Union[Unset, None, CurrencyChoices]): An enumeration. Default:
            CurrencyChoices.USD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestLiqHistoryByCategories]]
    """

    kwargs = _get_kwargs(
        token_id=token_id,
        client=client,
        begin_timestamp=begin_timestamp,
        end_timestamp=end_timestamp,
        currency=currency,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    token_id: str,
    *,
    client: Client,
    begin_timestamp: Union[Unset, None, int] = UNSET,
    end_timestamp: Union[Unset, None, int] = UNSET,
    currency: Union[Unset, None, CurrencyChoices] = CurrencyChoices.USD,
) -> Optional[Union[HTTPValidationError, RestLiqHistoryByCategories]]:
    """Get Liq Tokens History By Trader Category

    Args:
        token_id (str): Token ID
        begin_timestamp (Union[Unset, None, int]):
        end_timestamp (Union[Unset, None, int]):
        currency (Union[Unset, None, CurrencyChoices]): An enumeration. Default:
            CurrencyChoices.USD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestLiqHistoryByCategories]]
    """

    return (
        await asyncio_detailed(
            token_id=token_id,
            client=client,
            begin_timestamp=begin_timestamp,
            end_timestamp=end_timestamp,
            currency=currency,
        )
    ).parsed

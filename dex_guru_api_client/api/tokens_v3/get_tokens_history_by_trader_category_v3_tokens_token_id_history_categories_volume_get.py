from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.categories_choices import CategoriesChoices
from ...models.currency_choices import CurrencyChoices
from ...models.http_validation_error import HTTPValidationError
from ...models.interval_choices import IntervalChoices
from ...models.liquidity_categories_choices import LiquidityCategoriesChoices
from ...models.rest_volume_history_by_categories import RestVolumeHistoryByCategories
from ...types import UNSET, Response, Unset


def _get_kwargs(
    token_id: str,
    *,
    client: Client,
    begin_timestamp: Union[Unset, None, int] = UNSET,
    end_timestamp: Union[Unset, None, int] = UNSET,
    currency: Union[Unset, None, CurrencyChoices] = CurrencyChoices.USD,
    interval: Union[Unset, None, IntervalChoices] = IntervalChoices.VALUE_86400,
    trader_category: Union[CategoriesChoices, LiquidityCategoriesChoices, None, Unset] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v3/tokens/{token_id}/history/categories/volume".format(client.base_url, token_id=token_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["begin_timestamp"] = begin_timestamp

    params["end_timestamp"] = end_timestamp

    json_currency: Union[Unset, None, str] = UNSET
    if not isinstance(currency, Unset):
        json_currency = currency.value if currency else None

    params["currency"] = json_currency

    json_interval: Union[Unset, None, int] = UNSET
    if not isinstance(interval, Unset):
        json_interval = interval.value if interval else None

    params["interval"] = json_interval

    json_trader_category: Union[None, Unset, str]
    if isinstance(trader_category, Unset):
        json_trader_category = UNSET
    elif trader_category is None:
        json_trader_category = None

    elif isinstance(trader_category, CategoriesChoices):
        json_trader_category = UNSET
        if not isinstance(trader_category, Unset):
            json_trader_category = trader_category.value

    else:
        json_trader_category = UNSET
        if not isinstance(trader_category, Unset):
            json_trader_category = trader_category.value

    params["trader_category"] = json_trader_category

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
) -> Optional[Union[HTTPValidationError, RestVolumeHistoryByCategories]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RestVolumeHistoryByCategories.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, RestVolumeHistoryByCategories]]:
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
    interval: Union[Unset, None, IntervalChoices] = IntervalChoices.VALUE_86400,
    trader_category: Union[CategoriesChoices, LiquidityCategoriesChoices, None, Unset] = UNSET,
) -> Response[Union[HTTPValidationError, RestVolumeHistoryByCategories]]:
    """Get Tokens History By Trader Category

    Args:
        token_id (str): Token ID
        begin_timestamp (Union[Unset, None, int]):
        end_timestamp (Union[Unset, None, int]):
        currency (Union[Unset, None, CurrencyChoices]): An enumeration. Default:
            CurrencyChoices.USD.
        interval (Union[Unset, None, IntervalChoices]): An enumeration. Default:
            IntervalChoices.VALUE_86400.
        trader_category (Union[CategoriesChoices, LiquidityCategoriesChoices, None, Unset]):
            Trader category

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestVolumeHistoryByCategories]]
    """

    kwargs = _get_kwargs(
        token_id=token_id,
        client=client,
        begin_timestamp=begin_timestamp,
        end_timestamp=end_timestamp,
        currency=currency,
        interval=interval,
        trader_category=trader_category,
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
    interval: Union[Unset, None, IntervalChoices] = IntervalChoices.VALUE_86400,
    trader_category: Union[CategoriesChoices, LiquidityCategoriesChoices, None, Unset] = UNSET,
) -> Optional[Union[HTTPValidationError, RestVolumeHistoryByCategories]]:
    """Get Tokens History By Trader Category

    Args:
        token_id (str): Token ID
        begin_timestamp (Union[Unset, None, int]):
        end_timestamp (Union[Unset, None, int]):
        currency (Union[Unset, None, CurrencyChoices]): An enumeration. Default:
            CurrencyChoices.USD.
        interval (Union[Unset, None, IntervalChoices]): An enumeration. Default:
            IntervalChoices.VALUE_86400.
        trader_category (Union[CategoriesChoices, LiquidityCategoriesChoices, None, Unset]):
            Trader category

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestVolumeHistoryByCategories]]
    """

    return sync_detailed(
        token_id=token_id,
        client=client,
        begin_timestamp=begin_timestamp,
        end_timestamp=end_timestamp,
        currency=currency,
        interval=interval,
        trader_category=trader_category,
    ).parsed


async def asyncio_detailed(
    token_id: str,
    *,
    client: Client,
    begin_timestamp: Union[Unset, None, int] = UNSET,
    end_timestamp: Union[Unset, None, int] = UNSET,
    currency: Union[Unset, None, CurrencyChoices] = CurrencyChoices.USD,
    interval: Union[Unset, None, IntervalChoices] = IntervalChoices.VALUE_86400,
    trader_category: Union[CategoriesChoices, LiquidityCategoriesChoices, None, Unset] = UNSET,
) -> Response[Union[HTTPValidationError, RestVolumeHistoryByCategories]]:
    """Get Tokens History By Trader Category

    Args:
        token_id (str): Token ID
        begin_timestamp (Union[Unset, None, int]):
        end_timestamp (Union[Unset, None, int]):
        currency (Union[Unset, None, CurrencyChoices]): An enumeration. Default:
            CurrencyChoices.USD.
        interval (Union[Unset, None, IntervalChoices]): An enumeration. Default:
            IntervalChoices.VALUE_86400.
        trader_category (Union[CategoriesChoices, LiquidityCategoriesChoices, None, Unset]):
            Trader category

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestVolumeHistoryByCategories]]
    """

    kwargs = _get_kwargs(
        token_id=token_id,
        client=client,
        begin_timestamp=begin_timestamp,
        end_timestamp=end_timestamp,
        currency=currency,
        interval=interval,
        trader_category=trader_category,
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
    interval: Union[Unset, None, IntervalChoices] = IntervalChoices.VALUE_86400,
    trader_category: Union[CategoriesChoices, LiquidityCategoriesChoices, None, Unset] = UNSET,
) -> Optional[Union[HTTPValidationError, RestVolumeHistoryByCategories]]:
    """Get Tokens History By Trader Category

    Args:
        token_id (str): Token ID
        begin_timestamp (Union[Unset, None, int]):
        end_timestamp (Union[Unset, None, int]):
        currency (Union[Unset, None, CurrencyChoices]): An enumeration. Default:
            CurrencyChoices.USD.
        interval (Union[Unset, None, IntervalChoices]): An enumeration. Default:
            IntervalChoices.VALUE_86400.
        trader_category (Union[CategoriesChoices, LiquidityCategoriesChoices, None, Unset]):
            Trader category

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestVolumeHistoryByCategories]]
    """

    return (
        await asyncio_detailed(
            token_id=token_id,
            client=client,
            begin_timestamp=begin_timestamp,
            end_timestamp=end_timestamp,
            currency=currency,
            interval=interval,
            trader_category=trader_category,
        )
    ).parsed

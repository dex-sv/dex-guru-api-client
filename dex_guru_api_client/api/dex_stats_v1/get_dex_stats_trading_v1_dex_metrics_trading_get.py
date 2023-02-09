from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.currency_choices import CurrencyChoices
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    begin_timestamp: int,
    end_timestamp: int,
    interval: Union[Unset, None, int] = 86400,
    token_address: Union[Unset, None, str] = UNSET,
    chain_id: Union[Unset, None, int] = UNSET,
    currency: Union[Unset, None, CurrencyChoices] = CurrencyChoices.S,
) -> Dict[str, Any]:
    url = "{}/v1/dex/metrics/trading".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["begin_timestamp"] = begin_timestamp

    params["end_timestamp"] = end_timestamp

    params["interval"] = interval

    params["token_address"] = token_address

    params["chain_id"] = chain_id

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(Any, response.json())
        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    begin_timestamp: int,
    end_timestamp: int,
    interval: Union[Unset, None, int] = 86400,
    token_address: Union[Unset, None, str] = UNSET,
    chain_id: Union[Unset, None, int] = UNSET,
    currency: Union[Unset, None, CurrencyChoices] = CurrencyChoices.S,
) -> Response[Union[Any, HTTPValidationError]]:
    """Get Dex Stats Trading

    Args:
        begin_timestamp (int):
        end_timestamp (int):
        interval (Union[Unset, None, int]):  Default: 86400.
        token_address (Union[Unset, None, str]):
        chain_id (Union[Unset, None, int]):
        currency (Union[Unset, None, CurrencyChoices]): An enumeration. Default:
            CurrencyChoices.S.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        client=client,
        begin_timestamp=begin_timestamp,
        end_timestamp=end_timestamp,
        interval=interval,
        token_address=token_address,
        chain_id=chain_id,
        currency=currency,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    begin_timestamp: int,
    end_timestamp: int,
    interval: Union[Unset, None, int] = 86400,
    token_address: Union[Unset, None, str] = UNSET,
    chain_id: Union[Unset, None, int] = UNSET,
    currency: Union[Unset, None, CurrencyChoices] = CurrencyChoices.S,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Get Dex Stats Trading

    Args:
        begin_timestamp (int):
        end_timestamp (int):
        interval (Union[Unset, None, int]):  Default: 86400.
        token_address (Union[Unset, None, str]):
        chain_id (Union[Unset, None, int]):
        currency (Union[Unset, None, CurrencyChoices]): An enumeration. Default:
            CurrencyChoices.S.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    return sync_detailed(
        client=client,
        begin_timestamp=begin_timestamp,
        end_timestamp=end_timestamp,
        interval=interval,
        token_address=token_address,
        chain_id=chain_id,
        currency=currency,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    begin_timestamp: int,
    end_timestamp: int,
    interval: Union[Unset, None, int] = 86400,
    token_address: Union[Unset, None, str] = UNSET,
    chain_id: Union[Unset, None, int] = UNSET,
    currency: Union[Unset, None, CurrencyChoices] = CurrencyChoices.S,
) -> Response[Union[Any, HTTPValidationError]]:
    """Get Dex Stats Trading

    Args:
        begin_timestamp (int):
        end_timestamp (int):
        interval (Union[Unset, None, int]):  Default: 86400.
        token_address (Union[Unset, None, str]):
        chain_id (Union[Unset, None, int]):
        currency (Union[Unset, None, CurrencyChoices]): An enumeration. Default:
            CurrencyChoices.S.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        client=client,
        begin_timestamp=begin_timestamp,
        end_timestamp=end_timestamp,
        interval=interval,
        token_address=token_address,
        chain_id=chain_id,
        currency=currency,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    begin_timestamp: int,
    end_timestamp: int,
    interval: Union[Unset, None, int] = 86400,
    token_address: Union[Unset, None, str] = UNSET,
    chain_id: Union[Unset, None, int] = UNSET,
    currency: Union[Unset, None, CurrencyChoices] = CurrencyChoices.S,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Get Dex Stats Trading

    Args:
        begin_timestamp (int):
        end_timestamp (int):
        interval (Union[Unset, None, int]):  Default: 86400.
        token_address (Union[Unset, None, str]):
        chain_id (Union[Unset, None, int]):
        currency (Union[Unset, None, CurrencyChoices]): An enumeration. Default:
            CurrencyChoices.S.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    return (
        await asyncio_detailed(
            client=client,
            begin_timestamp=begin_timestamp,
            end_timestamp=end_timestamp,
            interval=interval,
            token_address=token_address,
            chain_id=chain_id,
            currency=currency,
        )
    ).parsed

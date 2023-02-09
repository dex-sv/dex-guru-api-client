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
    symbol: str,
    resolution: str,
    from_: int,
    to: int,
    currency_code: Union[Unset, None, CurrencyChoices] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/tradingview/history".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["symbol"] = symbol

    params["resolution"] = resolution

    params["from"] = from_

    params["to"] = to

    json_currency_code: Union[Unset, None, str] = UNSET
    if not isinstance(currency_code, Unset):
        json_currency_code = currency_code.value if currency_code else None

    params["currencyCode"] = json_currency_code

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
    symbol: str,
    resolution: str,
    from_: int,
    to: int,
    currency_code: Union[Unset, None, CurrencyChoices] = UNSET,
) -> Response[Union[Any, HTTPValidationError]]:
    """Get History

     We not need return ValidationError with status 422, we return empty_tradingview_history now.
    See try-except in function new_tradingview below.

    Args:
        symbol (str): Symbol for search
        resolution (str): Resolution
        from_ (int):
        to (int):
        currency_code (Union[Unset, None, CurrencyChoices]): An enumeration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        client=client,
        symbol=symbol,
        resolution=resolution,
        from_=from_,
        to=to,
        currency_code=currency_code,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    symbol: str,
    resolution: str,
    from_: int,
    to: int,
    currency_code: Union[Unset, None, CurrencyChoices] = UNSET,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Get History

     We not need return ValidationError with status 422, we return empty_tradingview_history now.
    See try-except in function new_tradingview below.

    Args:
        symbol (str): Symbol for search
        resolution (str): Resolution
        from_ (int):
        to (int):
        currency_code (Union[Unset, None, CurrencyChoices]): An enumeration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    return sync_detailed(
        client=client,
        symbol=symbol,
        resolution=resolution,
        from_=from_,
        to=to,
        currency_code=currency_code,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    symbol: str,
    resolution: str,
    from_: int,
    to: int,
    currency_code: Union[Unset, None, CurrencyChoices] = UNSET,
) -> Response[Union[Any, HTTPValidationError]]:
    """Get History

     We not need return ValidationError with status 422, we return empty_tradingview_history now.
    See try-except in function new_tradingview below.

    Args:
        symbol (str): Symbol for search
        resolution (str): Resolution
        from_ (int):
        to (int):
        currency_code (Union[Unset, None, CurrencyChoices]): An enumeration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        client=client,
        symbol=symbol,
        resolution=resolution,
        from_=from_,
        to=to,
        currency_code=currency_code,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    symbol: str,
    resolution: str,
    from_: int,
    to: int,
    currency_code: Union[Unset, None, CurrencyChoices] = UNSET,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Get History

     We not need return ValidationError with status 422, we return empty_tradingview_history now.
    See try-except in function new_tradingview below.

    Args:
        symbol (str): Symbol for search
        resolution (str): Resolution
        from_ (int):
        to (int):
        currency_code (Union[Unset, None, CurrencyChoices]): An enumeration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    return (
        await asyncio_detailed(
            client=client,
            symbol=symbol,
            resolution=resolution,
            from_=from_,
            to=to,
            currency_code=currency_code,
        )
    ).parsed

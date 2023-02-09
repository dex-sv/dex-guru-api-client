from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.currency_choices import CurrencyChoices
from ...models.http_validation_error import HTTPValidationError
from ...models.rest_balance_mark import RestBalanceMark
from ...types import UNSET, Response, Unset


def _get_kwargs(
    token_id: str,
    wallet_address: str,
    *,
    client: Client,
    from_: int,
    to: int,
    resolution: str,
    currency_code: Union[Unset, None, CurrencyChoices] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/tokens/{token_id}/wallets/{wallet_address}/balance_marks".format(
        client.base_url, token_id=token_id, wallet_address=wallet_address
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["from"] = from_

    params["to"] = to

    params["resolution"] = resolution

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


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[HTTPValidationError, List["RestBalanceMark"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RestBalanceMark.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Union[HTTPValidationError, List["RestBalanceMark"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    token_id: str,
    wallet_address: str,
    *,
    client: Client,
    from_: int,
    to: int,
    resolution: str,
    currency_code: Union[Unset, None, CurrencyChoices] = UNSET,
) -> Response[Union[HTTPValidationError, List["RestBalanceMark"]]]:
    """Get Buy Sell Marks For Token By Wallet

    Args:
        token_id (str):
        wallet_address (str):
        from_ (int):
        to (int):
        resolution (str): Resolution
        currency_code (Union[Unset, None, CurrencyChoices]): An enumeration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List['RestBalanceMark']]]
    """

    kwargs = _get_kwargs(
        token_id=token_id,
        wallet_address=wallet_address,
        client=client,
        from_=from_,
        to=to,
        resolution=resolution,
        currency_code=currency_code,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    token_id: str,
    wallet_address: str,
    *,
    client: Client,
    from_: int,
    to: int,
    resolution: str,
    currency_code: Union[Unset, None, CurrencyChoices] = UNSET,
) -> Optional[Union[HTTPValidationError, List["RestBalanceMark"]]]:
    """Get Buy Sell Marks For Token By Wallet

    Args:
        token_id (str):
        wallet_address (str):
        from_ (int):
        to (int):
        resolution (str): Resolution
        currency_code (Union[Unset, None, CurrencyChoices]): An enumeration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List['RestBalanceMark']]]
    """

    return sync_detailed(
        token_id=token_id,
        wallet_address=wallet_address,
        client=client,
        from_=from_,
        to=to,
        resolution=resolution,
        currency_code=currency_code,
    ).parsed


async def asyncio_detailed(
    token_id: str,
    wallet_address: str,
    *,
    client: Client,
    from_: int,
    to: int,
    resolution: str,
    currency_code: Union[Unset, None, CurrencyChoices] = UNSET,
) -> Response[Union[HTTPValidationError, List["RestBalanceMark"]]]:
    """Get Buy Sell Marks For Token By Wallet

    Args:
        token_id (str):
        wallet_address (str):
        from_ (int):
        to (int):
        resolution (str): Resolution
        currency_code (Union[Unset, None, CurrencyChoices]): An enumeration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List['RestBalanceMark']]]
    """

    kwargs = _get_kwargs(
        token_id=token_id,
        wallet_address=wallet_address,
        client=client,
        from_=from_,
        to=to,
        resolution=resolution,
        currency_code=currency_code,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    token_id: str,
    wallet_address: str,
    *,
    client: Client,
    from_: int,
    to: int,
    resolution: str,
    currency_code: Union[Unset, None, CurrencyChoices] = UNSET,
) -> Optional[Union[HTTPValidationError, List["RestBalanceMark"]]]:
    """Get Buy Sell Marks For Token By Wallet

    Args:
        token_id (str):
        wallet_address (str):
        from_ (int):
        to (int):
        resolution (str): Resolution
        currency_code (Union[Unset, None, CurrencyChoices]): An enumeration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List['RestBalanceMark']]]
    """

    return (
        await asyncio_detailed(
            token_id=token_id,
            wallet_address=wallet_address,
            client=client,
            from_=from_,
            to=to,
            resolution=resolution,
            currency_code=currency_code,
        )
    ).parsed

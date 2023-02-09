from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.get_chart_for_token_v1_tokens_token_id_wallets_wallet_address_chart_get_interval import (
    GetChartForTokenV1TokensTokenIdWalletsWalletAddressChartGetInterval,
)
from ...models.get_chart_for_token_v1_tokens_token_id_wallets_wallet_address_chart_get_period import (
    GetChartForTokenV1TokensTokenIdWalletsWalletAddressChartGetPeriod,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    token_id: str,
    wallet_address: str,
    *,
    client: Client,
    begin_timestamp: Union[Unset, None, int] = 1588723228,
    interval: Union[
        Unset, None, GetChartForTokenV1TokensTokenIdWalletsWalletAddressChartGetInterval
    ] = GetChartForTokenV1TokensTokenIdWalletsWalletAddressChartGetInterval.HOUR,
    period: Union[Unset, None, GetChartForTokenV1TokensTokenIdWalletsWalletAddressChartGetPeriod] = UNSET,
    no_price: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/v1/tokens/{token_id}/wallets/{wallet_address}/chart".format(
        client.base_url, token_id=token_id, wallet_address=wallet_address
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["begin_timestamp"] = begin_timestamp

    json_interval: Union[Unset, None, str] = UNSET
    if not isinstance(interval, Unset):
        json_interval = interval.value if interval else None

    params["interval"] = json_interval

    json_period: Union[Unset, None, str] = UNSET
    if not isinstance(period, Unset):
        json_period = period.value if period else None

    params["period"] = json_period

    params["no_price"] = no_price

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
    token_id: str,
    wallet_address: str,
    *,
    client: Client,
    begin_timestamp: Union[Unset, None, int] = 1588723228,
    interval: Union[
        Unset, None, GetChartForTokenV1TokensTokenIdWalletsWalletAddressChartGetInterval
    ] = GetChartForTokenV1TokensTokenIdWalletsWalletAddressChartGetInterval.HOUR,
    period: Union[Unset, None, GetChartForTokenV1TokensTokenIdWalletsWalletAddressChartGetPeriod] = UNSET,
    no_price: Union[Unset, None, bool] = False,
) -> Response[Union[Any, HTTPValidationError]]:
    """Get Chart For Token

    Args:
        token_id (str):
        wallet_address (str):
        begin_timestamp (Union[Unset, None, int]): Begin timestamp Default: 1588723228.
        interval (Union[Unset, None,
            GetChartForTokenV1TokensTokenIdWalletsWalletAddressChartGetInterval]): Interval for
            points. Default: hour Default:
            GetChartForTokenV1TokensTokenIdWalletsWalletAddressChartGetInterval.HOUR.
        period (Union[Unset, None,
            GetChartForTokenV1TokensTokenIdWalletsWalletAddressChartGetPeriod]): Calculate interval
            and begin timestamp
        no_price (Union[Unset, None, bool]): Skip request prices chart

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        token_id=token_id,
        wallet_address=wallet_address,
        client=client,
        begin_timestamp=begin_timestamp,
        interval=interval,
        period=period,
        no_price=no_price,
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
    begin_timestamp: Union[Unset, None, int] = 1588723228,
    interval: Union[
        Unset, None, GetChartForTokenV1TokensTokenIdWalletsWalletAddressChartGetInterval
    ] = GetChartForTokenV1TokensTokenIdWalletsWalletAddressChartGetInterval.HOUR,
    period: Union[Unset, None, GetChartForTokenV1TokensTokenIdWalletsWalletAddressChartGetPeriod] = UNSET,
    no_price: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Get Chart For Token

    Args:
        token_id (str):
        wallet_address (str):
        begin_timestamp (Union[Unset, None, int]): Begin timestamp Default: 1588723228.
        interval (Union[Unset, None,
            GetChartForTokenV1TokensTokenIdWalletsWalletAddressChartGetInterval]): Interval for
            points. Default: hour Default:
            GetChartForTokenV1TokensTokenIdWalletsWalletAddressChartGetInterval.HOUR.
        period (Union[Unset, None,
            GetChartForTokenV1TokensTokenIdWalletsWalletAddressChartGetPeriod]): Calculate interval
            and begin timestamp
        no_price (Union[Unset, None, bool]): Skip request prices chart

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    return sync_detailed(
        token_id=token_id,
        wallet_address=wallet_address,
        client=client,
        begin_timestamp=begin_timestamp,
        interval=interval,
        period=period,
        no_price=no_price,
    ).parsed


async def asyncio_detailed(
    token_id: str,
    wallet_address: str,
    *,
    client: Client,
    begin_timestamp: Union[Unset, None, int] = 1588723228,
    interval: Union[
        Unset, None, GetChartForTokenV1TokensTokenIdWalletsWalletAddressChartGetInterval
    ] = GetChartForTokenV1TokensTokenIdWalletsWalletAddressChartGetInterval.HOUR,
    period: Union[Unset, None, GetChartForTokenV1TokensTokenIdWalletsWalletAddressChartGetPeriod] = UNSET,
    no_price: Union[Unset, None, bool] = False,
) -> Response[Union[Any, HTTPValidationError]]:
    """Get Chart For Token

    Args:
        token_id (str):
        wallet_address (str):
        begin_timestamp (Union[Unset, None, int]): Begin timestamp Default: 1588723228.
        interval (Union[Unset, None,
            GetChartForTokenV1TokensTokenIdWalletsWalletAddressChartGetInterval]): Interval for
            points. Default: hour Default:
            GetChartForTokenV1TokensTokenIdWalletsWalletAddressChartGetInterval.HOUR.
        period (Union[Unset, None,
            GetChartForTokenV1TokensTokenIdWalletsWalletAddressChartGetPeriod]): Calculate interval
            and begin timestamp
        no_price (Union[Unset, None, bool]): Skip request prices chart

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        token_id=token_id,
        wallet_address=wallet_address,
        client=client,
        begin_timestamp=begin_timestamp,
        interval=interval,
        period=period,
        no_price=no_price,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    token_id: str,
    wallet_address: str,
    *,
    client: Client,
    begin_timestamp: Union[Unset, None, int] = 1588723228,
    interval: Union[
        Unset, None, GetChartForTokenV1TokensTokenIdWalletsWalletAddressChartGetInterval
    ] = GetChartForTokenV1TokensTokenIdWalletsWalletAddressChartGetInterval.HOUR,
    period: Union[Unset, None, GetChartForTokenV1TokensTokenIdWalletsWalletAddressChartGetPeriod] = UNSET,
    no_price: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Get Chart For Token

    Args:
        token_id (str):
        wallet_address (str):
        begin_timestamp (Union[Unset, None, int]): Begin timestamp Default: 1588723228.
        interval (Union[Unset, None,
            GetChartForTokenV1TokensTokenIdWalletsWalletAddressChartGetInterval]): Interval for
            points. Default: hour Default:
            GetChartForTokenV1TokensTokenIdWalletsWalletAddressChartGetInterval.HOUR.
        period (Union[Unset, None,
            GetChartForTokenV1TokensTokenIdWalletsWalletAddressChartGetPeriod]): Calculate interval
            and begin timestamp
        no_price (Union[Unset, None, bool]): Skip request prices chart

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    return (
        await asyncio_detailed(
            token_id=token_id,
            wallet_address=wallet_address,
            client=client,
            begin_timestamp=begin_timestamp,
            interval=interval,
            period=period,
            no_price=no_price,
        )
    ).parsed

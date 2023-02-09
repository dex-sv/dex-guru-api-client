from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.get_chart_for_token_v2_wallets_wallet_address_tokens_token_id_chart_get_interval import (
    GetChartForTokenV2WalletsWalletAddressTokensTokenIdChartGetInterval,
)
from ...models.get_chart_for_token_v2_wallets_wallet_address_tokens_token_id_chart_get_period import (
    GetChartForTokenV2WalletsWalletAddressTokensTokenIdChartGetPeriod,
)
from ...models.http_validation_error import HTTPValidationError
from ...models.rest_token_chart import RestTokenChart
from ...types import UNSET, Response, Unset


def _get_kwargs(
    wallet_address: str,
    token_id: str,
    *,
    client: Client,
    begin_timestamp: Union[Unset, None, int] = 1588723228,
    interval: Union[
        Unset, None, GetChartForTokenV2WalletsWalletAddressTokensTokenIdChartGetInterval
    ] = GetChartForTokenV2WalletsWalletAddressTokensTokenIdChartGetInterval.HOUR,
    period: Union[Unset, None, GetChartForTokenV2WalletsWalletAddressTokensTokenIdChartGetPeriod] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v2/wallets/{wallet_address}/tokens/{token_id}/chart".format(
        client.base_url, wallet_address=wallet_address, token_id=token_id
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
) -> Optional[Union[HTTPValidationError, RestTokenChart]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RestTokenChart.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, RestTokenChart]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    wallet_address: str,
    token_id: str,
    *,
    client: Client,
    begin_timestamp: Union[Unset, None, int] = 1588723228,
    interval: Union[
        Unset, None, GetChartForTokenV2WalletsWalletAddressTokensTokenIdChartGetInterval
    ] = GetChartForTokenV2WalletsWalletAddressTokensTokenIdChartGetInterval.HOUR,
    period: Union[Unset, None, GetChartForTokenV2WalletsWalletAddressTokensTokenIdChartGetPeriod] = UNSET,
) -> Response[Union[HTTPValidationError, RestTokenChart]]:
    """Get Chart For Token

    Args:
        wallet_address (str):
        token_id (str):
        begin_timestamp (Union[Unset, None, int]): Begin timestamp Default: 1588723228.
        interval (Union[Unset, None,
            GetChartForTokenV2WalletsWalletAddressTokensTokenIdChartGetInterval]): Interval for
            points. Default: hour Default:
            GetChartForTokenV2WalletsWalletAddressTokensTokenIdChartGetInterval.HOUR.
        period (Union[Unset, None,
            GetChartForTokenV2WalletsWalletAddressTokensTokenIdChartGetPeriod]): Calculate interval
            and begin timestamp

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTokenChart]]
    """

    kwargs = _get_kwargs(
        wallet_address=wallet_address,
        token_id=token_id,
        client=client,
        begin_timestamp=begin_timestamp,
        interval=interval,
        period=period,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    wallet_address: str,
    token_id: str,
    *,
    client: Client,
    begin_timestamp: Union[Unset, None, int] = 1588723228,
    interval: Union[
        Unset, None, GetChartForTokenV2WalletsWalletAddressTokensTokenIdChartGetInterval
    ] = GetChartForTokenV2WalletsWalletAddressTokensTokenIdChartGetInterval.HOUR,
    period: Union[Unset, None, GetChartForTokenV2WalletsWalletAddressTokensTokenIdChartGetPeriod] = UNSET,
) -> Optional[Union[HTTPValidationError, RestTokenChart]]:
    """Get Chart For Token

    Args:
        wallet_address (str):
        token_id (str):
        begin_timestamp (Union[Unset, None, int]): Begin timestamp Default: 1588723228.
        interval (Union[Unset, None,
            GetChartForTokenV2WalletsWalletAddressTokensTokenIdChartGetInterval]): Interval for
            points. Default: hour Default:
            GetChartForTokenV2WalletsWalletAddressTokensTokenIdChartGetInterval.HOUR.
        period (Union[Unset, None,
            GetChartForTokenV2WalletsWalletAddressTokensTokenIdChartGetPeriod]): Calculate interval
            and begin timestamp

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTokenChart]]
    """

    return sync_detailed(
        wallet_address=wallet_address,
        token_id=token_id,
        client=client,
        begin_timestamp=begin_timestamp,
        interval=interval,
        period=period,
    ).parsed


async def asyncio_detailed(
    wallet_address: str,
    token_id: str,
    *,
    client: Client,
    begin_timestamp: Union[Unset, None, int] = 1588723228,
    interval: Union[
        Unset, None, GetChartForTokenV2WalletsWalletAddressTokensTokenIdChartGetInterval
    ] = GetChartForTokenV2WalletsWalletAddressTokensTokenIdChartGetInterval.HOUR,
    period: Union[Unset, None, GetChartForTokenV2WalletsWalletAddressTokensTokenIdChartGetPeriod] = UNSET,
) -> Response[Union[HTTPValidationError, RestTokenChart]]:
    """Get Chart For Token

    Args:
        wallet_address (str):
        token_id (str):
        begin_timestamp (Union[Unset, None, int]): Begin timestamp Default: 1588723228.
        interval (Union[Unset, None,
            GetChartForTokenV2WalletsWalletAddressTokensTokenIdChartGetInterval]): Interval for
            points. Default: hour Default:
            GetChartForTokenV2WalletsWalletAddressTokensTokenIdChartGetInterval.HOUR.
        period (Union[Unset, None,
            GetChartForTokenV2WalletsWalletAddressTokensTokenIdChartGetPeriod]): Calculate interval
            and begin timestamp

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTokenChart]]
    """

    kwargs = _get_kwargs(
        wallet_address=wallet_address,
        token_id=token_id,
        client=client,
        begin_timestamp=begin_timestamp,
        interval=interval,
        period=period,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    wallet_address: str,
    token_id: str,
    *,
    client: Client,
    begin_timestamp: Union[Unset, None, int] = 1588723228,
    interval: Union[
        Unset, None, GetChartForTokenV2WalletsWalletAddressTokensTokenIdChartGetInterval
    ] = GetChartForTokenV2WalletsWalletAddressTokensTokenIdChartGetInterval.HOUR,
    period: Union[Unset, None, GetChartForTokenV2WalletsWalletAddressTokensTokenIdChartGetPeriod] = UNSET,
) -> Optional[Union[HTTPValidationError, RestTokenChart]]:
    """Get Chart For Token

    Args:
        wallet_address (str):
        token_id (str):
        begin_timestamp (Union[Unset, None, int]): Begin timestamp Default: 1588723228.
        interval (Union[Unset, None,
            GetChartForTokenV2WalletsWalletAddressTokensTokenIdChartGetInterval]): Interval for
            points. Default: hour Default:
            GetChartForTokenV2WalletsWalletAddressTokensTokenIdChartGetInterval.HOUR.
        period (Union[Unset, None,
            GetChartForTokenV2WalletsWalletAddressTokensTokenIdChartGetPeriod]): Calculate interval
            and begin timestamp

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTokenChart]]
    """

    return (
        await asyncio_detailed(
            wallet_address=wallet_address,
            token_id=token_id,
            client=client,
            begin_timestamp=begin_timestamp,
            interval=interval,
            period=period,
        )
    ).parsed

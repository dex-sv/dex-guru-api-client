from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.http_validation_error import HTTPValidationError
from ...models.rest_holders_providing_liquidity import RestHoldersProvidingLiquidity
from ...models.token_liquidity_holders_v2_tokens_token_id_liquidity_holders_get_interval import (
    TokenLiquidityHoldersV2TokensTokenIdLiquidityHoldersGetInterval,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    token_id: str,
    *,
    client: Client,
    begin_timestamp: Union[Unset, None, int] = 1588723228,
    interval: Union[
        Unset, None, TokenLiquidityHoldersV2TokensTokenIdLiquidityHoldersGetInterval
    ] = TokenLiquidityHoldersV2TokensTokenIdLiquidityHoldersGetInterval.DAY,
) -> Dict[str, Any]:
    url = "{}/v2/tokens/{token_id}/liquidity_holders".format(client.base_url, token_id=token_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["begin_timestamp"] = begin_timestamp

    json_interval: Union[Unset, None, str] = UNSET
    if not isinstance(interval, Unset):
        json_interval = interval.value if interval else None

    params["interval"] = json_interval

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
) -> Optional[Union[HTTPValidationError, RestHoldersProvidingLiquidity]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RestHoldersProvidingLiquidity.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, RestHoldersProvidingLiquidity]]:
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
    begin_timestamp: Union[Unset, None, int] = 1588723228,
    interval: Union[
        Unset, None, TokenLiquidityHoldersV2TokensTokenIdLiquidityHoldersGetInterval
    ] = TokenLiquidityHoldersV2TokensTokenIdLiquidityHoldersGetInterval.DAY,
) -> Response[Union[HTTPValidationError, RestHoldersProvidingLiquidity]]:
    """Token Liquidity Holders

    Args:
        token_id (str):
        begin_timestamp (Union[Unset, None, int]): Begin timestamp Default: 1588723228.
        interval (Union[Unset, None,
            TokenLiquidityHoldersV2TokensTokenIdLiquidityHoldersGetInterval]): Interval for points.
            Default: hour Default:
            TokenLiquidityHoldersV2TokensTokenIdLiquidityHoldersGetInterval.DAY.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestHoldersProvidingLiquidity]]
    """

    kwargs = _get_kwargs(
        token_id=token_id,
        client=client,
        begin_timestamp=begin_timestamp,
        interval=interval,
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
    begin_timestamp: Union[Unset, None, int] = 1588723228,
    interval: Union[
        Unset, None, TokenLiquidityHoldersV2TokensTokenIdLiquidityHoldersGetInterval
    ] = TokenLiquidityHoldersV2TokensTokenIdLiquidityHoldersGetInterval.DAY,
) -> Optional[Union[HTTPValidationError, RestHoldersProvidingLiquidity]]:
    """Token Liquidity Holders

    Args:
        token_id (str):
        begin_timestamp (Union[Unset, None, int]): Begin timestamp Default: 1588723228.
        interval (Union[Unset, None,
            TokenLiquidityHoldersV2TokensTokenIdLiquidityHoldersGetInterval]): Interval for points.
            Default: hour Default:
            TokenLiquidityHoldersV2TokensTokenIdLiquidityHoldersGetInterval.DAY.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestHoldersProvidingLiquidity]]
    """

    return sync_detailed(
        token_id=token_id,
        client=client,
        begin_timestamp=begin_timestamp,
        interval=interval,
    ).parsed


async def asyncio_detailed(
    token_id: str,
    *,
    client: Client,
    begin_timestamp: Union[Unset, None, int] = 1588723228,
    interval: Union[
        Unset, None, TokenLiquidityHoldersV2TokensTokenIdLiquidityHoldersGetInterval
    ] = TokenLiquidityHoldersV2TokensTokenIdLiquidityHoldersGetInterval.DAY,
) -> Response[Union[HTTPValidationError, RestHoldersProvidingLiquidity]]:
    """Token Liquidity Holders

    Args:
        token_id (str):
        begin_timestamp (Union[Unset, None, int]): Begin timestamp Default: 1588723228.
        interval (Union[Unset, None,
            TokenLiquidityHoldersV2TokensTokenIdLiquidityHoldersGetInterval]): Interval for points.
            Default: hour Default:
            TokenLiquidityHoldersV2TokensTokenIdLiquidityHoldersGetInterval.DAY.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestHoldersProvidingLiquidity]]
    """

    kwargs = _get_kwargs(
        token_id=token_id,
        client=client,
        begin_timestamp=begin_timestamp,
        interval=interval,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    token_id: str,
    *,
    client: Client,
    begin_timestamp: Union[Unset, None, int] = 1588723228,
    interval: Union[
        Unset, None, TokenLiquidityHoldersV2TokensTokenIdLiquidityHoldersGetInterval
    ] = TokenLiquidityHoldersV2TokensTokenIdLiquidityHoldersGetInterval.DAY,
) -> Optional[Union[HTTPValidationError, RestHoldersProvidingLiquidity]]:
    """Token Liquidity Holders

    Args:
        token_id (str):
        begin_timestamp (Union[Unset, None, int]): Begin timestamp Default: 1588723228.
        interval (Union[Unset, None,
            TokenLiquidityHoldersV2TokensTokenIdLiquidityHoldersGetInterval]): Interval for points.
            Default: hour Default:
            TokenLiquidityHoldersV2TokensTokenIdLiquidityHoldersGetInterval.DAY.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestHoldersProvidingLiquidity]]
    """

    return (
        await asyncio_detailed(
            token_id=token_id,
            client=client,
            begin_timestamp=begin_timestamp,
            interval=interval,
        )
    ).parsed

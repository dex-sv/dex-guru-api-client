from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.http_validation_error import HTTPValidationError
from ...models.rest_pnl_chart import RestPNLChart
from ...models.token_holders_categories_overtime_v2_tokens_token_id_pnl_wallet_address_chart_get_period import (
    TokenHoldersCategoriesOvertimeV2TokensTokenIdPnlWalletAddressChartGetPeriod,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    token_id: str,
    wallet_address: str,
    *,
    client: Client,
    period: Union[
        Unset, None, TokenHoldersCategoriesOvertimeV2TokensTokenIdPnlWalletAddressChartGetPeriod
    ] = TokenHoldersCategoriesOvertimeV2TokensTokenIdPnlWalletAddressChartGetPeriod.WEEK,
) -> Dict[str, Any]:
    url = "{}/v2/tokens/{token_id}/pnl/{wallet_address}/chart".format(
        client.base_url, token_id=token_id, wallet_address=wallet_address
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[HTTPValidationError, RestPNLChart]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RestPNLChart.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[HTTPValidationError, RestPNLChart]]:
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
    period: Union[
        Unset, None, TokenHoldersCategoriesOvertimeV2TokensTokenIdPnlWalletAddressChartGetPeriod
    ] = TokenHoldersCategoriesOvertimeV2TokensTokenIdPnlWalletAddressChartGetPeriod.WEEK,
) -> Response[Union[HTTPValidationError, RestPNLChart]]:
    """Token Holders Categories Overtime

    Args:
        token_id (str):
        wallet_address (str):
        period (Union[Unset, None,
            TokenHoldersCategoriesOvertimeV2TokensTokenIdPnlWalletAddressChartGetPeriod]): Calculate
            interval and begin timestamp Default:
            TokenHoldersCategoriesOvertimeV2TokensTokenIdPnlWalletAddressChartGetPeriod.WEEK.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestPNLChart]]
    """

    kwargs = _get_kwargs(
        token_id=token_id,
        wallet_address=wallet_address,
        client=client,
        period=period,
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
    period: Union[
        Unset, None, TokenHoldersCategoriesOvertimeV2TokensTokenIdPnlWalletAddressChartGetPeriod
    ] = TokenHoldersCategoriesOvertimeV2TokensTokenIdPnlWalletAddressChartGetPeriod.WEEK,
) -> Optional[Union[HTTPValidationError, RestPNLChart]]:
    """Token Holders Categories Overtime

    Args:
        token_id (str):
        wallet_address (str):
        period (Union[Unset, None,
            TokenHoldersCategoriesOvertimeV2TokensTokenIdPnlWalletAddressChartGetPeriod]): Calculate
            interval and begin timestamp Default:
            TokenHoldersCategoriesOvertimeV2TokensTokenIdPnlWalletAddressChartGetPeriod.WEEK.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestPNLChart]]
    """

    return sync_detailed(
        token_id=token_id,
        wallet_address=wallet_address,
        client=client,
        period=period,
    ).parsed


async def asyncio_detailed(
    token_id: str,
    wallet_address: str,
    *,
    client: Client,
    period: Union[
        Unset, None, TokenHoldersCategoriesOvertimeV2TokensTokenIdPnlWalletAddressChartGetPeriod
    ] = TokenHoldersCategoriesOvertimeV2TokensTokenIdPnlWalletAddressChartGetPeriod.WEEK,
) -> Response[Union[HTTPValidationError, RestPNLChart]]:
    """Token Holders Categories Overtime

    Args:
        token_id (str):
        wallet_address (str):
        period (Union[Unset, None,
            TokenHoldersCategoriesOvertimeV2TokensTokenIdPnlWalletAddressChartGetPeriod]): Calculate
            interval and begin timestamp Default:
            TokenHoldersCategoriesOvertimeV2TokensTokenIdPnlWalletAddressChartGetPeriod.WEEK.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestPNLChart]]
    """

    kwargs = _get_kwargs(
        token_id=token_id,
        wallet_address=wallet_address,
        client=client,
        period=period,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    token_id: str,
    wallet_address: str,
    *,
    client: Client,
    period: Union[
        Unset, None, TokenHoldersCategoriesOvertimeV2TokensTokenIdPnlWalletAddressChartGetPeriod
    ] = TokenHoldersCategoriesOvertimeV2TokensTokenIdPnlWalletAddressChartGetPeriod.WEEK,
) -> Optional[Union[HTTPValidationError, RestPNLChart]]:
    """Token Holders Categories Overtime

    Args:
        token_id (str):
        wallet_address (str):
        period (Union[Unset, None,
            TokenHoldersCategoriesOvertimeV2TokensTokenIdPnlWalletAddressChartGetPeriod]): Calculate
            interval and begin timestamp Default:
            TokenHoldersCategoriesOvertimeV2TokensTokenIdPnlWalletAddressChartGetPeriod.WEEK.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestPNLChart]]
    """

    return (
        await asyncio_detailed(
            token_id=token_id,
            wallet_address=wallet_address,
            client=client,
            period=period,
        )
    ).parsed

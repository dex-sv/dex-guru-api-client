from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.get_list_of_tokens_v2_tokens_list_of_tokens_get_assets import (
    GetListOfTokensV2TokensListOfTokensGetAssets,
)
from ...models.http_validation_error import HTTPValidationError
from ...models.network_choices import NetworkChoices
from ...models.rest_tokens_inventory_v2_market_cap import RestTokensInventoryV2MarketCap
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    network: Union[Unset, None, NetworkChoices] = UNSET,
    assets: Union[
        Unset, None, GetListOfTokensV2TokensListOfTokensGetAssets
    ] = GetListOfTokensV2TokensListOfTokensGetAssets.ALL,
    verified: Union[Unset, None, bool] = False,
    limit: Union[Unset, None, int] = 30,
    offset: Union[Unset, None, int] = 0,
) -> Dict[str, Any]:
    url = "{}/v2/tokens/list_of_tokens".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_network: Union[Unset, None, str] = UNSET
    if not isinstance(network, Unset):
        json_network = network.value if network else None

    params["network"] = json_network

    json_assets: Union[Unset, None, str] = UNSET
    if not isinstance(assets, Unset):
        json_assets = assets.value if assets else None

    params["assets"] = json_assets

    params["verified"] = verified

    params["limit"] = limit

    params["offset"] = offset

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
) -> Optional[Union[HTTPValidationError, RestTokensInventoryV2MarketCap]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RestTokensInventoryV2MarketCap.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, RestTokensInventoryV2MarketCap]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    network: Union[Unset, None, NetworkChoices] = UNSET,
    assets: Union[
        Unset, None, GetListOfTokensV2TokensListOfTokensGetAssets
    ] = GetListOfTokensV2TokensListOfTokensGetAssets.ALL,
    verified: Union[Unset, None, bool] = False,
    limit: Union[Unset, None, int] = 30,
    offset: Union[Unset, None, int] = 0,
) -> Response[Union[HTTPValidationError, RestTokensInventoryV2MarketCap]]:
    """Get List Of Tokens

    Args:
        network (Union[Unset, None, NetworkChoices]): An enumeration.
        assets (Union[Unset, None, GetListOfTokensV2TokensListOfTokensGetAssets]): Data type for
            tab Default: GetListOfTokensV2TokensListOfTokensGetAssets.ALL.
        verified (Union[Unset, None, bool]): Show only verified tokens
        limit (Union[Unset, None, int]): Limit records Default: 30.
        offset (Union[Unset, None, int]): Offset records

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTokensInventoryV2MarketCap]]
    """

    kwargs = _get_kwargs(
        client=client,
        network=network,
        assets=assets,
        verified=verified,
        limit=limit,
        offset=offset,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    network: Union[Unset, None, NetworkChoices] = UNSET,
    assets: Union[
        Unset, None, GetListOfTokensV2TokensListOfTokensGetAssets
    ] = GetListOfTokensV2TokensListOfTokensGetAssets.ALL,
    verified: Union[Unset, None, bool] = False,
    limit: Union[Unset, None, int] = 30,
    offset: Union[Unset, None, int] = 0,
) -> Optional[Union[HTTPValidationError, RestTokensInventoryV2MarketCap]]:
    """Get List Of Tokens

    Args:
        network (Union[Unset, None, NetworkChoices]): An enumeration.
        assets (Union[Unset, None, GetListOfTokensV2TokensListOfTokensGetAssets]): Data type for
            tab Default: GetListOfTokensV2TokensListOfTokensGetAssets.ALL.
        verified (Union[Unset, None, bool]): Show only verified tokens
        limit (Union[Unset, None, int]): Limit records Default: 30.
        offset (Union[Unset, None, int]): Offset records

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTokensInventoryV2MarketCap]]
    """

    return sync_detailed(
        client=client,
        network=network,
        assets=assets,
        verified=verified,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    network: Union[Unset, None, NetworkChoices] = UNSET,
    assets: Union[
        Unset, None, GetListOfTokensV2TokensListOfTokensGetAssets
    ] = GetListOfTokensV2TokensListOfTokensGetAssets.ALL,
    verified: Union[Unset, None, bool] = False,
    limit: Union[Unset, None, int] = 30,
    offset: Union[Unset, None, int] = 0,
) -> Response[Union[HTTPValidationError, RestTokensInventoryV2MarketCap]]:
    """Get List Of Tokens

    Args:
        network (Union[Unset, None, NetworkChoices]): An enumeration.
        assets (Union[Unset, None, GetListOfTokensV2TokensListOfTokensGetAssets]): Data type for
            tab Default: GetListOfTokensV2TokensListOfTokensGetAssets.ALL.
        verified (Union[Unset, None, bool]): Show only verified tokens
        limit (Union[Unset, None, int]): Limit records Default: 30.
        offset (Union[Unset, None, int]): Offset records

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTokensInventoryV2MarketCap]]
    """

    kwargs = _get_kwargs(
        client=client,
        network=network,
        assets=assets,
        verified=verified,
        limit=limit,
        offset=offset,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    network: Union[Unset, None, NetworkChoices] = UNSET,
    assets: Union[
        Unset, None, GetListOfTokensV2TokensListOfTokensGetAssets
    ] = GetListOfTokensV2TokensListOfTokensGetAssets.ALL,
    verified: Union[Unset, None, bool] = False,
    limit: Union[Unset, None, int] = 30,
    offset: Union[Unset, None, int] = 0,
) -> Optional[Union[HTTPValidationError, RestTokensInventoryV2MarketCap]]:
    """Get List Of Tokens

    Args:
        network (Union[Unset, None, NetworkChoices]): An enumeration.
        assets (Union[Unset, None, GetListOfTokensV2TokensListOfTokensGetAssets]): Data type for
            tab Default: GetListOfTokensV2TokensListOfTokensGetAssets.ALL.
        verified (Union[Unset, None, bool]): Show only verified tokens
        limit (Union[Unset, None, int]): Limit records Default: 30.
        offset (Union[Unset, None, int]): Offset records

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTokensInventoryV2MarketCap]]
    """

    return (
        await asyncio_detailed(
            client=client,
            network=network,
            assets=assets,
            verified=verified,
            limit=limit,
            offset=offset,
        )
    ).parsed

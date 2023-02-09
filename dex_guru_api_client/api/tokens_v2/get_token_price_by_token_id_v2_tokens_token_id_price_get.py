from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.amm_choices import AmmChoices
from ...models.http_validation_error import HTTPValidationError
from ...models.network_choices import NetworkChoices
from ...models.rest_token_price import RestTokenPrice
from ...types import UNSET, Response, Unset


def _get_kwargs(
    token_id: str,
    *,
    client: Client,
    amm: Union[Unset, None, AmmChoices] = AmmChoices.ALL,
    network: Union[Unset, None, NetworkChoices] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v2/tokens/{token_id}/price".format(client.base_url, token_id=token_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_amm: Union[Unset, None, str] = UNSET
    if not isinstance(amm, Unset):
        json_amm = amm.value if amm else None

    params["amm"] = json_amm

    json_network: Union[Unset, None, str] = UNSET
    if not isinstance(network, Unset):
        json_network = network.value if network else None

    params["network"] = json_network

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
) -> Optional[Union[HTTPValidationError, RestTokenPrice]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RestTokenPrice.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, RestTokenPrice]]:
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
    amm: Union[Unset, None, AmmChoices] = AmmChoices.ALL,
    network: Union[Unset, None, NetworkChoices] = UNSET,
) -> Response[Union[HTTPValidationError, RestTokenPrice]]:
    """Get Token Price By Token Id

    Args:
        token_id (str):
        amm (Union[Unset, None, AmmChoices]): An enumeration. Default: AmmChoices.ALL.
        network (Union[Unset, None, NetworkChoices]): An enumeration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTokenPrice]]
    """

    kwargs = _get_kwargs(
        token_id=token_id,
        client=client,
        amm=amm,
        network=network,
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
    amm: Union[Unset, None, AmmChoices] = AmmChoices.ALL,
    network: Union[Unset, None, NetworkChoices] = UNSET,
) -> Optional[Union[HTTPValidationError, RestTokenPrice]]:
    """Get Token Price By Token Id

    Args:
        token_id (str):
        amm (Union[Unset, None, AmmChoices]): An enumeration. Default: AmmChoices.ALL.
        network (Union[Unset, None, NetworkChoices]): An enumeration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTokenPrice]]
    """

    return sync_detailed(
        token_id=token_id,
        client=client,
        amm=amm,
        network=network,
    ).parsed


async def asyncio_detailed(
    token_id: str,
    *,
    client: Client,
    amm: Union[Unset, None, AmmChoices] = AmmChoices.ALL,
    network: Union[Unset, None, NetworkChoices] = UNSET,
) -> Response[Union[HTTPValidationError, RestTokenPrice]]:
    """Get Token Price By Token Id

    Args:
        token_id (str):
        amm (Union[Unset, None, AmmChoices]): An enumeration. Default: AmmChoices.ALL.
        network (Union[Unset, None, NetworkChoices]): An enumeration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTokenPrice]]
    """

    kwargs = _get_kwargs(
        token_id=token_id,
        client=client,
        amm=amm,
        network=network,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    token_id: str,
    *,
    client: Client,
    amm: Union[Unset, None, AmmChoices] = AmmChoices.ALL,
    network: Union[Unset, None, NetworkChoices] = UNSET,
) -> Optional[Union[HTTPValidationError, RestTokenPrice]]:
    """Get Token Price By Token Id

    Args:
        token_id (str):
        amm (Union[Unset, None, AmmChoices]): An enumeration. Default: AmmChoices.ALL.
        network (Union[Unset, None, NetworkChoices]): An enumeration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTokenPrice]]
    """

    return (
        await asyncio_detailed(
            token_id=token_id,
            client=client,
            amm=amm,
            network=network,
        )
    ).parsed

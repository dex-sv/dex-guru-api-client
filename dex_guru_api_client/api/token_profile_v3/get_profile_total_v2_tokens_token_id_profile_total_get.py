from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.http_validation_error import HTTPValidationError
from ...models.network_choices import NetworkChoices
from ...types import UNSET, Response, Unset


def _get_kwargs(
    token_id: str,
    *,
    client: Client,
    network: Union[Unset, None, NetworkChoices] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v2/tokens/{token_id}/profile/total".format(client.base_url, token_id=token_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
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
    *,
    client: Client,
    network: Union[Unset, None, NetworkChoices] = UNSET,
) -> Response[Union[Any, HTTPValidationError]]:
    """Get Profile Total

    Args:
        token_id (str):
        network (Union[Unset, None, NetworkChoices]): An enumeration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        token_id=token_id,
        client=client,
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
    network: Union[Unset, None, NetworkChoices] = UNSET,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Get Profile Total

    Args:
        token_id (str):
        network (Union[Unset, None, NetworkChoices]): An enumeration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    return sync_detailed(
        token_id=token_id,
        client=client,
        network=network,
    ).parsed


async def asyncio_detailed(
    token_id: str,
    *,
    client: Client,
    network: Union[Unset, None, NetworkChoices] = UNSET,
) -> Response[Union[Any, HTTPValidationError]]:
    """Get Profile Total

    Args:
        token_id (str):
        network (Union[Unset, None, NetworkChoices]): An enumeration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        token_id=token_id,
        client=client,
        network=network,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    token_id: str,
    *,
    client: Client,
    network: Union[Unset, None, NetworkChoices] = UNSET,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Get Profile Total

    Args:
        token_id (str):
        network (Union[Unset, None, NetworkChoices]): An enumeration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    return (
        await asyncio_detailed(
            token_id=token_id,
            client=client,
            network=network,
        )
    ).parsed

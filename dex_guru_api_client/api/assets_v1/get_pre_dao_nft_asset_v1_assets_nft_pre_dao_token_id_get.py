from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.http_validation_error import HTTPValidationError
from ...models.rest_nft_assets_model import RestNFTAssetsModel
from ...types import Response


def _get_kwargs(
    token_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/v1/assets/nft/pre-dao/{token_id}".format(client.base_url, token_id=token_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[HTTPValidationError, RestNFTAssetsModel]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RestNFTAssetsModel.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, RestNFTAssetsModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    token_id: int,
    *,
    client: Client,
) -> Response[Union[HTTPValidationError, RestNFTAssetsModel]]:
    """Get Pre Dao Nft Asset

    Args:
        token_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestNFTAssetsModel]]
    """

    kwargs = _get_kwargs(
        token_id=token_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    token_id: int,
    *,
    client: Client,
) -> Optional[Union[HTTPValidationError, RestNFTAssetsModel]]:
    """Get Pre Dao Nft Asset

    Args:
        token_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestNFTAssetsModel]]
    """

    return sync_detailed(
        token_id=token_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    token_id: int,
    *,
    client: Client,
) -> Response[Union[HTTPValidationError, RestNFTAssetsModel]]:
    """Get Pre Dao Nft Asset

    Args:
        token_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestNFTAssetsModel]]
    """

    kwargs = _get_kwargs(
        token_id=token_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    token_id: int,
    *,
    client: Client,
) -> Optional[Union[HTTPValidationError, RestNFTAssetsModel]]:
    """Get Pre Dao Nft Asset

    Args:
        token_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestNFTAssetsModel]]
    """

    return (
        await asyncio_detailed(
            token_id=token_id,
            client=client,
        )
    ).parsed

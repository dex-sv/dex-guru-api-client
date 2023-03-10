from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.body_get_tokens_by_params_post_v3_tokens_post import BodyGetTokensByParamsPostV3TokensPost
from ...models.http_validation_error import HTTPValidationError
from ...models.rest_tokens_inventory_v3 import RestTokensInventoryV3
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: BodyGetTokensByParamsPostV3TokensPost,
) -> Dict[str, Any]:
    url = "{}/v3/tokens".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[HTTPValidationError, RestTokensInventoryV3]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RestTokensInventoryV3.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, RestTokensInventoryV3]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: BodyGetTokensByParamsPostV3TokensPost,
) -> Response[Union[HTTPValidationError, RestTokensInventoryV3]]:
    """Get Tokens By Params Post

    Args:
        json_body (BodyGetTokensByParamsPostV3TokensPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTokensInventoryV3]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    json_body: BodyGetTokensByParamsPostV3TokensPost,
) -> Optional[Union[HTTPValidationError, RestTokensInventoryV3]]:
    """Get Tokens By Params Post

    Args:
        json_body (BodyGetTokensByParamsPostV3TokensPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTokensInventoryV3]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: BodyGetTokensByParamsPostV3TokensPost,
) -> Response[Union[HTTPValidationError, RestTokensInventoryV3]]:
    """Get Tokens By Params Post

    Args:
        json_body (BodyGetTokensByParamsPostV3TokensPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTokensInventoryV3]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: BodyGetTokensByParamsPostV3TokensPost,
) -> Optional[Union[HTTPValidationError, RestTokensInventoryV3]]:
    """Get Tokens By Params Post

    Args:
        json_body (BodyGetTokensByParamsPostV3TokensPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTokensInventoryV3]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed

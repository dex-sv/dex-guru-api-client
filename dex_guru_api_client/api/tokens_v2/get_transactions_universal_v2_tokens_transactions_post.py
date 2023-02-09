from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.body_get_transactions_universal_v2_tokens_transactions_post import (
    BodyGetTransactionsUniversalV2TokensTransactionsPost,
)
from ...models.http_validation_error import HTTPValidationError
from ...models.rest_transactions_model import RestTransactionsModel
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: BodyGetTransactionsUniversalV2TokensTransactionsPost,
) -> Dict[str, Any]:
    url = "{}/v2/tokens/transactions".format(client.base_url)

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
) -> Optional[Union[HTTPValidationError, RestTransactionsModel]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RestTransactionsModel.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, RestTransactionsModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: BodyGetTransactionsUniversalV2TokensTransactionsPost,
) -> Response[Union[HTTPValidationError, RestTransactionsModel]]:
    """Get Transactions Universal

    Args:
        json_body (BodyGetTransactionsUniversalV2TokensTransactionsPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTransactionsModel]]
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
    json_body: BodyGetTransactionsUniversalV2TokensTransactionsPost,
) -> Optional[Union[HTTPValidationError, RestTransactionsModel]]:
    """Get Transactions Universal

    Args:
        json_body (BodyGetTransactionsUniversalV2TokensTransactionsPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTransactionsModel]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: BodyGetTransactionsUniversalV2TokensTransactionsPost,
) -> Response[Union[HTTPValidationError, RestTransactionsModel]]:
    """Get Transactions Universal

    Args:
        json_body (BodyGetTransactionsUniversalV2TokensTransactionsPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTransactionsModel]]
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
    json_body: BodyGetTransactionsUniversalV2TokensTransactionsPost,
) -> Optional[Union[HTTPValidationError, RestTransactionsModel]]:
    """Get Transactions Universal

    Args:
        json_body (BodyGetTransactionsUniversalV2TokensTransactionsPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTransactionsModel]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed

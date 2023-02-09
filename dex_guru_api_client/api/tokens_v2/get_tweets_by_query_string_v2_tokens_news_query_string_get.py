from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.http_validation_error import HTTPValidationError
from ...models.rest_token_news import RestTokenNews
from ...types import Response


def _get_kwargs(
    query_string: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/v2/tokens/news/{query_string}".format(client.base_url, query_string=query_string)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[HTTPValidationError, RestTokenNews]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RestTokenNews.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[HTTPValidationError, RestTokenNews]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    query_string: str,
    *,
    client: Client,
) -> Response[Union[HTTPValidationError, RestTokenNews]]:
    """Get Tweets By Query String

    Args:
        query_string (str): Comma separated coin names as hashes. Example: $ETC

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTokenNews]]
    """

    kwargs = _get_kwargs(
        query_string=query_string,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    query_string: str,
    *,
    client: Client,
) -> Optional[Union[HTTPValidationError, RestTokenNews]]:
    """Get Tweets By Query String

    Args:
        query_string (str): Comma separated coin names as hashes. Example: $ETC

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTokenNews]]
    """

    return sync_detailed(
        query_string=query_string,
        client=client,
    ).parsed


async def asyncio_detailed(
    query_string: str,
    *,
    client: Client,
) -> Response[Union[HTTPValidationError, RestTokenNews]]:
    """Get Tweets By Query String

    Args:
        query_string (str): Comma separated coin names as hashes. Example: $ETC

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTokenNews]]
    """

    kwargs = _get_kwargs(
        query_string=query_string,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    query_string: str,
    *,
    client: Client,
) -> Optional[Union[HTTPValidationError, RestTokenNews]]:
    """Get Tweets By Query String

    Args:
        query_string (str): Comma separated coin names as hashes. Example: $ETC

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTokenNews]]
    """

    return (
        await asyncio_detailed(
            query_string=query_string,
            client=client,
        )
    ).parsed

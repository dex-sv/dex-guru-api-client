from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.http_validation_error import HTTPValidationError
from ...models.rest_token_tags_model import RestTokenTagsModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    tag_ids: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 20,
    offset: Union[Unset, None, int] = 0,
) -> Dict[str, Any]:
    url = "{}/v1/token_tags/tags".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["tag_ids"] = tag_ids

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
) -> Optional[Union[HTTPValidationError, RestTokenTagsModel]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RestTokenTagsModel.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, RestTokenTagsModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    tag_ids: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 20,
    offset: Union[Unset, None, int] = 0,
) -> Response[Union[HTTPValidationError, RestTokenTagsModel]]:
    """Get All Token Tags

    Args:
        tag_ids (Union[Unset, None, str]): Comma separated list of tag ids. If it is null, get all
            tags with limit offset
        limit (Union[Unset, None, int]): Count the number of results returned. Default: 20.
        offset (Union[Unset, None, int]): Offset the number of results returned.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTokenTagsModel]]
    """

    kwargs = _get_kwargs(
        client=client,
        tag_ids=tag_ids,
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
    tag_ids: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 20,
    offset: Union[Unset, None, int] = 0,
) -> Optional[Union[HTTPValidationError, RestTokenTagsModel]]:
    """Get All Token Tags

    Args:
        tag_ids (Union[Unset, None, str]): Comma separated list of tag ids. If it is null, get all
            tags with limit offset
        limit (Union[Unset, None, int]): Count the number of results returned. Default: 20.
        offset (Union[Unset, None, int]): Offset the number of results returned.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTokenTagsModel]]
    """

    return sync_detailed(
        client=client,
        tag_ids=tag_ids,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    tag_ids: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 20,
    offset: Union[Unset, None, int] = 0,
) -> Response[Union[HTTPValidationError, RestTokenTagsModel]]:
    """Get All Token Tags

    Args:
        tag_ids (Union[Unset, None, str]): Comma separated list of tag ids. If it is null, get all
            tags with limit offset
        limit (Union[Unset, None, int]): Count the number of results returned. Default: 20.
        offset (Union[Unset, None, int]): Offset the number of results returned.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTokenTagsModel]]
    """

    kwargs = _get_kwargs(
        client=client,
        tag_ids=tag_ids,
        limit=limit,
        offset=offset,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    tag_ids: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 20,
    offset: Union[Unset, None, int] = 0,
) -> Optional[Union[HTTPValidationError, RestTokenTagsModel]]:
    """Get All Token Tags

    Args:
        tag_ids (Union[Unset, None, str]): Comma separated list of tag ids. If it is null, get all
            tags with limit offset
        limit (Union[Unset, None, int]): Count the number of results returned. Default: 20.
        offset (Union[Unset, None, int]): Offset the number of results returned.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTokenTagsModel]]
    """

    return (
        await asyncio_detailed(
            client=client,
            tag_ids=tag_ids,
            limit=limit,
            offset=offset,
        )
    ).parsed

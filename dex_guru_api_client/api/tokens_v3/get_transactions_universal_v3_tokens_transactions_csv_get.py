from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    params: File,
    output_format: Union[Unset, None, str] = "csv",
    limit: Union[Unset, None, int] = 5000,
) -> Dict[str, Any]:
    url = "{}/v3/tokens/transactions/csv".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_params = params.to_tuple()

    params["params"] = json_params

    params["output_format"] = output_format

    params["limit"] = limit

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
    *,
    client: Client,
    params: File,
    output_format: Union[Unset, None, str] = "csv",
    limit: Union[Unset, None, int] = 5000,
) -> Response[Union[Any, HTTPValidationError]]:
    """Get Transactions Universal

    Args:
        params (File):
        output_format (Union[Unset, None, str]):  Default: 'csv'.
        limit (Union[Unset, None, int]):  Default: 5000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        client=client,
        params=params,
        output_format=output_format,
        limit=limit,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    params: File,
    output_format: Union[Unset, None, str] = "csv",
    limit: Union[Unset, None, int] = 5000,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Get Transactions Universal

    Args:
        params (File):
        output_format (Union[Unset, None, str]):  Default: 'csv'.
        limit (Union[Unset, None, int]):  Default: 5000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    return sync_detailed(
        client=client,
        params=params,
        output_format=output_format,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    params: File,
    output_format: Union[Unset, None, str] = "csv",
    limit: Union[Unset, None, int] = 5000,
) -> Response[Union[Any, HTTPValidationError]]:
    """Get Transactions Universal

    Args:
        params (File):
        output_format (Union[Unset, None, str]):  Default: 'csv'.
        limit (Union[Unset, None, int]):  Default: 5000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        client=client,
        params=params,
        output_format=output_format,
        limit=limit,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    params: File,
    output_format: Union[Unset, None, str] = "csv",
    limit: Union[Unset, None, int] = 5000,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Get Transactions Universal

    Args:
        params (File):
        output_format (Union[Unset, None, str]):  Default: 'csv'.
        limit (Union[Unset, None, int]):  Default: 5000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    return (
        await asyncio_detailed(
            client=client,
            params=params,
            output_format=output_format,
            limit=limit,
        )
    ).parsed

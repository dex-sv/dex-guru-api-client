from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.amm_choices import AmmChoices
from ...models.http_validation_error import HTTPValidationError
from ...models.order_choices import OrderChoices
from ...models.rest_tokens_inventory_v2 import RestTokensInventoryV2
from ...models.sort_choices import SortChoices
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    amm: Union[Unset, None, AmmChoices] = UNSET,
    sort_by: Union[Unset, None, SortChoices] = SortChoices.LIQUIDITYUSD,
    order: Union[Unset, None, OrderChoices] = OrderChoices.ASC,
    range_field: Union[Unset, None, str] = UNSET,
    range_gt: Union[Unset, None, float] = UNSET,
    range_lt: Union[Unset, None, float] = UNSET,
    range_gte: Union[Unset, None, float] = UNSET,
    range_lte: Union[Unset, None, float] = UNSET,
    field: Union[Unset, None, str] = UNSET,
    value: Union[Unset, None, str] = UNSET,
    ids: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 100,
    offset: Union[Unset, None, int] = 0,
    network: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v2/tokens".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_amm: Union[Unset, None, str] = UNSET
    if not isinstance(amm, Unset):
        json_amm = amm.value if amm else None

    params["amm"] = json_amm

    json_sort_by: Union[Unset, None, str] = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value if sort_by else None

    params["sort_by"] = json_sort_by

    json_order: Union[Unset, None, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value if order else None

    params["order"] = json_order

    params["range_field"] = range_field

    params["range_gt"] = range_gt

    params["range_lt"] = range_lt

    params["range_gte"] = range_gte

    params["range_lte"] = range_lte

    params["field"] = field

    params["value"] = value

    params["ids"] = ids

    params["limit"] = limit

    params["offset"] = offset

    params["network"] = network

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
) -> Optional[Union[HTTPValidationError, RestTokensInventoryV2]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RestTokensInventoryV2.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, RestTokensInventoryV2]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    amm: Union[Unset, None, AmmChoices] = UNSET,
    sort_by: Union[Unset, None, SortChoices] = SortChoices.LIQUIDITYUSD,
    order: Union[Unset, None, OrderChoices] = OrderChoices.ASC,
    range_field: Union[Unset, None, str] = UNSET,
    range_gt: Union[Unset, None, float] = UNSET,
    range_lt: Union[Unset, None, float] = UNSET,
    range_gte: Union[Unset, None, float] = UNSET,
    range_lte: Union[Unset, None, float] = UNSET,
    field: Union[Unset, None, str] = UNSET,
    value: Union[Unset, None, str] = UNSET,
    ids: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 100,
    offset: Union[Unset, None, int] = 0,
    network: Union[Unset, None, str] = UNSET,
) -> Response[Union[HTTPValidationError, RestTokensInventoryV2]]:
    """Get Tokens By Params

    Args:
        amm (Union[Unset, None, AmmChoices]): An enumeration.
        sort_by (Union[Unset, None, SortChoices]): An enumeration. Default:
            SortChoices.LIQUIDITYUSD.
        order (Union[Unset, None, OrderChoices]): An enumeration. Default: OrderChoices.ASC.
        range_field (Union[Unset, None, str]): Range field
        range_gt (Union[Unset, None, float]): Range gt
        range_lt (Union[Unset, None, float]): Range lt
        range_gte (Union[Unset, None, float]): Range gte
        range_lte (Union[Unset, None, float]): Range lte
        field (Union[Unset, None, str]): Field
        value (Union[Unset, None, str]): Value
        ids (Union[Unset, None, str]): Comma separated list of ids
        limit (Union[Unset, None, int]): Limit records Default: 100.
        offset (Union[Unset, None, int]): Offset records
        network (Union[Unset, None, str]): Comma separated list of any networks:
            eth,optimism,bsc,polygon,fantom,arbitrum,celo,avalanche,gnosis,canto,osmosis,nova

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTokensInventoryV2]]
    """

    kwargs = _get_kwargs(
        client=client,
        amm=amm,
        sort_by=sort_by,
        order=order,
        range_field=range_field,
        range_gt=range_gt,
        range_lt=range_lt,
        range_gte=range_gte,
        range_lte=range_lte,
        field=field,
        value=value,
        ids=ids,
        limit=limit,
        offset=offset,
        network=network,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    amm: Union[Unset, None, AmmChoices] = UNSET,
    sort_by: Union[Unset, None, SortChoices] = SortChoices.LIQUIDITYUSD,
    order: Union[Unset, None, OrderChoices] = OrderChoices.ASC,
    range_field: Union[Unset, None, str] = UNSET,
    range_gt: Union[Unset, None, float] = UNSET,
    range_lt: Union[Unset, None, float] = UNSET,
    range_gte: Union[Unset, None, float] = UNSET,
    range_lte: Union[Unset, None, float] = UNSET,
    field: Union[Unset, None, str] = UNSET,
    value: Union[Unset, None, str] = UNSET,
    ids: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 100,
    offset: Union[Unset, None, int] = 0,
    network: Union[Unset, None, str] = UNSET,
) -> Optional[Union[HTTPValidationError, RestTokensInventoryV2]]:
    """Get Tokens By Params

    Args:
        amm (Union[Unset, None, AmmChoices]): An enumeration.
        sort_by (Union[Unset, None, SortChoices]): An enumeration. Default:
            SortChoices.LIQUIDITYUSD.
        order (Union[Unset, None, OrderChoices]): An enumeration. Default: OrderChoices.ASC.
        range_field (Union[Unset, None, str]): Range field
        range_gt (Union[Unset, None, float]): Range gt
        range_lt (Union[Unset, None, float]): Range lt
        range_gte (Union[Unset, None, float]): Range gte
        range_lte (Union[Unset, None, float]): Range lte
        field (Union[Unset, None, str]): Field
        value (Union[Unset, None, str]): Value
        ids (Union[Unset, None, str]): Comma separated list of ids
        limit (Union[Unset, None, int]): Limit records Default: 100.
        offset (Union[Unset, None, int]): Offset records
        network (Union[Unset, None, str]): Comma separated list of any networks:
            eth,optimism,bsc,polygon,fantom,arbitrum,celo,avalanche,gnosis,canto,osmosis,nova

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTokensInventoryV2]]
    """

    return sync_detailed(
        client=client,
        amm=amm,
        sort_by=sort_by,
        order=order,
        range_field=range_field,
        range_gt=range_gt,
        range_lt=range_lt,
        range_gte=range_gte,
        range_lte=range_lte,
        field=field,
        value=value,
        ids=ids,
        limit=limit,
        offset=offset,
        network=network,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    amm: Union[Unset, None, AmmChoices] = UNSET,
    sort_by: Union[Unset, None, SortChoices] = SortChoices.LIQUIDITYUSD,
    order: Union[Unset, None, OrderChoices] = OrderChoices.ASC,
    range_field: Union[Unset, None, str] = UNSET,
    range_gt: Union[Unset, None, float] = UNSET,
    range_lt: Union[Unset, None, float] = UNSET,
    range_gte: Union[Unset, None, float] = UNSET,
    range_lte: Union[Unset, None, float] = UNSET,
    field: Union[Unset, None, str] = UNSET,
    value: Union[Unset, None, str] = UNSET,
    ids: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 100,
    offset: Union[Unset, None, int] = 0,
    network: Union[Unset, None, str] = UNSET,
) -> Response[Union[HTTPValidationError, RestTokensInventoryV2]]:
    """Get Tokens By Params

    Args:
        amm (Union[Unset, None, AmmChoices]): An enumeration.
        sort_by (Union[Unset, None, SortChoices]): An enumeration. Default:
            SortChoices.LIQUIDITYUSD.
        order (Union[Unset, None, OrderChoices]): An enumeration. Default: OrderChoices.ASC.
        range_field (Union[Unset, None, str]): Range field
        range_gt (Union[Unset, None, float]): Range gt
        range_lt (Union[Unset, None, float]): Range lt
        range_gte (Union[Unset, None, float]): Range gte
        range_lte (Union[Unset, None, float]): Range lte
        field (Union[Unset, None, str]): Field
        value (Union[Unset, None, str]): Value
        ids (Union[Unset, None, str]): Comma separated list of ids
        limit (Union[Unset, None, int]): Limit records Default: 100.
        offset (Union[Unset, None, int]): Offset records
        network (Union[Unset, None, str]): Comma separated list of any networks:
            eth,optimism,bsc,polygon,fantom,arbitrum,celo,avalanche,gnosis,canto,osmosis,nova

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTokensInventoryV2]]
    """

    kwargs = _get_kwargs(
        client=client,
        amm=amm,
        sort_by=sort_by,
        order=order,
        range_field=range_field,
        range_gt=range_gt,
        range_lt=range_lt,
        range_gte=range_gte,
        range_lte=range_lte,
        field=field,
        value=value,
        ids=ids,
        limit=limit,
        offset=offset,
        network=network,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    amm: Union[Unset, None, AmmChoices] = UNSET,
    sort_by: Union[Unset, None, SortChoices] = SortChoices.LIQUIDITYUSD,
    order: Union[Unset, None, OrderChoices] = OrderChoices.ASC,
    range_field: Union[Unset, None, str] = UNSET,
    range_gt: Union[Unset, None, float] = UNSET,
    range_lt: Union[Unset, None, float] = UNSET,
    range_gte: Union[Unset, None, float] = UNSET,
    range_lte: Union[Unset, None, float] = UNSET,
    field: Union[Unset, None, str] = UNSET,
    value: Union[Unset, None, str] = UNSET,
    ids: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 100,
    offset: Union[Unset, None, int] = 0,
    network: Union[Unset, None, str] = UNSET,
) -> Optional[Union[HTTPValidationError, RestTokensInventoryV2]]:
    """Get Tokens By Params

    Args:
        amm (Union[Unset, None, AmmChoices]): An enumeration.
        sort_by (Union[Unset, None, SortChoices]): An enumeration. Default:
            SortChoices.LIQUIDITYUSD.
        order (Union[Unset, None, OrderChoices]): An enumeration. Default: OrderChoices.ASC.
        range_field (Union[Unset, None, str]): Range field
        range_gt (Union[Unset, None, float]): Range gt
        range_lt (Union[Unset, None, float]): Range lt
        range_gte (Union[Unset, None, float]): Range gte
        range_lte (Union[Unset, None, float]): Range lte
        field (Union[Unset, None, str]): Field
        value (Union[Unset, None, str]): Value
        ids (Union[Unset, None, str]): Comma separated list of ids
        limit (Union[Unset, None, int]): Limit records Default: 100.
        offset (Union[Unset, None, int]): Offset records
        network (Union[Unset, None, str]): Comma separated list of any networks:
            eth,optimism,bsc,polygon,fantom,arbitrum,celo,avalanche,gnosis,canto,osmosis,nova

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTokensInventoryV2]]
    """

    return (
        await asyncio_detailed(
            client=client,
            amm=amm,
            sort_by=sort_by,
            order=order,
            range_field=range_field,
            range_gt=range_gt,
            range_lt=range_lt,
            range_gte=range_gte,
            range_lte=range_lte,
            field=field,
            value=value,
            ids=ids,
            limit=limit,
            offset=offset,
            network=network,
        )
    ).parsed

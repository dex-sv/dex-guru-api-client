from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.http_validation_error import HTTPValidationError
from ...models.rest_tokens_history import RestTokensHistory
from ...types import UNSET, Response, Unset


def _get_kwargs(
    token_id: str,
    *,
    client: Client,
    begin_timestamp: Union[Unset, None, int] = UNSET,
    end_timestamp: Union[Unset, None, int] = UNSET,
    amms: Union[Unset, None, str] = [],
) -> Dict[str, Any]:
    url = "{}/v2/tokens/{token_id}/history".format(client.base_url, token_id=token_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["begin_timestamp"] = begin_timestamp

    params["end_timestamp"] = end_timestamp

    params["amms"] = amms

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
) -> Optional[Union[HTTPValidationError, RestTokensHistory]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RestTokensHistory.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, RestTokensHistory]]:
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
    begin_timestamp: Union[Unset, None, int] = UNSET,
    end_timestamp: Union[Unset, None, int] = UNSET,
    amms: Union[Unset, None, str] = [],
) -> Response[Union[HTTPValidationError, RestTokensHistory]]:
    """Get Tokens History

     This copy of v1_tokens router same endpoint

    Args:
        token_id (str): Token ID
        begin_timestamp (Union[Unset, None, int]):
        end_timestamp (Union[Unset, None, int]):
        amms (Union[Unset, None, str]): Comma separated list of any amms: uniswap,all,uniswap_v3,s
            ushiswap,pancakeswap,quickswap,pangolin,traderjoe,ubeswap,spookyswap,spiritswap,kyber,lydi
            a,impossible_finance,cryptocom,firebid_finance,elk_finance,canary,empiredex,yetiswap,bague
            tte,zoodex,jetswap,soulswap,paintswap,hyperswap,morpheusswap,wakaswap,yoshi_exchange,dfyn,
            waultswap,polydex,cafeswap,alitaswap,apeswap,cheeseswap,julswap,babyswap,safeswap,swapr,pa
            ncakeswap_v1,standard,polycat,biswap,yieldfields,unitedfarmers,gravity_finance,shibaswap,s
            heepdex,zipswap,bakeryswap,solidly,curve,1inch,tomb_finance,ellipsis,bancor_v2,dodo,velodr
            ome,knightswap,mdex,meshswap,comethswap,safemoon,fraxswap,stepn,fstswap,pandora,nomiswap,p
            lanet,jfswap,titano,orbitalswap,wigoswap,swapsicle,dystopia,sushiswap_bento,impossible_fin
            ance_v3,saddle,balancer,honeyswap,baoswap,levin_swap,platypus,beethoven,babydogeswap,radio
            shack,CantoSwap,padswap,kyberswap_elastic,dodo_v2,wombat,SwapFish,Verse,WardenSwap,thena,o
            smosis,Arbswap,Slingshot,Forte Default: [].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTokensHistory]]
    """

    kwargs = _get_kwargs(
        token_id=token_id,
        client=client,
        begin_timestamp=begin_timestamp,
        end_timestamp=end_timestamp,
        amms=amms,
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
    begin_timestamp: Union[Unset, None, int] = UNSET,
    end_timestamp: Union[Unset, None, int] = UNSET,
    amms: Union[Unset, None, str] = [],
) -> Optional[Union[HTTPValidationError, RestTokensHistory]]:
    """Get Tokens History

     This copy of v1_tokens router same endpoint

    Args:
        token_id (str): Token ID
        begin_timestamp (Union[Unset, None, int]):
        end_timestamp (Union[Unset, None, int]):
        amms (Union[Unset, None, str]): Comma separated list of any amms: uniswap,all,uniswap_v3,s
            ushiswap,pancakeswap,quickswap,pangolin,traderjoe,ubeswap,spookyswap,spiritswap,kyber,lydi
            a,impossible_finance,cryptocom,firebid_finance,elk_finance,canary,empiredex,yetiswap,bague
            tte,zoodex,jetswap,soulswap,paintswap,hyperswap,morpheusswap,wakaswap,yoshi_exchange,dfyn,
            waultswap,polydex,cafeswap,alitaswap,apeswap,cheeseswap,julswap,babyswap,safeswap,swapr,pa
            ncakeswap_v1,standard,polycat,biswap,yieldfields,unitedfarmers,gravity_finance,shibaswap,s
            heepdex,zipswap,bakeryswap,solidly,curve,1inch,tomb_finance,ellipsis,bancor_v2,dodo,velodr
            ome,knightswap,mdex,meshswap,comethswap,safemoon,fraxswap,stepn,fstswap,pandora,nomiswap,p
            lanet,jfswap,titano,orbitalswap,wigoswap,swapsicle,dystopia,sushiswap_bento,impossible_fin
            ance_v3,saddle,balancer,honeyswap,baoswap,levin_swap,platypus,beethoven,babydogeswap,radio
            shack,CantoSwap,padswap,kyberswap_elastic,dodo_v2,wombat,SwapFish,Verse,WardenSwap,thena,o
            smosis,Arbswap,Slingshot,Forte Default: [].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTokensHistory]]
    """

    return sync_detailed(
        token_id=token_id,
        client=client,
        begin_timestamp=begin_timestamp,
        end_timestamp=end_timestamp,
        amms=amms,
    ).parsed


async def asyncio_detailed(
    token_id: str,
    *,
    client: Client,
    begin_timestamp: Union[Unset, None, int] = UNSET,
    end_timestamp: Union[Unset, None, int] = UNSET,
    amms: Union[Unset, None, str] = [],
) -> Response[Union[HTTPValidationError, RestTokensHistory]]:
    """Get Tokens History

     This copy of v1_tokens router same endpoint

    Args:
        token_id (str): Token ID
        begin_timestamp (Union[Unset, None, int]):
        end_timestamp (Union[Unset, None, int]):
        amms (Union[Unset, None, str]): Comma separated list of any amms: uniswap,all,uniswap_v3,s
            ushiswap,pancakeswap,quickswap,pangolin,traderjoe,ubeswap,spookyswap,spiritswap,kyber,lydi
            a,impossible_finance,cryptocom,firebid_finance,elk_finance,canary,empiredex,yetiswap,bague
            tte,zoodex,jetswap,soulswap,paintswap,hyperswap,morpheusswap,wakaswap,yoshi_exchange,dfyn,
            waultswap,polydex,cafeswap,alitaswap,apeswap,cheeseswap,julswap,babyswap,safeswap,swapr,pa
            ncakeswap_v1,standard,polycat,biswap,yieldfields,unitedfarmers,gravity_finance,shibaswap,s
            heepdex,zipswap,bakeryswap,solidly,curve,1inch,tomb_finance,ellipsis,bancor_v2,dodo,velodr
            ome,knightswap,mdex,meshswap,comethswap,safemoon,fraxswap,stepn,fstswap,pandora,nomiswap,p
            lanet,jfswap,titano,orbitalswap,wigoswap,swapsicle,dystopia,sushiswap_bento,impossible_fin
            ance_v3,saddle,balancer,honeyswap,baoswap,levin_swap,platypus,beethoven,babydogeswap,radio
            shack,CantoSwap,padswap,kyberswap_elastic,dodo_v2,wombat,SwapFish,Verse,WardenSwap,thena,o
            smosis,Arbswap,Slingshot,Forte Default: [].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTokensHistory]]
    """

    kwargs = _get_kwargs(
        token_id=token_id,
        client=client,
        begin_timestamp=begin_timestamp,
        end_timestamp=end_timestamp,
        amms=amms,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    token_id: str,
    *,
    client: Client,
    begin_timestamp: Union[Unset, None, int] = UNSET,
    end_timestamp: Union[Unset, None, int] = UNSET,
    amms: Union[Unset, None, str] = [],
) -> Optional[Union[HTTPValidationError, RestTokensHistory]]:
    """Get Tokens History

     This copy of v1_tokens router same endpoint

    Args:
        token_id (str): Token ID
        begin_timestamp (Union[Unset, None, int]):
        end_timestamp (Union[Unset, None, int]):
        amms (Union[Unset, None, str]): Comma separated list of any amms: uniswap,all,uniswap_v3,s
            ushiswap,pancakeswap,quickswap,pangolin,traderjoe,ubeswap,spookyswap,spiritswap,kyber,lydi
            a,impossible_finance,cryptocom,firebid_finance,elk_finance,canary,empiredex,yetiswap,bague
            tte,zoodex,jetswap,soulswap,paintswap,hyperswap,morpheusswap,wakaswap,yoshi_exchange,dfyn,
            waultswap,polydex,cafeswap,alitaswap,apeswap,cheeseswap,julswap,babyswap,safeswap,swapr,pa
            ncakeswap_v1,standard,polycat,biswap,yieldfields,unitedfarmers,gravity_finance,shibaswap,s
            heepdex,zipswap,bakeryswap,solidly,curve,1inch,tomb_finance,ellipsis,bancor_v2,dodo,velodr
            ome,knightswap,mdex,meshswap,comethswap,safemoon,fraxswap,stepn,fstswap,pandora,nomiswap,p
            lanet,jfswap,titano,orbitalswap,wigoswap,swapsicle,dystopia,sushiswap_bento,impossible_fin
            ance_v3,saddle,balancer,honeyswap,baoswap,levin_swap,platypus,beethoven,babydogeswap,radio
            shack,CantoSwap,padswap,kyberswap_elastic,dodo_v2,wombat,SwapFish,Verse,WardenSwap,thena,o
            smosis,Arbswap,Slingshot,Forte Default: [].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RestTokensHistory]]
    """

    return (
        await asyncio_detailed(
            token_id=token_id,
            client=client,
            begin_timestamp=begin_timestamp,
            end_timestamp=end_timestamp,
            amms=amms,
        )
    ).parsed

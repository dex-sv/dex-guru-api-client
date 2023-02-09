from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_chart_point import RestChartPoint
    from ..models.rest_price_volume import RestPriceVolume
    from ..models.rest_trending_price_moving import RestTrendingPriceMoving


T = TypeVar("T", bound="RestTrending")


@attr.s(auto_attribs=True)
class RestTrending:
    """
    Attributes:
        id (Union[Unset, str]):
        symbol (Union[Unset, str]):
        network (Union[Unset, str]):
        logo_uri (Union[Unset, str]):
        token_address (Union[Unset, str]):
        heavy_traders_cot (Union[Unset, float]):  Default: 50.0.
        current (Union[Unset, RestPriceVolume]):
        trending (Union[Unset, RestTrendingPriceMoving]):
        chart (Union[Unset, List['RestChartPoint']]):
    """

    id: Union[Unset, str] = UNSET
    symbol: Union[Unset, str] = UNSET
    network: Union[Unset, str] = UNSET
    logo_uri: Union[Unset, str] = UNSET
    token_address: Union[Unset, str] = UNSET
    heavy_traders_cot: Union[Unset, float] = 50.0
    current: Union[Unset, "RestPriceVolume"] = UNSET
    trending: Union[Unset, "RestTrendingPriceMoving"] = UNSET
    chart: Union[Unset, List["RestChartPoint"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        symbol = self.symbol
        network = self.network
        logo_uri = self.logo_uri
        token_address = self.token_address
        heavy_traders_cot = self.heavy_traders_cot
        current: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.current, Unset):
            current = self.current.to_dict()

        trending: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.trending, Unset):
            trending = self.trending.to_dict()

        chart: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.chart, Unset):
            chart = []
            for chart_item_data in self.chart:
                chart_item = chart_item_data.to_dict()

                chart.append(chart_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if network is not UNSET:
            field_dict["network"] = network
        if logo_uri is not UNSET:
            field_dict["logoURI"] = logo_uri
        if token_address is not UNSET:
            field_dict["tokenAddress"] = token_address
        if heavy_traders_cot is not UNSET:
            field_dict["heavyTradersCOT"] = heavy_traders_cot
        if current is not UNSET:
            field_dict["current"] = current
        if trending is not UNSET:
            field_dict["trending"] = trending
        if chart is not UNSET:
            field_dict["chart"] = chart

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.rest_chart_point import RestChartPoint
        from ..models.rest_price_volume import RestPriceVolume
        from ..models.rest_trending_price_moving import RestTrendingPriceMoving

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        symbol = d.pop("symbol", UNSET)

        network = d.pop("network", UNSET)

        logo_uri = d.pop("logoURI", UNSET)

        token_address = d.pop("tokenAddress", UNSET)

        heavy_traders_cot = d.pop("heavyTradersCOT", UNSET)

        _current = d.pop("current", UNSET)
        current: Union[Unset, RestPriceVolume]
        if isinstance(_current, Unset):
            current = UNSET
        else:
            current = RestPriceVolume.from_dict(_current)

        _trending = d.pop("trending", UNSET)
        trending: Union[Unset, RestTrendingPriceMoving]
        if isinstance(_trending, Unset):
            trending = UNSET
        else:
            trending = RestTrendingPriceMoving.from_dict(_trending)

        chart = []
        _chart = d.pop("chart", UNSET)
        for chart_item_data in _chart or []:
            chart_item = RestChartPoint.from_dict(chart_item_data)

            chart.append(chart_item)

        rest_trending = cls(
            id=id,
            symbol=symbol,
            network=network,
            logo_uri=logo_uri,
            token_address=token_address,
            heavy_traders_cot=heavy_traders_cot,
            current=current,
            trending=trending,
            chart=chart,
        )

        rest_trending.additional_properties = d
        return rest_trending

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

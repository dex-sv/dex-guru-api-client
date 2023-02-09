from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="RestPNLChartItem")


@attr.s(auto_attribs=True)
class RestPNLChartItem:
    """
    Attributes:
        timestamp (int):
        realized (float):
        unrealized (float):
        balance (float):
    """

    timestamp: int
    realized: float
    unrealized: float
    balance: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp = self.timestamp
        realized = self.realized
        unrealized = self.unrealized
        balance = self.balance

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "realized": realized,
                "unrealized": unrealized,
                "balance": balance,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        timestamp = d.pop("timestamp")

        realized = d.pop("realized")

        unrealized = d.pop("unrealized")

        balance = d.pop("balance")

        rest_pnl_chart_item = cls(
            timestamp=timestamp,
            realized=realized,
            unrealized=unrealized,
            balance=balance,
        )

        rest_pnl_chart_item.additional_properties = d
        return rest_pnl_chart_item

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

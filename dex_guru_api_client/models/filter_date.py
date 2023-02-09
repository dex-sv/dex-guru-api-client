import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="FilterDate")


@attr.s(auto_attribs=True)
class FilterDate:
    """You can pass YYYY-MM-DD or YYYY-MM-DDTHH:MM[:SS] or timestamp

    Attributes:
        start_date (Union[Unset, datetime.date, datetime.datetime, str]):
        end_date (Union[Unset, datetime.date, datetime.datetime, str]):
    """

    start_date: Union[Unset, datetime.date, datetime.datetime, str] = UNSET
    end_date: Union[Unset, datetime.date, datetime.datetime, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start_date: Union[Unset, str]
        if isinstance(self.start_date, Unset):
            start_date = UNSET

        elif isinstance(self.start_date, datetime.datetime):
            start_date = UNSET
            if not isinstance(self.start_date, Unset):
                start_date = self.start_date.isoformat()

        elif isinstance(self.start_date, datetime.date):
            start_date = UNSET
            if not isinstance(self.start_date, Unset):
                start_date = self.start_date.isoformat()

        else:
            start_date = self.start_date

        end_date: Union[Unset, str]
        if isinstance(self.end_date, Unset):
            end_date = UNSET

        elif isinstance(self.end_date, datetime.datetime):
            end_date = UNSET
            if not isinstance(self.end_date, Unset):
                end_date = self.end_date.isoformat()

        elif isinstance(self.end_date, datetime.date):
            end_date = UNSET
            if not isinstance(self.end_date, Unset):
                end_date = self.end_date.isoformat()

        else:
            end_date = self.end_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_start_date(data: object) -> Union[Unset, datetime.date, datetime.datetime, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _start_date_type_0 = data
                start_date_type_0: Union[Unset, datetime.datetime]
                if isinstance(_start_date_type_0, Unset):
                    start_date_type_0 = UNSET
                else:
                    start_date_type_0 = isoparse(_start_date_type_0)

                return start_date_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _start_date_type_1 = data
                start_date_type_1: Union[Unset, datetime.date]
                if isinstance(_start_date_type_1, Unset):
                    start_date_type_1 = UNSET
                else:
                    start_date_type_1 = isoparse(_start_date_type_1).date()

                return start_date_type_1
            except:  # noqa: E722
                pass
            return cast(Union[Unset, datetime.date, datetime.datetime, str], data)

        start_date = _parse_start_date(d.pop("start_date", UNSET))

        def _parse_end_date(data: object) -> Union[Unset, datetime.date, datetime.datetime, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _end_date_type_0 = data
                end_date_type_0: Union[Unset, datetime.datetime]
                if isinstance(_end_date_type_0, Unset):
                    end_date_type_0 = UNSET
                else:
                    end_date_type_0 = isoparse(_end_date_type_0)

                return end_date_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _end_date_type_1 = data
                end_date_type_1: Union[Unset, datetime.date]
                if isinstance(_end_date_type_1, Unset):
                    end_date_type_1 = UNSET
                else:
                    end_date_type_1 = isoparse(_end_date_type_1).date()

                return end_date_type_1
            except:  # noqa: E722
                pass
            return cast(Union[Unset, datetime.date, datetime.datetime, str], data)

        end_date = _parse_end_date(d.pop("end_date", UNSET))

        filter_date = cls(
            start_date=start_date,
            end_date=end_date,
        )

        filter_date.additional_properties = d
        return filter_date

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

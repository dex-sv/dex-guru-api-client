from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.rest_liq_by_categories_elephant import RestLiqByCategoriesElephant
    from ..models.rest_liq_by_categories_other import RestLiqByCategoriesOther
    from ..models.rest_liq_by_categories_rooster import RestLiqByCategoriesRooster
    from ..models.rest_liq_by_categories_tiger import RestLiqByCategoriesTiger


T = TypeVar("T", bound="RestLiqByCategories")


@attr.s(auto_attribs=True)
class RestLiqByCategories:
    """
    Attributes:
        timestamp (int):
        other (RestLiqByCategoriesOther):
        rooster (RestLiqByCategoriesRooster):
        elephant (RestLiqByCategoriesElephant):
        tiger (RestLiqByCategoriesTiger):
    """

    timestamp: int
    other: "RestLiqByCategoriesOther"
    rooster: "RestLiqByCategoriesRooster"
    elephant: "RestLiqByCategoriesElephant"
    tiger: "RestLiqByCategoriesTiger"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp = self.timestamp
        other = self.other.to_dict()

        rooster = self.rooster.to_dict()

        elephant = self.elephant.to_dict()

        tiger = self.tiger.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "Other": other,
                "Rooster": rooster,
                "Elephant": elephant,
                "Tiger": tiger,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.rest_liq_by_categories_elephant import RestLiqByCategoriesElephant
        from ..models.rest_liq_by_categories_other import RestLiqByCategoriesOther
        from ..models.rest_liq_by_categories_rooster import RestLiqByCategoriesRooster
        from ..models.rest_liq_by_categories_tiger import RestLiqByCategoriesTiger

        d = src_dict.copy()
        timestamp = d.pop("timestamp")

        other = RestLiqByCategoriesOther.from_dict(d.pop("Other"))

        rooster = RestLiqByCategoriesRooster.from_dict(d.pop("Rooster"))

        elephant = RestLiqByCategoriesElephant.from_dict(d.pop("Elephant"))

        tiger = RestLiqByCategoriesTiger.from_dict(d.pop("Tiger"))

        rest_liq_by_categories = cls(
            timestamp=timestamp,
            other=other,
            rooster=rooster,
            elephant=elephant,
            tiger=tiger,
        )

        rest_liq_by_categories.additional_properties = d
        return rest_liq_by_categories

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

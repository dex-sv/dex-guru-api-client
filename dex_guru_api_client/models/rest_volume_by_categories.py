from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.rest_volume_by_categories_bot import RestVolumeByCategoriesBot
    from ..models.rest_volume_by_categories_casual import RestVolumeByCategoriesCasual
    from ..models.rest_volume_by_categories_heavy import RestVolumeByCategoriesHeavy
    from ..models.rest_volume_by_categories_medium import RestVolumeByCategoriesMedium
    from ..models.rest_volume_by_categories_noob import RestVolumeByCategoriesNoob


T = TypeVar("T", bound="RestVolumeByCategories")


@attr.s(auto_attribs=True)
class RestVolumeByCategories:
    """
    Attributes:
        timestamp (int):
        casual (RestVolumeByCategoriesCasual):
        medium (RestVolumeByCategoriesMedium):
        heavy (RestVolumeByCategoriesHeavy):
        bot (RestVolumeByCategoriesBot):
        noob (RestVolumeByCategoriesNoob):
    """

    timestamp: int
    casual: "RestVolumeByCategoriesCasual"
    medium: "RestVolumeByCategoriesMedium"
    heavy: "RestVolumeByCategoriesHeavy"
    bot: "RestVolumeByCategoriesBot"
    noob: "RestVolumeByCategoriesNoob"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp = self.timestamp
        casual = self.casual.to_dict()

        medium = self.medium.to_dict()

        heavy = self.heavy.to_dict()

        bot = self.bot.to_dict()

        noob = self.noob.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "Casual": casual,
                "Medium": medium,
                "Heavy": heavy,
                "Bot": bot,
                "Noob": noob,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.rest_volume_by_categories_bot import RestVolumeByCategoriesBot
        from ..models.rest_volume_by_categories_casual import RestVolumeByCategoriesCasual
        from ..models.rest_volume_by_categories_heavy import RestVolumeByCategoriesHeavy
        from ..models.rest_volume_by_categories_medium import RestVolumeByCategoriesMedium
        from ..models.rest_volume_by_categories_noob import RestVolumeByCategoriesNoob

        d = src_dict.copy()
        timestamp = d.pop("timestamp")

        casual = RestVolumeByCategoriesCasual.from_dict(d.pop("Casual"))

        medium = RestVolumeByCategoriesMedium.from_dict(d.pop("Medium"))

        heavy = RestVolumeByCategoriesHeavy.from_dict(d.pop("Heavy"))

        bot = RestVolumeByCategoriesBot.from_dict(d.pop("Bot"))

        noob = RestVolumeByCategoriesNoob.from_dict(d.pop("Noob"))

        rest_volume_by_categories = cls(
            timestamp=timestamp,
            casual=casual,
            medium=medium,
            heavy=heavy,
            bot=bot,
            noob=noob,
        )

        rest_volume_by_categories.additional_properties = d
        return rest_volume_by_categories

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

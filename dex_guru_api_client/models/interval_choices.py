from enum import IntEnum


class IntervalChoices(IntEnum):
    VALUE_60 = 60
    VALUE_300 = 300
    VALUE_600 = 600
    VALUE_1800 = 1800
    VALUE_3600 = 3600
    VALUE_14400 = 14400
    VALUE_43200 = 43200
    VALUE_86400 = 86400
    VALUE_604800 = 604800

    def __str__(self) -> str:
        return str(self.value)

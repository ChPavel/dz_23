from marshmallow import fields, Schema, validates_schema, ValidationError
from typing import Any, Iterable

VALID_CMD_PARAMS: Iterable[str] = (
    'filter',
    'sort',
    'map',
    'unique',
    'limit',
    'regex'
)


class RequestParams(Schema):
    """
    Класс, определяющий модель, с возможностью валидации данных.
    """
    cmd = fields.Str(required=True)
    value = fields.Str(required=True)

    @validates_schema
    def validate_cmd_params(self, values: dict[str, str], *args: Any, **kwargs: Any) -> dict[str, str]:
        if values['cmd'] not in VALID_CMD_PARAMS:
            raise ValidationError('"cmd" contains invalid value')

        return values


class BatchRequestParams(Schema):
    """
    Класс, позволяющий расширить число параметров в модели.
    """
    queries = fields.Nested(RequestParams, many=True)

from marshmallow import fields, Schema, validates_schema, ValidationError


VALID_CMD_PARAMS = (
    'filter',
    'sort',
    'map',
    'unique',
    'limit'
)


class RequestParams(Schema):
    """
    Класс, определяющий модель, с возможностью валидации данных.
    """
    cmd = fields.Str(required=True)
    value = fields.Str(required=True)

    @validates_schema
    def validate_cmd_params(self, values, *args, **kwargs):
        if values['cmd'] not in VALID_CMD_PARAMS:
            raise ValidationError('"cmd" contains invalid value')


class BatchRequestParams(Schema):
    """
    Класс, позволяющий расширить число параметров в модели.
    """
    queries = fields.Nested(RequestParams, many=True)

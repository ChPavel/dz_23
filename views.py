from typing import Any

from flask import Blueprint, request, jsonify
from models import BatchRequestParams
from marshmallow import ValidationError
from functions import build_query


main_bp = Blueprint('main', __name__)


@main_bp.route('/perform_query', methods=['POST'])
def perform_query() -> Any:
    try:
        params: dict = BatchRequestParams().load(request.json)  # type: ignore
    except ValidationError as e:
        return e.messages, 400

    result = None
    for query in params['queries']:
        result = build_query(
            cmd=query['cmd'],
            param=query['value'],
            data=result
        )

    return jsonify(result)

from functools import wraps
from functools import wraps

from flask import jsonify


def get_token(_request):
    _t = _request.cookies.get('authToken')
    if _t is None:
        _t = _request.headers.get('authToken')
    return _t


def login_required(_request):
    def decorator(func):
        @wraps(func)
        def vld_decorated(*args, **kwargs):
            t = get_token(_request)

            if t is not None:
                return func(*args, **kwargs)
            else:
                return jsonify({'code': 400,
                                'message': 'Invalid token',
                                'response': []})

        return vld_decorated

    return decorator

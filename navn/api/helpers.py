from flask import request as request
from flask import Flask


from functools import wraps


def enforce_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        headers = request.headers
        if "key" in headers:
            if headers["key"] == Flask.API_KEY:
                return func(*args, **kwargs)
        else:
            return "ERROR"

    return wrapper

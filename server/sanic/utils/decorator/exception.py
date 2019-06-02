# -*- coding: utf-8 -*-
# @Time     : 4/30/19 4:32 PM
# @Author   : Lee才晓
# @Describe :
from sanic.exceptions import abort
from sanic_jwt_extended import jwt_required


def try_except(func):
    def dec(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            raise e

    return dec


def response_exception(func):
    @jwt_required
    def wrapper(request, *args, **kwargs):
        try:
            return func(request, *args, **kwargs)
        except Exception as e:
            return abort(status_code=500, message=e)

    return wrapper
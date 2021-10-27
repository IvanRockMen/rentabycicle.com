import datetime
import functools
import inspect
import json
import traceback

from django.db import transaction
from django.http import JsonResponse
from django.views import View


JSON_DUMP_PARAMS = {
    'ensure_ascii': False
}

def return_response(json_object, status=200):
    """Отдаёт JSON с правильными HTTP заголовками и в читаемой
    в браузере виде в случае с кирилицей."""
    return JsonResponse(
        json_object,
        status=status,
        safe=not isinstance(json_object, list),
        json_dumps_params=JSON_DUMP_PARAMS
    )

def error_response(exception):
    """Формирует HTTP ответ с описанием ошибки и Traceback'ом."""
    res = {
        "errorMessage": str(exception),
        "traceback": traceback.format_exc()
    }
    return return_response(res, status=400)

def base_view(fn):
    """Декоратор для обработки исключений"""
    @functools.wraps(fn)
    def inner(request, *args, **kwargs):
        try:
            with transaction.atomic():
                return fn(request, *args, **kwargs)
        except Exception as e:
            return error_response(e)

    return inner

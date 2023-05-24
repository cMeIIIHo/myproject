import json
from concurrent.futures import ThreadPoolExecutor, wait
from contextlib import contextmanager
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.transaction import get_connection
from django.conf import settings
import pytz
from functools import wraps


# .strftime("%d.%m %H:%M")

# вытащит все параметры из запроса (post, get, body) запихнет в request.its_params
def its_params(function):
    @wraps(function)
    def _f(request, *args, **kwargs):
        try:
            params = json.loads(request.body.decode('utf-8'))
        except ValueError:
            params = {}

        for key, value in request.POST.items():
            params[key] = value

        for key, value in request.GET.items():
            params[key] = value

        request.its_params = params
        return function(request, *args, **kwargs)

    return _f


@contextmanager
def lock_table(model):
    with transaction.atomic():
        cursor = get_connection().cursor()
        cursor.execute(f'LOCK TABLE {model._meta.db_table}')
        try:
            yield
        finally:
            cursor.close()


def set_tz(dt, tz=settings.TIME_ZONE):
    timezone = pytz.timezone(tz)
    dt = timezone.localize(dt.replace(tzinfo=None))
    return dt


def change_tz(dt, tz='Europe/Moscow'):
    dt = dt.astimezone(tz=pytz.timezone(tz))
    return dt


# создание декоратора
def simple_decorator_with_args(*decorator_args, **decorator_kwargs):
    def real_decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            # do smth with decorator_args, decorator_kwargs
            # do smth with args, kwargs

            func_result = function(*args, **kwargs)
            return func_result

        return wrapper

    return real_decorator

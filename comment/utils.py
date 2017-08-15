from contextlib import contextmanager
from comment.models import Comment


@contextmanager
def override_autotime(model=Comment, fields=['created_at', 'updated_at']):
    _previous = {}
    for field in model._meta.local_fields:
        if field.name in fields:
            _previous[field.name] = (field.auto_now, field.auto_now_add)
            field.auto_now, field.auto_now_add = False, False
    try:
        yield
    finally:
        for field in model._meta.local_fields:
            if field.name in _previous:
                field.auto_now, field.auto_now_add = _previous[field.name]

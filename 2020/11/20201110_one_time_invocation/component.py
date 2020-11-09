from functools import cached_property

from view import View


# noinspection PyPep8Naming
class component(cached_property):

    def __init__(self, func):
        cached_property.__init__(self, func)

    def __get__(self, instance: View, owner=None):
        if not hasattr(instance, '_is_loaded') or not object.__getattribute__(instance, '_is_loaded'):
            object.__getattribute__(instance, '_wait_for_view')()
            object.__setattr__(instance, '_is_loaded', True)
        return super().__get__(instance, owner)

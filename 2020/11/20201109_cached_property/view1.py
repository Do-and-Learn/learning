from functools import cached_property

from view import View


class View1(View):

    def _wait_for_view(self):
        print('wait for view 1')

    @cached_property
    def component1(self):
        print(f'build component1 ({type(self).__name__})')
        return f'component1 ({type(self).__name__})'

    @cached_property
    def component2(self):
        print(f'build component2 ({type(self).__name__})')
        return f'component2 ({type(self).__name__})'

    @cached_property
    def component3(self):
        print(f'build component3 ({type(self).__name__})')
        return f'component3 ({type(self).__name__})'

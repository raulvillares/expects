# -*- coding: utf-8 -*

from functools import wraps

from expects import *
from expects.testing import failure


def dummy_decorator(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper_func

@dummy_decorator
def function_with_decorator():
    pass

def function_without_decorator():
    pass

@dummy_decorator # <-- this is the decorator
# dummy comment
def function_with_decorator_and_comments():
    pass


DUMMY_DECORATOR_AS_STR = '@dummy_decorator'


with describe('have decorator'):
    with it('should pass if the function is decorated'):
        expect(function_with_decorator).to(have_decorator(DUMMY_DECORATOR_AS_STR))

    with it('should fail if the function is not decorated'):
        with failure(f'{DUMMY_DECORATOR_AS_STR} decorator not found in []'):
            expect(function_without_decorator).to(have_decorator(DUMMY_DECORATOR_AS_STR))

    with context('#negated'):
        with it('should pass if the function is not decorated'):
                expect(function_without_decorator).not_to(have_decorator(DUMMY_DECORATOR_AS_STR))

        with it('should fail if the function is decorated'):
            with failure(f'{DUMMY_DECORATOR_AS_STR} decorator found'):
                expect(function_with_decorator).not_to(have_decorator(DUMMY_DECORATOR_AS_STR))

    with context('managing comments'):
        with it('should ignore comments'):
            expect(function_with_decorator_and_comments).to(have_decorator(DUMMY_DECORATOR_AS_STR))
                    
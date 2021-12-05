# -*- coding: utf-8 -*

import ast
import inspect
from functools import wraps

from .. import Matcher


class have_decorator(Matcher):
    def __init__(self, expected):
        self._expected = expected

    def _match(self, function):
        decorators = self._get_method_decorators(function)
        if self._expected in decorators:
            return True, [f'{self._expected} decorator found']
        else:
            return False, [f'{self._expected} decorator not found in {decorators}']

    def _get_method_decorators(self, func):
        function_source = inspect.getsource(func)
        function_definition_index = function_source.find('def ')
        lines_before_definition = function_source[:function_definition_index].strip().splitlines()
        return [self._sanitize_decorator(line) for line in lines_before_definition if self._is_decorator_line(line)]

    def _is_decorator_line(self, line):
        return line.strip().startswith('@')

    def _sanitize_decorator(self, line):
        return line.strip().split()[0]

# -*- coding: utf-8 -*


class Matcher(object):
    def _failure_message(self, subject):
        return 'Expected {subject!r} to {description}'.format(
            subject=subject, description=self._description(subject))

    def _failure_message_negated(self, subject):
        return 'Expected {subject!r} not to {description}'.format(
            subject=subject, description=self._description(subject))


def plain_enumerate(args):
    result = ''

    total = len(args)
    for i, arg in enumerate(args):
        result += repr(arg)

        if i + 2 == total:
            result += ' and '
        elif i + 1 != total:
            result += ', '
    return result

from .equal import Equal as equal
from .be import Be as be
from .be_true import be_true
from .be_false import be_false
from .be_none import be_none
from .be_a import BeAnInstanceOf as be_a
be_an = be_a
from .be_empty import be_empty
from .be_above import BeAbove as be_above
from .be_below import BeBelow as be_below
from .be_above_or_equal import BeAboveOrEqual as be_above_or_equal
from .be_below_or_equal import BeBelowOrEqual as be_below_or_equal
from .be_within import BeWithIn as be_within
from .have_length import HaveLength as have_length
from .have_property import HaveProperty as have_property
from .have_properties import HaveProperties as have_properties
from .have_key import HaveKey as have_key
from .have_keys import HaveKeys as have_keys
from .contain import Contain as contain
from .contain_only import ContainOnly as contain_only
from .start_with import StartWith as start_with
from .end_with import EndWith as end_with
from .match import Match as match
from .raise_error import RaiseError as raise_error

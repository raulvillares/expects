# -*- coding: utf-8 -*-

from mamba import describe, context, before

from spec.fixtures import Foo

from expects import *
from expects.testing import failure


with describe('have_properties') as _:
    def it_should_pass_if_object_has_properties_in_args():
        expect(_.obj).to(have_properties('bar', 'baz'))

    def it_should_pass_if_object_has_properties_in_kwargs():
        expect(_.obj).to(have_properties(bar=0, baz=1))

    def it_should_pass_if_object_has_properties_in_args_and_kwargs():
        expect(_.obj).to(have_properties('bar', baz=1))

    def it_should_pass_if_object_has_properties_in_dict():
        expect(_.obj).to(have_properties({'bar': 0, 'baz': 1}))

    def it_should_fail_if_object_does_not_have_property_in_args():
        with failure("to have properties 'bar' and 'foo'"):
            expect(_.obj).to(have_properties('bar', 'foo'))

    def it_should_fail_if_object_does_not_have_property_in_kwargs():
        with failure('to have properties bar=0 and foo=1'):
            expect(_.obj).to(have_properties(bar=0, foo=1))

    def it_should_fail_if_object_has_property_without_value_in_kwargs():
        with failure('to have properties bar=1 and baz=1'):
            expect(_.obj).to(have_properties(bar=1, baz=1))

    def it_should_fail_if_object_does_not_have_property_in_args_but_in_kwargs():
        with failure("to have properties 'foo' and bar=0"):
            expect(_.obj).to(have_properties('foo', bar=0))

    def it_should_fail_if_object_has_property_in_args_and_kwargs_without_value():
        with failure("to have properties 'baz' and bar=1"):
            expect(_.obj).to(have_properties('baz', bar=1))

    def it_should_fail_if_object_has_property_without_value_in_dict():
        with failure('to have properties bar=1 and baz=1'):
            expect(_.obj).to(have_properties({'bar': 1, 'baz': 1}))

    with context('#negated'):
        def it_should_pass_if_object_does_not_have_properties_in_args():
            expect(_.obj).not_to(have_properties('foo', 'foobar'))

        def it_should_pass_if_object_does_not_have_properties_in_kwargs():
            expect(_.obj).not_to(have_properties(foo=0, foobar=1))

        def it_should_pass_if_object_has_property_without_value_in_kwargs():
            expect(_.obj).not_to(have_properties(foo=0, bar=1))

        def it_should_pass_if_object_does_not_have_properties_in_dict():
            expect(_.obj).not_to(have_properties({'foo': 0, 'foobar': 1}))

        def it_should_pass_if_object_has_property_without_value_in_dict():
            expect(_.obj).not_to(have_properties({'foo': 0, 'bar': 1}))

        def it_should_pass_if_object_has_one_property_and_not_the_other_in_args():
            expect(_.obj).not_to(have_properties('foo', 'bar'))

        def it_should_fail_if_object_has_properties_in_args():
            with failure("not to have properties 'bar' and 'baz'"):
                expect(_.obj).not_to(have_properties('bar', 'baz'))

        def it_should_fail_if_object_has_properties_in_kwargs():
            with failure("not to have properties bar=0 and baz=1"):
                expect(_.obj).not_to(have_properties(bar=0, baz=1))

    @before.each
    def fixtures():
        _.obj = Foo()

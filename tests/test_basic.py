import os
import pytest
from jinja2 import Template, Environment


def test_no_extension():
    template = Template('foo {{ bar }}')
    result = template.render(bar="foo")
    assert result == "foo foo"


def test_extension1():
    env = Environment(extensions=["jinja2_getenv_extension.GetenvExtension"])
    os.environ["FOOBAR"] = "foobar"
    template = env.from_string("test {{ \"FOOBAR\"|getenv }}")
    result = template.render()
    assert result == "test foobar"


def test_extension2():
    env = Environment(extensions=["jinja2_getenv_extension.GetenvExtension"])
    try:
        del (os.environ["FOOBAR"])
    except KeyError:
        pass
    template = env.from_string("test {{ \"FOOBAR\"|getenv }}")
    with pytest.raises(Exception):
        template.render()


def test_extension3():
    env = Environment(extensions=["jinja2_getenv_extension.GetenvExtension"])
    try:
        del (os.environ["FOOBAR"])
    except KeyError:
        pass
    template = env.from_string("test {{ \"FOOBAR\"|getenv(\"foo\") }}")
    result = template.render()
    assert result == "test foo"

from typing import Tuple, TypeVar, Union

import pytest

from generic_args import TypeArgsError, generic_type_args

T = TypeVar('T')   # noqa: WPS111


GET_ARGS_DOCSTRING_TESTCASES = [
    # Source: typing_inspect.get_args docstring
    (
        Union[int, Union[T, int], str][int],  # type: ignore
        (int, str),
    ),
    (
        Union[int, Tuple[T, int]][str],  # type: ignore
        (int, Tuple[str, int]),
    ),
]


FAILURE_TESTCASES = [
    int,
    str,
    object,

    object(),
    5,
    3.1415,
    'foo',
    {},
]


@pytest.mark.parametrize(  # noqa: WPS317
    (
        'generic_type',
        'type_parameters',
    ),
    GET_ARGS_DOCSTRING_TESTCASES,
)
def test_get_args_docstring(generic_type, type_parameters):
    """Tests for typing.Generic."""
    assert generic_type_args(generic_type) == type_parameters


@pytest.mark.parametrize('type_or_value', FAILURE_TESTCASES)
def test_failure(type_or_value):
    """Test a value which does not have generic parameters."""
    with pytest.raises(TypeArgsError):
        generic_type_args(type_or_value)

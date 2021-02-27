from typing import Tuple, TypeVar, Union

import pytest

from generic_args import TypeArgsError, generic_type_args

T = TypeVar('T')   # noqa: WPS111


SUCCESS_TESTCASES = [   # noqa: WPS407
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


FAILURE_TESTCASES = [   # noqa: WPS407
    int,
    str,

    5,
    3.1415,
    'foo',
    {},
]


@pytest.mark.parametrize(('generic_type', 'type_parameters'), SUCCESS_TESTCASES)
def test_success(generic_type, type_parameters):
    """Tests for typing.Generic."""
    assert generic_type_args(generic_type) == type_parameters


@pytest.mark.parametrize('type_or_value', FAILURE_TESTCASES)
def test_failure(type_or_value):
    """Test a value which does not have generic parameters."""
    with pytest.raises(TypeArgsError):
        generic_type_args(type_or_value)

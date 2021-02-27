import types
from typing import Iterable, Mapping

import pytest

from generic_args import generic_type_args

TESTCASES = [
    (Iterable[int], (int, )),
    (Mapping[str, float], (str, float)),
]


@pytest.mark.parametrize(('generic_type', 'type_parameters'), TESTCASES)
def test_plain_generic(generic_type, type_parameters):
    """Test generic type."""
    assert generic_type_args(generic_type) == type_parameters


@pytest.mark.parametrize(('generic_type', 'type_parameters'), TESTCASES)
def test_generic_with_inheritance(generic_type, type_parameters):
    """Test inheritance from generic type."""
    subclass_type = types.new_class('SubClass', (generic_type, ), {})
    assert generic_type_args(subclass_type) == type_parameters

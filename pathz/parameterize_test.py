import pytest

@pytest.mark.parametrize("x", [1, 2, 3])
def test_example(x):
    assert x > 0

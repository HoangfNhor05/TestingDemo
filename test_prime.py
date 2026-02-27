import pytest
from utils import is_prime


def test_true():
    assert is_prime(2) == True


def test_false():
    assert is_prime(4) == False


def test_exception():
    with pytest.raises(ValueError):
        is_prime(1)


@pytest.mark.timeout(2)
def test_timeout():
    is_prime(99999)
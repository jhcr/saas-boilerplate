import pytest
from utils import hashid


pytestmark = pytest.mark.django_db


def test_encode_decode_roundtrip():
    original = 123
    encoded = hashid.encode(original)
    assert hashid.decode(encoded) == original


def test_decode_invalid_returns_none():
    assert hashid.decode("invalid") is None

from hashids import Hashids
from django.conf import settings

hashids = Hashids(salt=settings.HASHID_FIELD_SALT, min_length=7)


def encode(val):
    return hashids.encode(val)


def decode(val):
    try:
        decoded = hashids.decode(val)
    except TypeError:
        return None
    return decoded[0] if decoded else None

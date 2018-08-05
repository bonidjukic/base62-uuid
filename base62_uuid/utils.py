import string

from uuid import uuid4


def uuid_to_base62():
    """ Shortens generated uuid using 62-character base. """
    integer = uuid4().int
    base = string.digits + string.ascii_letters
    if integer == 0:
        return base[0]

    length = len(base)
    ret = ''
    while integer != 0:
        ret = base[integer % length] + ret
        integer = integer // length

    return ret

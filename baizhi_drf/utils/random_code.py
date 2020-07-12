import random


def get_random_code():
    code = "%06d" % random.randint(0, 999999),
    return code

def animals(num: int = 0) -> str:

    """Return name of animals

    :param -> num
    :return -> "animal" """
    if num <= 3:
        return "rabbit"
    elif num <= 5:
        return "dog"
    elif num <= 7:
        return "cat"
    elif num <= 10:
        return "bear"
    elif num <= 14:
        return "spider"
    elif num <= 17:
        return "bird"
    elif num <= 20:
        return "fish"
    else:
        return "not foud"


def multiplos(num: int) -> str:
    """ Return the number is multiple

    :param -> num
    :return -> str"""

    if num % 3 == 0 and num % 5 != 0:
        return "Only Three"
    elif num % 5 == 0 and num % 3 != 0:
        return "Only Five"
    elif num % 3 == 0 and num % 5 == 0:
        return "Three and Five"
    else:
        return "None"


print(animals(7))
help(animals)

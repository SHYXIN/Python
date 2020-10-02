"""
https://en.wikipedia.org/wiki/Merge_sort
"""


def merge_sort(array, left: int, right: int):
    """
    Merge sort algorithm.
    :param array: the array to be sorted.
    :param left: the left index of sub array.
    :param right: the right index of sub array.
    :return: sorted array.

    >>> import random
    >>> array = random.sample(range(-50, 50), 10)
    >>> merge_sort(array, 0, len(array) - 1) == sorted(array)
    True
    >>> import string
    >>> array = random.choices(string.ascii_letters + string.digits, k = 10)
    >>> merge_sort(array, 0, len(array) - 1) == sorted(array)
    True
    >>> array = [random.uniform(-50.0, 50.0) for i in range(10)]
    >>> merge_sort(array, 0, len(array) - 1) == sorted(array)
    True
    """
    if left < right:
        middle = (left + right) >> 1
        merge_sort(array, left, middle)
        merge_sort(array, middle + 1, right)
        merge(array, left, middle, right)
    return array


def merge(array, left: int, middle: int, right: int):
    """
    Merge two sorted sub array.
    :param array: the array to be sorted.
    :param left: the left index of first sub array.
    :param middle: the right index of first sub array.
    :param right: the right index of second sub array.
    :return: sorted array.
    """
    i = left
    j = middle + 1
    k = left
    while i <= middle and j <= right:
        if array[i] <= array[j]:
            array[k] = array[i]
            i += 1
        else:
            array[k] = array[j]
            j += 1
        k += 1

    while i <= middle:
        array[k] = array[i]
        i += 1
        k += 1

    while j <= right:
        array[k] = array[j]
        j += 1
        k += 1
    pass


if __name__ == '__main__':
    from doctest import testmod

    testmod()

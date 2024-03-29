def neighbor_digits(num, prev_digit=-1):
    """
    Returns the number of digits in num that have the same digit to its right
    or left.
    >>> neighbor_digits(111)
    3
    >>> neighbor_digits(123)
    0
    >>> neighbor_digits(112)
    2
    >>> neighbor_digits(1122)
    4
    """
    if num < 10:
        return num == prev_digit
    rest = num // 10
    last = num % 10
    return int(prev_digit == last or rest % 10 == last) + neighbor_digits(rest, last)



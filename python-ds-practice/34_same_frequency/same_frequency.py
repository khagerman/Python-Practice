def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

    >>> same_frequency(551122, 221515)
    True

    >>> same_frequency(321142, 3212215)
    False

    >>> same_frequency(1212, 2211)
    True
    """

    # turn num into string into a list and compare if they have the same numbers
    a = list(str(num1))
    b = list(str(num2))
    a.sort()
    b.sort()
    return a == b

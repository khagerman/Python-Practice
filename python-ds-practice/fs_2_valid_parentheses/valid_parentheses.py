def valid_parentheses(parens):
    """Are the parentheses validly balanced?

    >>> valid_parentheses("()")
    True

    >>> valid_parentheses("()()")
    True

    >>> valid_parentheses("(()())")
    True

    >>> valid_parentheses(")()")
    False

    >>> valid_parentheses("())")
    False

    >>> valid_parentheses("((())")
    False

    >>> valid_parentheses(")()(")
    False
    """
    open_p = "("
    close_p = ")"
    count = 0
    for i in range(len(parens)):
        if parens[i] == open_p and parens[i + 1] == close_p:
            count += 1
    return count != 0 and count % 2 == 0

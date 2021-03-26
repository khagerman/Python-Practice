def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

    >>> vowel_count('rithm school')
    {'i': 1, 'o': 2}

    >>> vowel_count('HOW ARE YOU? i am great!')
    {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowel = set("aeiou")
    new_dict = {}
    for letter in phrase.lower():
        if letter in vowel:
            new_dict[letter] = new_dict.get(letter, 0) + 1
    return new_dict
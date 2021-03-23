def print_upper_words(words):
    """Given list of words, print each word in uppercase
    For example:
      ["hello", "hey", "yo", "yes"]

    Should print:
        HELLO
        HEY
        YO
        YES
    """
    for word in words:
        print(word.upper())


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])


def print_letter_e_words(words):
    """Given list of words, print each word that starts with the letter "e"
    For example:
      ["eye", "hello", "yo", "east"]

    Should print:
        eye
        east
    """
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())


print_letter_e_words(["eye", "hello", "yo", "east"])


def print_words_that_start_with(words, must_start_with):
    """Given list of words, print each word that starts with a given set of letters
    For example:
    ["hello", "hey", "goodbye", "yo", "yes"],
                must_start_with={"h", "y"})
    Should print:
        "HELLO", "HEY", "YO", and "YES"
    """

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())


print_words_that_start_with(
    ["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"}
)

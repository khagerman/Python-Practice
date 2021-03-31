"""Word Finder: finds random words from a dictionary.
>>> wf = WordFinder("sample.txt")
3 words read

>>> wf.random()
'cat'

>>> wf.random()
'cat'

>>> wf.random()
'porcupine'

>>> wf.random()
'dog'
"""
import random


class WordFinder:
    def __init__(self, file_name="words.txt"):

        # get file to read
        # get words from file
        # print number of words read in file

        self.file_name = file_name
        self.words = open(self.file_name).read().splitlines()
        print(f"{len(self.words)} words read")

    def random(self):
        """Return random word from file given"""
        return random.choice(self.words)

    def __repr__(self):
        "Show reprenstation"
        return f"<start={self.start} current_num={self.current_num}>"


class SpecialWordFinder(WordFinder):
    """
    Method that returns a random word from a list of words but omits blank lines
    or words that begin with a special character.
    """

    def __init__(self, words):
        # get parent class [`super()`], call its `__init__()`
        super().__init__(words)
        self.filter_words = [
            word for word in self.words if word != "" and not word.startswith("#")
        ]
        print(f"{len(self.filter_words)} words read")

    def check_if_word(self):
        for word in self.filter_words:
            return word
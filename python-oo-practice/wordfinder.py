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
    def __init__(self, file):

        # get file to read

        # print number of words read in file

        file_contents = open(file)
        self.words = self.get_words(file_contents)
        print(f"{len(self.words)} words read")

    def get_words(self, file_contents):
        """get words from file given"""
        return file_contents.read().splitlines()

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

    def get_words(self):
        for word in self.filter_words:
            return word

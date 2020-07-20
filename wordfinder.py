"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    def __init__(self, dict_file):
        self.dict_file = dict_file
        self.word_list = self.read_file(dict_file)

    def read_file(self, dict_file):
        """Parse text from reference file"""
        file = open(dict_file, 'r')
        text = file.read()
        word_list = text.split('\n')
        file.close()
        return word_list

    def random(self):
        """Get random word from list"""
        return random.choice(self.word_list)


class SpecialWordFinder(WordFinder):
    """Removes blank lines and comments from the word list"""

    def __init__(self, dict_file):
        super().__init__(dict_file)
        self.word_list = [
            word for word in self.word_list if word != '' and word[0] != '#']

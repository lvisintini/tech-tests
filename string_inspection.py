from collections import Counter

from constants import VOWELS, CONSONANTS


class StringInspector(object):
    """
        A class to group all string inspections in one object.
    """

    def __init__(self, string):
        self.string = string

    @property
    def char_counts(self):
        if not hasattr(self, '_char_counts'):
            self._char_counts = Counter(self.string.lower())
        return self._char_counts


    def vowel_counts(self):
        vowel_counts = dict(zip(VOWELS, [0]*len(VOWELS)))

        vowel_counts.update({
            char: count
            for char, count in self.char_counts.items()
            if char in VOWELS
        })

        return vowel_counts

    def consonants_count(self):
        return sum([
            count
            for char, count in self.char_counts.items()
            if char in CONSONANTS
        ])


def inspect_string(string):

    inspector = StringInspector(string)

    return inspector.vowel_counts(), inspector.consonants_count()



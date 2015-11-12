from constants import VOWELS, CONSONANTS

from string_inspection import StringInspector


class TestStringInspection(object):

    def test_vowel_counts_is_case_insensitive(self):
        """
            Check vowels are counted regardless of case

        """
        inspector = StringInspector(VOWELS.lower() + VOWELS.upper())

        expected = {
            'a': 2,
            'e': 2,
            'i': 2,
            'o': 2,
            'u': 2,
        }

        assert inspector.vowel_counts() == expected

    def test_vowel_counts(self):
        """
            Check vowels are counted correctly

        """
        inspector = StringInspector('asdfghjkl')
        expected = {
            'a': 1,
            'e': 0,
            'i': 0,
            'o': 0,
            'u': 0,
        }
        assert inspector.vowel_counts() == expected

        inspector = StringInspector('asdfghijkl...a.sdeeeu0oee')
        expected = {
            'a': 2,
            'e': 5,
            'i': 1,
            'o': 1,
            'u': 1,
        }
        assert inspector.vowel_counts() == expected


    def test_all_vowels_are_matched(self):
        """
            Check all vowels are matched

        """
        inspector = StringInspector(VOWELS.lower())
        expected = {
            'a': 1,
            'e': 1,
            'i': 1,
            'o': 1,
            'u': 1,
        }
        assert inspector.vowel_counts() == expected

    def test_vowel_counts_empty_string(self):
        """
            Zeroes all around
        """

        inspector = StringInspector('')
        expected = {
            'a': 0,
            'e': 0,
            'i': 0,
            'o': 0,
            'u': 0,
        }
        assert inspector.vowel_counts() == expected


    def test_constants_count_is_case_insensitive(self):
        """
            Check consonant is counted regardless of case

        """

        inspector = StringInspector('bBcCdDfFgG')
        assert inspector.consonants_count() == 10

    def test_consonats_count(self):
        """
            Check consonant are counted correctly

        """

        inspector = StringInspector('qqwertyuioafasdfdsfsdfghjklzxcvbnm')
        assert inspector.consonants_count() == 28

    def test_all_consonats_are_matched(self):
        """
            Check all consonants are matched

        """

        inspector = StringInspector(CONSONANTS)
        assert inspector.consonants_count() == len(CONSONANTS)
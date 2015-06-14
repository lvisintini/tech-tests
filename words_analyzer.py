from collections import defaultdict


class WordsAnalyzer(object):
    def __init__(self, words):
        self.words = words

    @property
    def anagram_groups(self):
        """
            Using the provided, returns a list of all anagram groups with more than one word in them

        """
        return sorted([group for group in self.get_anagrams_dict().values() if len(group) > 1], key=lambda g: len(g))

    @property
    def anagrams_dict(self):
        """
            Generates anagrams_dict if not already provided

            All words are grouped in lists inside a dict where the keys are a string of the word's sorted letters in
            lower case.

            Like:

            {
                'aemt': ['tame', 'team', 'meat'],
                'aelmnt': ['mantle', 'lament', 'mental'],
            }

        """
        if not hasattr(self, '_anagrams_dict'):
            self._anagrams_dict = defaultdict(list)
            for w in self.words:
                self._anagrams_dict[''.join(sorted(w.lower()))].append(w)
        return self._anagrams_dict

    def get_longest_chain(self):
        max_chain_length = 0
        for w in self.words:
            if len(w) > max_chain_length:
                candidate = self.get_max_chain_len(w)
                if candidate > max_chain_length:
                    max_chain_length = candidate

        return max_chain_length


    def get_max_chain_len(self, word):
        anagrams_key = ''.join(sorted(word))
        max_chain = 0
        for i in range(len(word)):
            reduced_anagrams_key = anagrams_key[:i] + anagrams_key[i + 1:]

            if self.anagrams_dict[reduced_anagrams_key]:
                next_word = self.anagrams_dict[reduced_anagrams_key][0]
                new_word_max_chains = self.get_max_chain_len(next_word)
                if new_word_max_chains > max_chain
                    max_chain = new_word_max_chains

        return max_chain + 1



if __name__ == '__main__':
    f = open('words.txt', 'r')
    words_in_file = [w.strip() for w in f.readlines()]
    f.close()
    wa = WordsAnalyzer(words_in_file)
    for ag in wa.anagram_groups:
        print ag






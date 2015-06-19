from collections import defaultdict


class WordsAnalyzer(object):
    def __init__(self, words):
        self.words = words
        self._anagrams_dict = None

    @property
    def anagram_groups(self):
        """
            Using the provided, returns a list of all anagram groups with more than one word in them

        """
        return sorted([group for group in self.anagrams_dict.values() if len(group) > 1], key=lambda g: len(g))

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
        if self._anagrams_dict is None:
            self._anagrams_dict = defaultdict(list)
            for word in self.words:
                self._anagrams_dict[self.get_anagram_key_for_word(word)].append(word)
            self._anagrams_dict = dict(self._anagrams_dict)
        return self._anagrams_dict

    def get_loaded_anagrams_for_word(self, word):
        return self.anagrams_dict.get(self.get_anagram_key_for_word(word), [])

    @staticmethod
    def get_anagram_key_for_word(word):
        return ''.join(sorted(word.lower()))

    @staticmethod
    def get_reduced_angram_keys(anagram_key_or_word):
        ak = ''.join(sorted(anagram_key_or_word.lower()))
        return list(set([ak[:i] + ak[i + 1:] for i in range(len(ak)) if len(ak) > 1]))

    def get_chains_for_word(self, word):
        ak = self.get_anagram_key_for_word(word)

        chains = [[word, ]]
        for reduced_anagram_key in self.get_reduced_angram_keys(ak):
            next_chains = self.get_chains_for_anagram_key(reduced_anagram_key)

            if next_chains:
                for chain in next_chains:
                    chain.insert(0, word)
                    chains.append(chain)

        return chains

    def get_all_chains(self):
        anagram_keys = sorted(self.anagrams_dict.keys(), reverse=True)
        chains = []
        for chains_for_ak in [self.get_chains_for_anagram_key(ak) for ak in anagram_keys]:
            chains += chains_for_ak
        return chains

    def get_chains_for_anagram_key(self, ak):
        # use memoize decorator to avoid lookign for the same words
        chains = []

        for word in self.anagrams_dict.get(ak, []):
            chains.extend([[word, ]])

            for reduced_anagram_key in self.get_reduced_angram_keys(ak):

                next_chains = [
                    [word, ] + next_chain
                    for next_chain in self.get_chains_for_anagram_key(reduced_anagram_key)
                    if next_chain
                ]

                chains.extend(next_chains)

        return chains

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
                if new_word_max_chains > max_chain:
                    max_chain = new_word_max_chains

        return max_chain + 1

if __name__ == '__main__':
    f = open('words.txt', 'r')
    words_in_file = [w.strip() for w in f.readlines()]
    f.close()
    wa = WordsAnalyzer(words_in_file)
    #for ag in wa.anagram_groups:
    #    print ag

    #print wa.get_chains_for_word('Angelica')

    for chain in wa.get_chains_for_word('Angelica'):
        if len(chain) > 1:
            print ' -> '.join(chain)
    #print wa.get_loaded_anagrams_for_word('ramada')
    #print map(len, wa.get_reduced_angram_keys('ramada'))
    #print [map(len, c) for c in wa.get_chains_for_word('ramada')]


    for chain in wa.get_all_chains():
        if len(chain) > 1:
            print ' -> '.join(chain)

    #print max([len(c) for c in wa.get_all_chains()])

import urllib2
import random

def get_new_word_file():
    word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

    response = urllib2.urlopen(word_site)
    txt = response.read()
    WORDS = txt.splitlines()

    sample = []
    valid_chars = map(chr, range(97, 123)) + map(chr, range(65, 91))
    while len(sample) < 10000:
        sel = random.choice(WORDS)
        if len(sel) > 2 and all([x in valid_chars for x in sel]) and sel.upper() != sel and sel not in sample:
            sample.append(sel)

    sample = sorted(sample)

    f = open('words.txt', 'w')
    f.writelines([s + '\n' for s in sample])
    f.close()

if __name__ == '__main__':
    get_new_word_file()

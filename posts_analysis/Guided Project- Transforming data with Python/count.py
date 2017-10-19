import read
import itertools
import re
from collections import Counter

df = read.load_data()

def string_splitter(x):
    s = re.sub('[()\[\]\?\:]', '', str(x))
    splitted = str(s).split(" ")
    return splitted

all_headlines = [string_splitter(x) for x in df["headline"]]
flat_headlines = [s.lower() for s in list(itertools.chain.from_iterable(all_headlines))]

word_count_100 = Counter(flat_headlines).most_common(100)

print(word_count_100)



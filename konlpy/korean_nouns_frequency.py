from konlpy.tag import Okt
from collections import Counter
import csv


filename = './news.txt'
f = open(filename, 'r', encoding='utf-8')
news = f.read()

okt = Okt()
noun = okt.nouns(news)

for i, word in enumerate(noun):
    if len(word) < 2:
        noun.pop(i)

count = Counter(noun)
f.close()

noun_list = count.most_common(100)
for word in noun_list:
    print(word)

with open("noun_list.txt", 'w', encoding='utf-8') as f:
    for word in noun_list:
        f.write(" ".join(map(str, word)))
        f.write("\n")
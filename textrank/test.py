from text_rank import TextRank

url = 'https://news.v.daum.net/v/20210316153619695'
textrank = TextRank(url)
for row in textrank.summarize(3):
    print(row)
    print()
print('keyword: ', textrank.keywords())
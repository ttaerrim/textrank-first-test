from text_rank import TextRank

url = 'https://news.v.daum.net/v/20170611192209012?rcmd=r'
textrank = TextRank(url)
for row in textrank.summarize(3):
    print(row)
    print()
print('keyword: ', textrank.keywords())
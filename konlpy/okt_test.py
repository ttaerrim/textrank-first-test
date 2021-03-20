from konlpy.tag import Okt

okt = Okt()

print(okt.morphs('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다.'))
print(okt.nouns('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다.'))
print(okt.phrases('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다.'))
print(okt.pos('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다.'))
print(okt.pos('이런 것도 되나욬ㅋㅋㅋ'))
print(okt.pos('이런 것도 되나욬ㅋㅋㅋ', norm=True))
print(okt.pos('이런 것도 되나욬ㅋㅋㅋ', norm=True, stem=True))

######################

print(okt.nouns("띄어쓰기가꼭필요한가요이렇게대충써도가능한가요"))
print(okt.pos("품사도 태깅해 주는 okt this is english ^^* 이렇게 쓰는 것도 가능해욬ㅋㅋ 이건 stt 돌리면 필요는 없겠다", norm=True, stem=True))
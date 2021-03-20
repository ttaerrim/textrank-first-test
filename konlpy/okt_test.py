from konlpy.tag import Okt

okt = Okt()

print(okt.morphs('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다.'))
print(okt.nouns('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다.'))
print(okt.phrases('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다.'))
print(okt.pos('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다.'))
print(okt.pos('이런 것도 되나욬ㅋㅋㅋ'))
print(okt.pos('이런 것도 되나욬ㅋㅋㅋ', norm=True))
print(okt.pos('이런 것도 되나욬ㅋㅋㅋ', norm=True, stem=True))

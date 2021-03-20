from konlpy.tag import Hannanum, Kkma, Komoran, Okt, Mecab

## Hannanum class
hannanum = Hannanum()

print(hannanum.analyze('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다.'))
print(hannanum.morphs('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다.'))
print(hannanum.nouns('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다.'))
print(hannanum.pos('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다.'))

## Kkma class

kkma = Kkma()

print(kkma.morphs('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다.'))
print(kkma.nouns('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다.'))
print(kkma.pos('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다.'))
print(kkma.sentences('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다. 근데 난 흑마늘 뭐시기 먹어 보지도 못했는데 어쩌라는 건지 모르겠고요. 이거 문장 부호 안 찍어도 돼요 아니면 어떻게 되는 거예요 정답 알려 주세요'))

## Komoran class

komoran = Komoran()

print(komoran.morphs('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다.'))
print(komoran.nouns('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다.'))
print(komoran.pos('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다.'))

## Mecab class

mecab = Mecab()

print(mecab.morphs('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다.'))
print(mecab.nouns('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다.'))
print(mecab.pos('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다.'))

## Okt class

okt = Okt()

print(okt.morphs('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다.'))
print(okt.nouns('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다.'))
print(okt.phrases('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다.'))
print(okt.pos('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다.'))
print(okt.pos('이런 것도 되나욬ㅋㅋㅋ'))
print(okt.pos('이런 것도 되나욬ㅋㅋㅋ', norm=True))
print(okt.pos('이런 것도 되나욬ㅋㅋㅋ', norm=True, stem=True))

print(okt.nouns("띄어쓰기가꼭필요한가요이렇게대충써도가능한가요"))
print(okt.pos("품사도 태깅해 주는 okt this is english ^^* 이렇게 쓰는 것도 가능해욬ㅋㅋ 이건 stt 돌리면 필요는 없겠다", norm=True, stem=True))
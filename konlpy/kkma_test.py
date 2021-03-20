from konlpy.tag import Kkma

kkma = Kkma()

print(kkma.morphs('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다.'))
print(kkma.nouns('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다.'))
print(kkma.pos('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다.'))
print(kkma.sentences('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다. 근데 난 흑마늘 뭐시기 먹어 보지도 못했는데 어쩌라는 건지 모르겠고요. 이거 문장 부호 안 찍어도 돼요 아니면 어떻게 되는 거예요 정답 알려 주세요'))
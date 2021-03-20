from konlpy.tag import Mecab

mecab = Mecab()

print(mecab.morphs('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다.'))
print(mecab.nouns('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다.'))
print(mecab.pos('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다.'))
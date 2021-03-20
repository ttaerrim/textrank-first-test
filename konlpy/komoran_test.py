from konlpy.tag import Komoran

komoran = Komoran()

print(komoran.morphs('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다.'))
print(komoran.nouns('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다.'))
print(komoran.pos('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다.'))
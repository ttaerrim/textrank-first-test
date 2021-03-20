from konlpy.tag import Hannanum

hannanum = Hannanum()

print(hannanum.analyze('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다.'))
print(hannanum.morphs('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다.'))
print(hannanum.nouns('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다.'))
print(hannanum.pos('롯데마트의 흑마늘양념 치킨이 논란이 되고 있다.'))
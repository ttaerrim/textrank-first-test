from wordcloud import WordCloud

filename = "./noun_list.txt"
f = open(filename, 'r', encoding='utf-8')
noun_list = f.read()

wordcloud = WordCloud(font_path="/System/Library/Fonts/AppleSDGothicNeo.ttc", background_color='white')

result = wordcloud.generate(noun_list)
image = result.to_image()
image.show()
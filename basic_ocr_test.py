import easyocr
reader = easyocr.Reader(['en'])

# file = 'images/npaper.jpg'
file = 'images/code.png'

result = reader.readtext(file)
# print(result)

text = []

for data in result:
    word = data[1]
    text.append(word)

print(text)
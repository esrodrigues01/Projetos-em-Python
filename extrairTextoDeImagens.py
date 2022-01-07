import easyocr 

reader = easyocr.Reader(['pt'])

results = reader.readtext('exemplo.png', paragraph = False)


for result in results:
    print(f'Texto: {result[0]}\n')
    print(f'Posição: {result[1]}\n')
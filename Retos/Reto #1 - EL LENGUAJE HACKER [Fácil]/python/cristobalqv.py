diccionario = {'a':'4',
               'b':'I3',
               'c':'[',
               'd':')',
               'e':'3',
               'f':'|=',
               'g':'&',
               'h':'#',
               'i':'1',
               'j':',_|',
               'k':'>|',
               'l':'1',
               'm':'/\/\ ',
               'n':'^/',
               'o':'0',
               'p':'|*',
               'q':'(_,)',
               'r':'I2',
               's':'5',
               't':'7',
               'u':'(_)',
               'v':'\/',
               'w':'\/\/',
               'x':'><',
               'y':'j',
               'z':'2'}

lista = []

input = input('escriba una frase: ').lower()

for letra in input:
    for key, value in diccionario.items():
        if letra == key:
            lista.append(value)
        else:
            pass

str_unido = ''.join(lista)
        
print(str_unido)
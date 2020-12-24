fw = open('sample.txt', 'w')
fw.write('Writing some suff in my text file\n')
fw.write('I like caramel bacon\n')
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()


def entrada(*valores):
    archivo = open('ejemploText.txt', 'w')
    for valor in valores:
       archivo.write(valor + '\n')
    archivo.close()

def lectura(uri):
    archivo = open(uri, 'r')
    contenido = archivo.read()
    archivo.close()
    return contenido

entrada('Hola', 'Mundo', 'Mi nombre', 'es Jesus Fuentes')

print(lectura('ejemploText.txt'))

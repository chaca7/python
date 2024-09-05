
from urllib import request
from urllib.error import URLError

lista_palabra = ['carajo', 'bobo', 'mbore','puto','menso','orco']
def ver_cont(url):
    try:
        f = request.urlopen(url)
    except URLError:
        return('¡La url ' + url + 'no existe}!')
    else:
        contenido = f.read()
        return contenido
def contar_palabras(url):
    try:
        f = request.urlopen(url)
    except URLError:
        return('¡La url ' + url + 'no existe!')
    else:
        contenido = f.read()
        return len(contenido.split())

def buscar_palabras(url):
    contenido = ver_cont(url)
    for lp in lista_palabra:
        if lp in contenido.decode():
            print(f"{lp} existe en el sitio")


url = 'https://es.wiktionary.org/wiki/Wikcionario:Insultos_regionales'
print("\n----------------------------------------\n")
buscar_palabras(url)
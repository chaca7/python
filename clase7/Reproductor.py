from pygame import mixer
class Reproductor:
    #atributos
    archivo = None

    #constructor
    def __init__(self, archivo):
        self.archivo = archivo
        mixer.init()
        mixer.music.load(archivo)

    def play(self):
        mixer.music.play()
        return "Reproduciendo musica"

    def pausarMusica(self):
        mixer.music.pause()
        return "La musica se ha pausado"
    
    def stop(self):
        mixer.music.stop()
        return "La musica se ha pausado"
    
    def volumen(self, v):
        mixer.music.set_volume(v)
        return "Definiendp volumen a {}".format(v)
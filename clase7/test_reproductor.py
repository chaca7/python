from tkinter import *
from tkinter import ttk
from Reproductor import *

musica = Reproductor('x.mp3')

def play_musica():
     musica.volumen(0.8)
     x=musica.play()
     label.config(text = x)

def pausar():
     x=musica.pausarMusica()
     label.config(text = x)

master = Tk()
master.geometry("200x200")

label = Label(master, text = " Reproductor de musica")

label.pack(pady= 10)

btn_play = Button(master,text="▶", command = play_musica)
btn_play.pack(pady = 10)
btn_pausar = Button(master,text="⏸", command = pausar)
btn_pausar.pack(pady = 10)
mainloop()
from tkinter import messagebox

import os
import datetime

def abrirCalculadora():
    os.system("calc")

def mostrarHora():
    hora = datetime.datetime.now()
    messagebox.showinfo(message=f"{hora.year}", title = "La hora")
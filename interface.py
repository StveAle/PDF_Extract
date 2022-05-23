import tkinter as tk
from functions import *

class firstWindow(tk.Frame):

    #Constructor con herencia de la clase Frame de la libreria tkinter
    #La variable master es un objeto que contendrá este frame
    #usamos super para traer el constructor de la clase Frame a nuestra clase
    def __init__(self,master=None):
        super.__init__(master)
        self.master=master
        self.pack()
        self.createWidgets()

    #Creamos los elementos que tendrá el frame
    def createWidgets(self):
        pass
        
import tkinter as tk
from turtle import left, right
from functions import *

class v1Window(tk.Frame):

    #Constructor con herencia de la clase Frame de la libreria tkinter
    #La variable master es un objeto que contendrá este frame
    #usamos super para traer el constructor de la clase Frame a nuestra clase
    def __init__(self,master=None):
        super().__init__(master, width=650, height=450, bg='#C0CBFC')
        self.master=master
        #self.pack()
        self.createWidgets()

    #Creamos los elementos que tendrá el frame
    def createWidgets(self):
        self.frameMain=tk.Frame(self.master)
        self.frameMain.grid(row=0,column=3,padx=(10,10),pady=(5,5) )

        tk.Label(self.frameMain,text='Dirección: ',padx=5,pady=5).grid(row=0,column=0)
        tk.Label(self.frameMain,text='Cantidad de columnas: ',padx=5,pady=5).grid(row=1,column=0)      

        val='C: '
        self.txt1=tk.Entry(self.frameMain,width=40,textvariable=val)
        self.txt1.grid(row=0,column=2)
        #self.txt1.insert(0,'C:\\')

        self.buttonFrame=tk.Frame(self.frameMain,padx=5,pady=5)
        self.buscarBtn=tk.Button(self.frameMain,text='Buscar',padx=5,pady=5)
        self.buscarBtn.grid(row=0,column=3)
        
class campoFrame(tk.Frame):

    def __init__(self,master=None):
        super().__init__(master, bg='red')
        self.master=master
        self.createWidgets()

    def createWidgets(self):
        nCampolbl=tk.Label(self.master,text='N campo: ',padx=5,pady=5)
        nameCampolbl=tk.Label(self.master,text='Nompre del campo: ',padx=5,pady=5)
        fBuscarlbl=tk.Label(self.master,text='Forma de buscar: ',padx=5,pady=5)    
        
        nCampolbl.grid(row=0,column=0, sticky='n')
        nameCampolbl.grid(row=1,column=0, sticky='n')
        fBuscarlbl.grid(row=2,column=0, sticky='n')



if __name__=='__main__':
    root=tk.Tk()
    root.wm_title('EXTRACTOR PDF')
    app=v1Window(root)
    app.mainloop()
        
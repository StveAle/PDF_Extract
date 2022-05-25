import tkinter as tk
from tkinter import ttk
from functions import *

class v1Window(tk.Frame):

    #Constructor con herencia de la clase Frame de la libreria tkinter
    #La variable master es un objeto que contendrá este frame
    #usamos super para traer el constructor de la clase Frame a nuestra clase
    def __init__(self,master=None):
        super().__init__(master, width=650, height=450, bg='#C0CBFC')
        self.master=master
        self.createWidgets()

    #Creamos los elementos que tendrá el frame
    def createWidgets(self):
        self.frameMain=tk.Frame(self.master)
        self.frameMain.grid(row=0,column=3,padx=(10,10),pady=(5,5) )

        self.frameTop=tk.Frame(self.frameMain)
        self.frameTop.grid(row=0,columnspan=3)

        self.directlbl=tk.Label(self.frameTop,text='Dirección: ',padx=5,pady=5)
        val='C: '
        self.addresstxt=tk.Entry(self.frameTop,width=50,textvariable=val)
        self.buscarBtn=tk.Button(self.frameTop,text='Buscar',padx=5,pady=5)
        #self.txt1.grid(row=0,column=2)
        #self.txt1.insert(0,'C:\\')

        self.directlbl.pack(side='left')
        self.addresstxt.pack(side='left')
        self.buscarBtn.pack(side='left')

        tk.Label(self.frameMain,text='Cantidad de columnas: ',padx=5,pady=5).grid(row=1,column=0, sticky='w')      

        self.cFrame=tk.Frame(self.frameMain,padx=5, pady=5,borderwidth=2, relief='ridge')
        self.cFrame.grid(row=2,column=0)
        campoFrame(self.cFrame)
        
class campoFrame(tk.Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.createWidgets()

    def createWidgets(self):
        nCampolbl=tk.Label(self.master,text='N campo: ',padx=5,pady=5)
        nameCampolbl=tk.Label(self.master,text='Nompre del campo: ',padx=5,pady=5)
        fBuscarlbl=tk.Label(self.master,text='Forma de buscar: ',padx=5,pady=5)    
        
        nCampolbl.grid(row=0,column=0, sticky='e')
        nameCampolbl.grid(row=1,column=0, sticky='e')
        fBuscarlbl.grid(row=2,column=0, sticky='e')

        nCampoTbx=tk.Entry(self.master)
        nameCampoTbx=tk.Entry(self.master)
        fBuscarCbx=ttk.Combobox(self.master, state='readonly')

        nCampoTbx.grid(row=0,column=1, sticky='n')
        nameCampoTbx.grid(row=1,column=1, sticky='n')
        fBuscarCbx.grid(row=2,column=1, sticky='n')


if __name__=='__main__':
    root=tk.Tk()
    root.wm_title('EXTRACTOR PDF')
    app=v1Window(root)

    app.mainloop()
        
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
        #Frame principal
        self.frameMain=tk.Frame(self.master)
        self.frameMain.grid(row=0,column=3,padx=(10,10),pady=(5,5) )

        #Frame top
        self.frameTop=tk.Frame(self.frameMain)
        self.frameTop.grid(row=0,columnspan=3)

        #Contenido frame top
        self.directlbl=tk.Label(self.frameTop,text='Dirección: ',padx=5,pady=5)
        val='C: '
        self.addresstxt=tk.Entry(self.frameTop,width=50,textvariable=val)
        self.buscarBtn=tk.Button(self.frameTop,text='Buscar',padx=5,pady=5)
        #self.txt1.grid(row=0,column=2)
        #self.txt1.insert(0,'C:\\')
        self.directlbl.pack(side='left')
        self.addresstxt.pack(side='left')
        self.buscarBtn.pack(side='left')

        #Cantidad de campos
        self.cantFrame=tk.Frame(self.frameMain)
        self.cantFrame.grid(row=1,column=0,sticky='w',padx=(20,5))
        self.cantCampolbl=tk.Label(self.cantFrame,text='Cantidad de columnas: ',padx=5,pady=5)
        self.cantCampotxt=tk.Entry(self.cantFrame, width=3)
        self.cantCampolbl.pack(side='left')
        self.cantCampotxt.pack(side='left')

        #Frame parametros de extracción
        self.cFrame=tk.Frame(self.frameMain,padx=5, pady=5,borderwidth=2, relief='ridge')
        self.cFrame.grid(row=2,column=0)
        campoFrame(self.cFrame)

        #Botones
        self.frameButton=tk.Frame(self.frameMain,padx=10,pady=10)
        self.frameButton.grid(row=3,column=0)
        self.checkBtn=tk.Button(self.frameButton,padx=5,text='Check')
        self.createBtn=tk.Button(self.frameButton,padx=5,text='Crear')
        self.closeBtn=tk.Button(self.frameButton,padx=5,text='Cerrar')
        self.checkBtn.pack(side='left')
        self.createBtn.pack(side='left')
        self.closeBtn.pack(side='bottom')

        
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

        self.frameBotton=tk.Frame(self.master,padx=5,pady=5)
        self.frameBotton.grid(row=3,columnspan=2, sticky='w')

        ccFrame(self.frameBotton)

class ccFrame(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.createWidgets()

    def createWidgets(self):
        xlabel=tk.Label(self.master,text='X: ',padx=5,pady=5)
        ylabel=tk.Label(self.master,text='Y: ',padx=5,pady=5)
        
        xtxt=tk.Entry(self.master)
        ytxt=tk.Entry(self.master)
        
        xlabel.grid(row=0,column=0, sticky='e')
        ylabel.grid(row=1,column=0, sticky='e')
        xtxt.grid(row=0,column=1, sticky='w')
        ytxt.grid(row=1,column=1, sticky='w')

if __name__=='__main__':
    root=tk.Tk()
    root.wm_title('EXTRACTOR PDF')
    app=v1Window(root)

    app.mainloop()
        
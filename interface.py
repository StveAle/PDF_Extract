import tkinter as tk
from tkinter import Grid, ttk
from tkinter import filedialog
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
        self.master.columnconfigure(0,weight=1)
        self.master.rowconfigure(0,weight=1)
        self.frameMain.grid(row=0,column=0,padx=(10,10),pady=(5,5),sticky='news' )
        self.frameMain.columnconfigure(0,weight=1)

        #Frame top
        self.frameTop=tk.Frame(self.frameMain)
        self.frameTop.columnconfigure(1,weight=1)
        self.frameTop.rowconfigure(0,weight=1)
        self.frameTop.grid(row=0,columnspan=3,sticky='news',ipadx=5,ipady=5)
        

        #Contenido frame top
        self.directlbl=tk.Label(self.frameTop,text='Dirección: ',padx=5,pady=5)
        self.addresstxt=tk.Entry(self.frameTop,width=80,textvariable='')
        self.buscarBtn=tk.Button(self.frameTop,text='Buscar',command=self.openExplorer,padx=5,pady=5)
        #self.txt1.grid(row=0,column=2)
        #self.txt1.insert(0,'C:\\')
        self.directlbl.grid(row=0,column=0)
        self.addresstxt.grid(row=0,column=1, sticky='ew')
        self.buscarBtn.grid(row=0,column=2,padx=10)

        #Cantidad de campos
        self.cantFrame=tk.Frame(self.frameMain)
        self.cantFrame.grid(row=1,column=0,sticky='w',padx=(5,5))
        self.cantCampolbl=tk.Label(self.cantFrame,text='Cantidad de columnas: ',padx=5,pady=5)
        self.cantCampotxt=tk.Entry(self.cantFrame, width=3)
        self.crearCamposButton=tk.Button(self.cantFrame,text='Crear Campos')
        self.cantCampolbl.pack(side='left')
        self.cantCampotxt.pack(side='left')
        self.crearCamposButton.pack(side='left',padx=27)

        #Frame parametros de extracción
        self.cFrame=tk.Frame(self.frameMain,padx=5, pady=5,borderwidth=2, relief='ridge')
        self.cFrame.grid(row=2,column=0, sticky='w')
        campoFrame(self.cFrame)

        #Botones
        self.frameButton=tk.Frame(self.frameMain,padx=10,pady=10)
        self.frameButton.grid(row=3,column=0, sticky='e')
        self.checkBtn=tk.Button(self.frameButton,padx=5,text='Check')
        self.createBtn=tk.Button(self.frameButton,padx=5,text='Crear')
        self.closeBtn=tk.Button(self.frameButton,padx=5,text='Cerrar')
        self.checkBtn.pack(side='left',padx=5)
        self.createBtn.pack(side='left',padx=5)
        self.closeBtn.pack(side='bottom',padx=5)


    def openExplorer(self):
        self.file=filedialog.askopenfilename(title='ABRIR PDF', filetypes=[('Archivos PDF','*.pdf')])
        self.addresstxt.delete(0,'end')
        self.addresstxt.insert(0,self.file)
        return self.file
        
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
        
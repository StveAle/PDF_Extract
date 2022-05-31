import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkPDFViewer import tkPDFViewer as tkpdf
from functions import *

############################################################################################
#                                   PENDIENTES
#
# 1-Hacer que el scrollbar funcione
#
############################################################################################

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
        self.master.columnconfigure(0,weight=1)
        self.master.rowconfigure(0,weight=1)

        self.frameMain=tk.Frame(self.master)
        self.frameMain.pack(fill='both',expand=True)

        self.frameCanvas=tk.Canvas(self.frameMain)
        self.frameCanvas.pack(side='left',padx=(10,10),pady=(5,5),expand=True,fill=tk.BOTH)
        self.frameCanvas.columnconfigure(0,weight=1)

        #Scrollbar
        self.scrollbarMain=ttk.Scrollbar(self.frameMain,orient=tk.VERTICAL,command=self.frameCanvas.yview)
        self.scrollbarMain.pack(side='right',fill=tk.Y)
        self.frameCanvas.configure(yscrollcommand=self.scrollbarMain.set)
        self.frameCanvas.bind('<Configure>',lambda e: self.frameCanvas.configure(scrollregion=self.frameCanvas.bbox('all')))

        #Frame top
        self.frameTop=tk.Frame(self.frameCanvas)
        self.frameTop.columnconfigure(1,weight=1)
        self.frameTop.grid(row=0,columnspan=3,sticky='news',ipadx=5,ipady=5)

        #Contenido frame top
        self.directlbl=tk.Label(self.frameTop,text='Dirección: ',padx=5,pady=5)
        self.addresstxt=tk.Entry(self.frameTop,width=80,textvariable='')
        self.buscarBtn=tk.Button(self.frameTop,text='Buscar',command=self.openExplorer,padx=5,pady=5)
        self.directlbl.grid(row=0,column=0)
        self.addresstxt.grid(row=0,column=1, sticky='ew')
        self.buscarBtn.grid(row=0,column=2,padx=10)

        #PDF
        self.pdfViewFrame=tk.Frame(self.frameCanvas)
        self.pdfViewFrame.grid(row=1,column=1,sticky='news',rowspan=12)

        #Frame lateral
        self.frameLateral=tk.Frame(self.frameCanvas)
        self.frameLateral.grid(row=1,column=0,sticky='nw')

        #Cantidad de campos
        self.cantFrame=tk.Frame(self.frameLateral)
        self.cantFrame.grid(row=0,column=0,sticky='nw',padx=(5,5))
        self.cantCampolbl=tk.Label(self.cantFrame,text='Cantidad de columnas: ',padx=5,pady=5)
        self.cantCampotxt=tk.Entry(self.cantFrame, width=3)
        self.crearCamposButton=tk.Button(self.cantFrame,text='Crear Campos',command=self.crearCampos)
        self.cantCampolbl.pack(side='left',anchor='n')
        self.cantCampotxt.pack(side='left',anchor='n')
        self.crearCamposButton.pack(side='left',padx=27,anchor='n')

        #Frame parametros de extracción
        self.cFrame=tk.Frame(self.frameLateral,padx=5, pady=5,borderwidth=1, relief='solid')
        self.cFrame.grid(row=1,column=0, sticky='nw')

        #Botones
        self.frameButton=tk.Frame(self.frameLateral,padx=10,pady=10)
        self.frameButton.grid(row=2,column=0, sticky='nw')
        self.checkBtn=tk.Button(self.frameButton,padx=5,text='Check',command=self.check)
        self.createBtn=tk.Button(self.frameButton,padx=5,text='Crear', command=self.crear)
        self.closeBtn=tk.Button(self.frameButton,padx=5,text='Cerrar',command=self.cerrar)
        self.checkBtn.pack(side='left',padx=5)
        self.createBtn.pack(side='left',padx=5)
        self.closeBtn.pack(side='bottom',padx=5)

    def crearCampos(self):
        nCampos=self.cantCampotxt.get()
        self.xtxt=[]
        self.ytxt=[]
        self.campotxt=[]

        for i in range(int(nCampos)):
            cFrame=campoFrame(self.cFrame)
            cFrame.nCampoTbx.insert(0,i+1)
            self.x,self.y,self.campoName=cFrame.getObjects()
            self.xtxt.append(self.x)        
            self.ytxt.append(self.y)
            self.campotxt.append(self.campoName)        

    def openExplorer(self):
        self.file=filedialog.askopenfilename(title='ABRIR PDF', filetypes=[('Archivos PDF','*.pdf')])
        self.addresstxt.delete(0,'end')
        self.addresstxt.insert(0,self.file)
        print(self.file)
        pdfload=tkpdf.ShowPdf()
        pdfView=pdfload.pdf_view(self.pdfViewFrame,pdf_location=open(r'{}'.format(self.file),'r'),width=77,height=100)
        pdfView.pack()
        
    def cerrar(self):
        self.master.destroy()

    def check(self):
        x,y=[],[]
        for ix,iy in zip(self.xtxt,self.ytxt):
            x.append(ix.get())
            y.append(iy.get())
        
        self.listaCampos={}
        i=0
        for ix,iy in zip(x,y):
            words=listWordCC(float(ix),float(iy),r'{}'.format(self.file))
            self.listaCampos[self.campotxt[i].get()]=words
            print(self.campotxt[i].get())
            i+=1
        print(self.listaCampos)

    def crear(self):
        self.saveAsFile=filedialog.asksaveasfile(title='GUARDAR COMO',defaultextension='.xlsx', 
                                                filetypes=[('Archivos EXCEL','*.xlsx')])
        
        saveExceltoDicInterface(self.listaCampos,self.saveAsFile.name)

class campoFrame(tk.Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.createWidgets()

    def createWidgets(self):
        self.qFrame=tk.Frame(self.master,padx=3,pady=3,borderwidth=1,relief=tk.GROOVE)
        self.qFrame.pack(side=tk.TOP,anchor='nw')
        nCampolbl=tk.Label(self.qFrame,text='N campo: ',padx=5,pady=5)
        nameCampolbl=tk.Label(self.qFrame,text='Nompre del campo: ',padx=5,pady=5)
        fBuscarlbl=tk.Label(self.qFrame,text='Forma de buscar: ',padx=5,pady=5)    
        
        nCampolbl.grid(row=0,column=0, sticky='ne')
        nameCampolbl.grid(row=1,column=0, sticky='ne')
        fBuscarlbl.grid(row=2,column=0, sticky='ne')

        self.nCampoTbx=tk.Entry(self.qFrame,width=4)
        self.nameCampoTbx=tk.Entry(self.qFrame)
        fBuscarCbx=ttk.Combobox(self.qFrame, state='readonly')

        self.nCampoTbx.grid(row=0,column=1, sticky='nw')
        self.nameCampoTbx.grid(row=1,column=1, sticky='nw')
        fBuscarCbx.grid(row=2,column=1, sticky='nw')

        self.frameBotton=tk.Frame(self.qFrame,padx=5,pady=5)
        self.frameBotton.grid(row=3,columnspan=2, sticky='w')

        cFrameObj=ccFrame(self.frameBotton)
        self.x,self.y=cFrameObj.getObjects()

    def getObjects(self):
        return self.x,self.y,self.nameCampoTbx

class ccFrame(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.createWidgets()

    def createWidgets(self):
        xlabel=tk.Label(self.master,text='X: ',padx=5,pady=5)
        ylabel=tk.Label(self.master,text='Y: ',padx=5,pady=5)
        
        self.xtxt=tk.Entry(self.master)
        self.ytxt=tk.Entry(self.master)
        
        xlabel.grid(row=0,column=0, sticky='e')
        ylabel.grid(row=1,column=0, sticky='e')
        self.xtxt.grid(row=0,column=1, sticky='w')
        self.ytxt.grid(row=1,column=1, sticky='w')
        

    def getObjects(self):        
        return self.xtxt, self.ytxt
        
if __name__=='__main__':
    root=tk.Tk()
    root.wm_title('EXTRACTOR PDF-pre Alpha 0.1')
    app=v1Window(root)

    app.mainloop()
        
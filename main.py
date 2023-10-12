from tkinter import *
from tkinter import messagebox
from descomponer_Lu import  resolverSistema, verificarDescomponerLu

root = Tk()

WIDTH_TEXT = 5
WIDTH_TEXT1 = 3
class Contenerdor:
    def __init__(self, master):
        # components
        self.frame_principal = Frame(master, bg='#202020')
        self.frame_funcion1 = Frame(master)
        self.frame_funcion2 = Frame(master)

        # contenedores
        self.frame_matriz = Frame(self.frame_funcion1)
        self.frame_matriz2 = Frame(self.frame_funcion2)

        self.frame_principal.pack(expand=TRUE, fill=BOTH)

        self.label = Label(self.frame_principal,text="()")
        self.function1 = Button(self.frame_principal, text="hacer funcion 1", command=self.cambiarVentana)
        self.function2 = Button(self.frame_principal, text="hacer funcion 2", command=self.cambiarVentana2)

        self.label2 = Label(self.frame_funcion1,text="este es el segundo label")
        

        # positions
        self.label.pack()
        self.function1.pack()
        self.function2.pack()
        

    def cambiarVentana(self):
        self.frame_principal.pack_forget()
        self.frame_funcion1.pack()
        self.label2.pack()
        self.init_function1()

    def cambiarVentana2(self):
        self.frame_principal.pack_forget()
        self.frame_funcion2.pack()
        self.label2.pack()
        self.init_function2()

    def generar(self):

        numCuadrado = 3
        if not validators(self.dataINputs, numCuadrado):
            messagebox.showwarning("Advertencia", "los espacio no pueden estar vacios")
            return
        i = 0
        arrayGlobal = []
        for f in range(numCuadrado):
            arrayTem = []
            for c in range(numCuadrado):
                arrayTem.append(float(self.dataINputs[f"value{i}"].get()))
                i+=1
            arrayGlobal.append(arrayTem)

        dataLu = verificarDescomponerLu(arrayGlobal)
        # creacio  de los resultados 

        if dataLu:
            L = dataLu["L"]
            U = dataLu["U"]

            print(L)
            print(U)



        

    def init_function1(self):
        numCuadrado = 3
        self.dataINputs = {}
        i= 0
        for f in range(numCuadrado):
            for c in range(numCuadrado):
                input = Entry(self.frame_matriz, width=WIDTH_TEXT)
                input.grid(row=f,column=c)
                self.dataINputs[f"value{i}"] = input
                i+=1


        self.btn_calcular = Button(self.frame_funcion1,text='calcular', command=self.generar)

        self.frame_matriz.pack()
        self.btn_calcular.pack()


    def generar2(self):
        NUM_CUADRADO = 4
        i = 0
        M = []
        cohefientVariable = []
        for f in range(NUM_CUADRADO-1):
            arrayTem = []
            for c in range(1,NUM_CUADRADO+1):
                if c % NUM_CUADRADO == 0:
                    cohefientVariable.append(float(self.inputValues[i].get()))
                else:
                    arrayTem.append(float(self.inputValues[i].get()))
                i+=1
            M.append(arrayTem)

        # print(M,cohefientVariable)
        resolverSistema(M,cohefientVariable)



    def init_function2(self):
        numCuadrado = 3
        i= 0
        self.inputValues = {}
        letraCoheficiente = ["X", "Y", "Z", "="]
        label = Label(self.frame_funcion2, text='este es el texto 2')
        for f in range(numCuadrado):
            j = 0
            for c in range(numCuadrado+numCuadrado+2):
                if c%2== 0:
                    coheficiente = Label(self.frame_matriz2, text=letraCoheficiente[j])
                    coheficiente.grid(row=f, column=c)
                    j+=1
                else:
                    input = Entry(self.frame_matriz2, width=WIDTH_TEXT1)
                    input.grid(row=f,column=c)
                    self.inputValues[i] = input
                    i+=1


        self.btn_calcular = Button(self.frame_funcion2,text='calcular', command=self.generar2)

        self.frame_matriz2.pack()
        self.btn_calcular.pack()
        label.pack()

def validators(array, numCuadrado):
    i = 0
    for f in range(numCuadrado):
        for c in range(numCuadrado):
            if array[f"value{i}"].get().strip() == "":
                return False
            i+=1

    return True
        


root.geometry('530x530')
root.title('segundo parial')
cont = Contenerdor(root)
root.mainloop()


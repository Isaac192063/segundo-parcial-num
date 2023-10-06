from tkinter import *

root = Tk()
WIDTH_TEXT = 5
class Contenerdor:
    def __init__(self, master):
        # components
        self.frame_principal = Frame(master, bg='#202020')
        self.frame_funcion1 = Frame(master)

        # contenedores
        self.frame_matriz = Frame(self.frame_funcion1)

        self.frame_principal.pack(expand=TRUE, fill=BOTH)

        self.label = Label(self.frame_principal,text="()")
        self.btn_cambiarFrame = Button(self.frame_principal, text="cambiar a segunda pantalla", command=self.cambiarVentana)

        self.label2 = Label(self.frame_funcion1,text="este es el segundo label")
        

        # positions
        self.label.pack()
        self.btn_cambiarFrame.pack()
        

    def cambiarVentana(self):
        self.frame_principal.pack_forget()
        self.frame_funcion1.pack()
        self.label2.pack()
        self.init_function1()

    def init_function1(self):
        self.input1 = Entry(self.frame_matriz,width=WIDTH_TEXT)
        self.input2 = Entry(self.frame_matriz, width=WIDTH_TEXT)
        self.input3 = Entry(self.frame_matriz,width=WIDTH_TEXT)
        self.input4 = Entry(self.frame_matriz, width=WIDTH_TEXT)
        self.input5 = Entry(self.frame_matriz,width=WIDTH_TEXT)
        self.input6 = Entry(self.frame_matriz, width=WIDTH_TEXT)
        self.input7 = Entry(self.frame_matriz, width=WIDTH_TEXT)
        self.input8 = Entry(self.frame_matriz, width=WIDTH_TEXT)
        self.input9 = Entry(self.frame_matriz, width=WIDTH_TEXT)

        self.btn_calcular = Button(self.frame_funcion1,text='calcular', command=lambda: print('deberia calcular'))

        self.input1.grid(row=0, column=0)
        self.input2.grid(row=0, column=1)
        self.input3.grid(row=0, column=2)
        self.input4.grid(row=1, column=0)
        self.input5.grid(row=1, column=1)
        self.input6.grid(row=1, column=2)
        self.input7.grid(row=2, column=0)
        self.input8.grid(row=2, column=1)
        self.input9.grid(row=2, column=2)
        self.frame_matriz.pack()
        self.btn_calcular.pack()
        


root.geometry('530x530')
root.title('segundo parial')
cont = Contenerdor(root)
root.mainloop()


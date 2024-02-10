
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk



root = tk.Tk()
root.title("Cifrado cesar")
root.iconbitmap("icono.ico")
#variables
varopcion = IntVar()
sino=IntVar()
yn = IntVar()

frame = Frame(root)
frame.pack()
frame.config(width="650", height="350",padx=80,pady=20)

cesarimg= PhotoImage(file="cesar.png")


Label(frame, image=cesarimg).pack()

messagebox.showinfo("Cifrado Cesar", "Programa elaborado por Jorge")


Label(frame, text="\n\nSeleccione la operación que desea realizar:").pack()



def imprimir(Labe,yes,no):

    if varopcion.get() == 0:
        Label5.config(text="Texto a codificar:")
        Labe1.config(text="Salto de texto para codificar:")
        Labe.grid_forget()
        yes.grid_forget()
        no.grid_forget()
        Labe1.grid(row=5, column=0,sticky="e")
        salt.grid(row=5, column=1)


        
       
        
def vermensaje(Labe,yes,no,Labe1,salt):
    if varopcion.get()==2:
        Labe1.grid(row=5, column=0,sticky="e")
        salt.grid(row=5, column=1)
        Label5.config(text="Texto a descodificar:")
        Labe1.config(text="Salto de texto para descodificar:")
        
        
        Labe.grid(row=4, column=0,sticky="w")
        yes.grid(row=4, column=1,sticky="e")
        no.grid(row=4, column=2,sticky="e")

Radiobutton(frame, text="Codificar",variable = varopcion, value=0, command =lambda: imprimir(Labe,yes,no)).pack()
Radiobutton(frame, text="Descodificar",variable = varopcion, value=2, command =lambda: vermensaje(Labe,yes,no,Labe1,salt)).pack()







frame2 = Frame(frame)
frame2.pack()

cuadrotext5= Text(frame2, width=16, height=3)
cuadrotext5.grid(row=0, column=1)
Scrollbar = Scrollbar(frame2, command=cuadrotext5.yview)
Scrollbar.grid(row=0, column=3,sticky="nsew")

cuadrotext5.config(yscrollcommand=Scrollbar.set)



Label5 = Label(frame2,text="Texto a codificar:",font=("Comic Sans",10))
Label5.grid(row=0, column=0,sticky="e")



label6 = Label(frame2,text="\n\n¡Desea utilizar una lista personalizada?",font=("Comic Sans",10))
label6.grid(row=1, column=0,columnspan=3,sticky="we",padx=10,pady=10)




def hide_button(B1,Lab): 
    
    B1.grid_forget() 
    Lab.grid_forget()
  
def show_button(B1,Lab): 
    
    B1.grid(row=3, column=1)
    Lab.grid(row=3, column=0)
  
 

B1 = Text(frame2, width=16, height=3)
B1.grid_forget()
Lab = Label(frame2,text="Lista:",font=("Comic Sans",10))
Lab.grid_forget()
  

r1 = Radiobutton(frame2, text="SI",variable = sino, value=1, command = lambda: show_button(B1,Lab))
r2 = Radiobutton(frame2, text="NO",variable = sino, value=0, command =lambda: hide_button(B1,Lab))
r1.grid(row=2, column=0,padx=50,pady=10)
r2.grid(row=2, column=1,padx=50,pady=10)




def validate_entry(text):
    return text.isdecimal()



def veryesno(Labe1,salt):
    if yn.get() == 0:
        Labe1.grid(row=5, column=0,sticky="e")
        salt.grid(row=5, column=1)

def oculyesno(Label1,salt):
    if yn.get() == 1:
        Label1.grid_forget()
        salt.grid_forget()
        



Labe = Label(frame2,text="¿Conoce el salto de caracteres?",font=("Comic Sans",10))
yes = Radiobutton(frame2, text="SI",variable = yn, value=0, command = lambda: veryesno(Labe1,salt))
no = Radiobutton(frame2, text="NO",variable = yn, value=1, command =lambda: oculyesno(Labe1,salt)) 
Labe.grid_forget()
yes.grid_forget()
no.grid_forget()


Labe1= Label(frame2,text="Salto de texto para codificar:",font=("Comic Sans",10))

salt = Entry(frame2,
    validate="key",
    validatecommand=(root.register(validate_entry), "%S")
)
Labe1.grid_forget()
salt.grid_forget()
 


Labe1.grid(row=5, column=0,sticky="e")
salt.grid(row=5, column=1)


frame3 = Frame(frame)
frame3.pack()




def por(): 
    global sino
    global yn 
    global varopcion
    
    
    msgc=""
    Msg=cuadrotext5.get("1.0",END)
    
    if sino == 1:
        lista = B1.get("1.0",END)
        Lista_M = lista.upper()
    else:
        lista ="abcdefghijklmnñopqrstuvwxyz" 
        Lista_M = lista.upper()
        
    if varopcion.get() == 0:
        try:
            salto = salt.get()
            salto = int(salto)
        except:
            messagebox.showerror("Error", "El salto debe ser un número entero")
            return
        for msg in Msg: #Pasar cada letra del mensaje principal
                if msg == msg.lower(): #Evaluar si el datos está en minuscula
                    if msg in lista:   #Buscar si la letra del mensaje principal está en la lista definida inicialmente
                        Rempla = lista.find(msg) #Buscar posicion del elemento en la lista definida 
                        Rempla += salto          #Asignar el nuevo numero de posicion
                        while True:
                            if Rempla >= len(lista): #Analizar si el nuevo numero de posición supera la cantidad de elemtos que tiene la lista inicial
                                Rempla -= len(lista) #A la nueva posición restarle la cantidad de elementos de la lista original
                                continue
                            else:
                                break
                        
                        msgc += lista[Rempla]    #Asignar a la lista msgc la nueva letra 
                    else:
                        msgc += msg              #En caso de que el caracter no este definido en la lista original no se le hace cambios.
                        
                else:
                    if msg in Lista_M:
                        Rempla = Lista_M.find(msg) #Buscar posicion del elemento en la lista definida
                        Rempla += salto
                        while True:
                            if Rempla >= len(Lista_M): #Analizar si el nuevo numero de posición supera la cantidad de elemtos que tiene la lista inicial
                                Rempla -= len(Lista_M) #A la nueva posición restarle la cantidad de elementos de la lista original
                                continue
                            else:
                                break
                        msgc += Lista_M[Rempla]    #Asignar a la lista msgc la nueva letra
                    else:
                        msgc += msg       
        messagebox.showinfo("Mensaje codificado",msgc)
    
    
    elif varopcion.get() == 2:
        
        if yn.get() == 0:
            try:
                salto = salt.get()
                salto = int(salto) 
            except:
                messagebox.showerror("Error", "El salto debe ser un número entero")
                return

            for msg in Msg: #Pasar cada letra del mensaje principal
                            if msg == msg.lower(): #Evaluar si el datos está en minuscula
                                if msg in lista:   #Buscar si la letra del mensaje principal está en la lista definida inicialmente
                                    Rempla = lista.find(msg) #Buscar posicion del elemento en la lista definida 
                                    Rempla -= salto          #Asignar el nuevo numero de posicion
                                    if Rempla >= len(lista): #Analizar si el nuevo numero de posición supera la cantidad de elemtos que tiene la lista inicial
                                        Rempla -= len(lista) #A la nueva posición restarle la cantidad de elementos de la lista original
                                    
                                    while True:
                                        if Rempla < 0 : #Analizar si el nuevo numero de posición supera la cantidad de elemtos que tiene la lista inicial
                                            Rempla += len(lista)
                                            continue
                                        else: 
                                            break   
                                        
                                    msgc += lista[Rempla]    #Asignar a la lista msgc la nueva letra 
                                else:
                                    msgc += msg              #En caso de que el caracter no este definido en la lista original no se le hace cambios.
                            
                            
                            
                            else:
                                if msg in Lista_M: #Buscar si la letra del mensaje principal está en la lista definida
                                    Rempla = Lista_M.find(msg) #Buscar posicion del elemento en la lista definida
                                    Rempla -= salto         #Asignar el nuevo numero de posicion
                                    if Rempla >= len(Lista_M): #Analizar si el nuevo numero de posición supera la cantidad de elemtos que tiene la lista inicial
                                        Rempla -= len(Lista_M) #A la nueva posición restarle la cantidad de elementos de la lista original
                                    
                                    while True:
                                        if Rempla < 0 : #Analizar si el nuevo numero de posición supera la cantidad de elemtos que tiene la lista inicial
                                            Rempla += len(Lista_M)
                                            continue
                                        else:
                                            break 
                                    msgc += Lista_M[Rempla]   #Asignar a la lista msgc la nueva letra
                                else:
            
                                    msgc += msg
            messagebox.showinfo("Mensaje descodificado",msgc)

        else:

            raiz1 = Tk() 
            raiz1.title("Resultados")
            La = Label(raiz1,text="Resultados:",font=("Comic Sans",14))
            La.pack()
            text = Text(raiz1, width=50)
            text.pack()
                    
            for salto in range(len(lista)-1,0,-1):  #Probar la cantidad de saltos posibles con el fin de realizar un ataque de fuerza bruta
                    msgc =""
                    
                    
                    for msg in Msg:
                            
                            
                            if msg == msg.lower(): #Evaluar si el datos está en minuscula
                                    if msg in lista:  #Buscar si la letra del mensaje principal está en la lista definida inicialmente
                                        Rempla = lista.find(msg) #Buscar posicion del elemento en la lista definida
                                        Rempla -= salto         #Asignar el nuevo numero de posicion
                                        if Rempla >= len(lista): #Analizar si el nuevo numero de posición supera la cantidad de elemtos que tiene la lista inicial
                                            Rempla -= len(lista) #A la nueva posición restarle la cantidad de elementos de la lista original
                                        
                                        while True:
                                            if Rempla < 0 : #Analizar si el nuevo numero de posición supera la cantidad de elemtos que tiene la lista inicial
                                                Rempla += len(lista)
                                                continue
                                            else: 
                                                break
                                        msgc += lista[Rempla]   #Asignar a la lista msgc la nueva letra
                                    else:
                                        msgc += msg             #En caso de que el caracter no este definido en la lista original no se le hace cambios.
                                
                                    
                            else:
                                    if msg in Lista_M:
                                        Rempla = Lista_M.find(msg)
                                        Rempla -= salto
                                        if Rempla >= len(Lista_M):
                                            Rempla -= len(Lista_M)
                                        
                                        while True:
                                            if Rempla < 0 : #Analizar si el nuevo numero de posición supera la cantidad de elemtos que tiene la lista inicial
                                                Rempla += len(lista)
                                                continue
                                            else: 
                                                break
                                        
                                        
                                        msgc += Lista_M[Rempla]
                                    else:
                                        msgc += msg
                    text.insert(1.0,f" El mensaje probable # {salto} : {msgc} ")

                        




Boton = Button(frame3,text="Generar texto",command = por)
Boton.pack()



root.mainloop()
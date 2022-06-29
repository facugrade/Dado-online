import random as rm
import tkinter as tk


def sd():
    Numero_del_dado.config(text=rm.randint(1,8))

#Creacion de la ventana
ventana = tk.Tk ()
ventana.title("DADO")
ventana.config(width=400, height=300)
#Cierre de creacion de ventana

#Boton
giro = tk.Button(text="CLICK PARA GIRAR EL DADO!!", command=sd)
giro.place(x=110 , y=150, width=170, height=45)
#Cierre del boton

#Seteo del dado
Numero_del_dado = tk.Label()
Numero_del_dado.place(x=180, y=100)
#Seteo del dado

#expli
texto1 = tk.Label(text="7 = tira denuevo 8 = perdes un turno")
texto1.place(x=110, y=200)
#expli cierre



ventana.mainloop()

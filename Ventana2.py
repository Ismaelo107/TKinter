import tkinter as tk


root = tk.Tk()

# Creamos ventana

def crear_ventana():
    root.geometry("300x300+3+3")
    root.title("Esta es mi ventana")

def crear_etiqueta(title, fila, columna):
    etiqueta = tk.Label(root,text=title)
    etiqueta.grid(row=fila,column=columna)

def crear_cuadroTexto(fila, columna):
    texto = tk.Entry(root)
    texto.grid(row=fila,column=columna)
    texto.get()

def crear_boton(textoBoton,fila,columna):
    boton = tk.Button(root,text=textoBoton)
    boton.grid(row=fila,column=columna)

# __main__
crear_ventana()
crear_etiqueta("Usuario:", 0, 0)
crear_cuadroTexto(0,1)

crear_etiqueta(" Contraseña:", 1, 0)
crear_cuadroTexto(1,1)

crear_boton("LogIN",3,1)
crear_boton("SingUP",3,2)

root.mainloop()

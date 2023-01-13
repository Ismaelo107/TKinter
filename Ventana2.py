import tkinter as tk

root = tk.Tk()


# Creamos ventana root
def crear_root(ventana):

    root.geometry("300x300+3+3")
    root.title(titulo)
    crear_etiqueta("Usuario:", 0, 0)
    crear_cuadroTexto(0, 1)

    crear_etiqueta(" Contraseña:", 1, 0)
    crear_cuadroTexto(1, 1)

    crear_boton("LogIN", 3, 1, funcion_boton_iniciar)
    crear_boton("SingUP", 3, 2, funcion_boton_registrar)

def cerrar_ventana(ventana):
    ventana.destroy()

#Creamos etiquetas
def crear_etiqueta(title, fila, columna):
    etiqueta = tk.Label(root,text=title)
    etiqueta.grid(row=fila,column=columna)

def crear_cuadroTexto(fila, columna):
    texto = tk.Entry(root)
    texto.grid(row=fila,column=columna)
    texto.get()

def crear_boton(textoBoton,fila,columna,funcion):
    boton = tk.Button(root,text=textoBoton, command=funcion)
    boton.grid(row=fila,column=columna)





# __main__
crear_root(root)




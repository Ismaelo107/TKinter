import tkinter as tk

root = tk.Tk()


def crear_etiqueta(ventana,texto, fila, columna):
    etiqueta = tk.Label(ventana, text=texto)
    etiqueta.grid(row=fila, column=columna)


def crear_boton(ventana,textoBoton, fila, columna, funcion):
    boton = tk.Button(ventana, text=textoBoton, command=funcion)
    boton.grid(row=fila, column=columna)

def crear_cuadroTexto(ventana,fila, columna,contenido):
    texto = tk.Entry(ventana,textvariable=contenido)
    texto.grid(row=fila,column=columna )



def registrar():
    root.destroy()
    child1 = tk.Tk()
    child1.title("Ventana de Registro")
    child1.geometry("500x500+0+0")
    crear_etiqueta(child1,"Nombre: ",0,0)
    crear_etiqueta(child1,"Apellidos: ",1,0)
    crear_etiqueta(child1,"Correo: ",2,0)
    crear_cuadroTexto(child1,0,1,"nombre")
    crear_cuadroTexto(child1,1,1,"apellidos")
    crear_cuadroTexto(child1,2,1,"correo")
    crear_boton(child1,"Listo!",10,10)


    child1.mainloop()


def crear_root():
    root.title("Ventana1")
    root.geometry("500x500+0+0")
    crear_etiqueta(root," ", 0, 6)
    crear_etiqueta(root,"Bienvenido a la Página Principal", 7, 17)
    crear_boton(root,"Iniciar Sesión", 10, 8, "")
    crear_etiqueta(root,"¿Tienes Cuenta?", 10, 7)
    crear_boton(root,"¡Registrate!", 11, 8, registrar)
    crear_etiqueta(root,"¡Si no es así!", 11, 7)
    root.mainloop()


# __main__

crear_root()

import tkinter as tk

root = tk.Tk()
root.title("Iniciar sesión")

label_username = tk.Label(root, text="Nombre de usuario")
label_password = tk.Label(root, text="Contraseña")
entry_username = tk.Entry(root)
entry_password = tk.Entry(root, show="*")
button_login = tk.Button(root, text="Iniciar sesión")

label_username.grid(row=0, column=0)
label_password.grid(row=1, column=0)
entry_username.grid(row=0, column=1)
entry_password.grid(row=1, column=1)
button_login.grid(row=2, column=1)

root.mainloop()

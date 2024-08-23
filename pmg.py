import tkinter as tk
from tkinter import messagebox

# Función para mostrar la ventana de inicio de sesión
def login():
    def check_credentials():
        username = username_entry.get()
        password = password_entry.get()
        # Aquí puedes reemplazar con tus credenciales reales
        if username == "user" and password == "pass":
            login_window.destroy()
            open_calculator()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

    login_window = tk.Tk()
    login_window.title("Login")
    
    # Estilo de ventana de inicio de sesión
    login_window.configure(bg="#2e3b4e")
    
    tk.Label(login_window, text="Username", bg="#2e3b4e", fg="white", font=("Arial", 14)).pack(pady=5)
    username_entry = tk.Entry(login_window, font=("Arial", 14))
    username_entry.pack(pady=5)
    
    tk.Label(login_window, text="Password", bg="#2e3b4e", fg="white", font=("Arial", 14)).pack(pady=5)
    password_entry = tk.Entry(login_window, show="*", font=("Arial", 14))
    password_entry.pack(pady=5)
    
    tk.Button(login_window, text="Login", command=check_credentials, bg="#4caf50", fg="white", font=("Arial", 14), width=15).pack(pady=10)
    
    login_window.mainloop()

# Función para abrir la calculadora
def open_calculator():
    calculator = tk.Tk()
    calculator.title("Calculator")

    # Estilo de ventana de calculadora
    calculator.configure(bg="#3c3c3c")
    
    display = tk.Entry(calculator, bd=5, relief="ridge", font=("Arial", 20), justify="right", bg="#fff", fg="#000")
    display.grid(row=0, column=0, columnspan=4, pady=10, padx=10, sticky="nsew")

    def press(key):
        current = display.get()
        display.delete(0, tk.END)
        display.insert(tk.END, current + key)
    
    def calculate():
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception:
            messagebox.showerror("Error", "Invalid input")
    
    def clear():
        display.delete(0, tk.END)
    
    # Botones de la calculadora
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ]
    
    for (text, row, col) in buttons:
        if text == '=':
            b = tk.Button(calculator, text=text, command=calculate, width=5, height=2, bg="#4caf50", fg="white", font=("Arial", 14))
        else:
            b = tk.Button(calculator, text=text, command=lambda t=text: press(t), width=5, height=2, bg="#333", fg="white", font=("Arial", 14))
        b.grid(row=row, column=col, padx=5, pady=5)
    
    tk.Button(calculator, text='C', command=clear, width=5, height=2, bg="#f44336", fg="white", font=("Arial", 14)).grid(row=5, column=0, columnspan=4, pady=5)
    
    # Configuración de las columnas y filas para que se ajusten
    for i in range(4):
        calculator.columnconfigure(i, weight=1)
    for i in range(6):
        calculator.rowconfigure(i, weight=1)
    
    calculator.mainloop()

# Inicia el programa mostrando la ventana de inicio de sesión
login()

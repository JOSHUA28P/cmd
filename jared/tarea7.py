#crear un programa que calcule la suma, la resta, la multiplicacion, division utilizandolos metodos para cada  operacion(POO)  y que tenga login 

class Calculator:
    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b
    def multiply(self, a, b): return a * b
    def divide(self, a, b): return a / b if b != 0 else "Error, División por cero"

class Authentication:
    def __init__(self):
        self.users = {"jared": "123"}  

    def login(self, username, password):
        return self.users.get(username) == password

def main():
    auth = Authentication()
    calc = Calculator()

    username = input("Nombre de usuario: ")
    password = input("Contraseña: ")

    if auth.login(username, password):
        print("Iniciaste seccion.")
        while True:
            print("\n1. Sumar")
            print("\n2. Restar")
            print("\n3. Multiplicar")
            print("\n4. Dividir")
            print("\n5. Salir")                                        
            choice = input("Opción: ")
            if choice == '5': break

            if choice in ['1', '2', '3', '4']:
                num1 = float(input("Primer número: "))
                num2 = float(input("Segundo número: "))

                if choice == '1': print(f"Resultado: {calc.add(num1, num2)}")
                elif choice == '2': print(f"Resultado: {calc.subtract(num1, num2)}")
                elif choice == '3': print(f"Resultado: {calc.multiply(num1, num2)}")
                elif choice == '4': print(f"Resultado: {calc.divide(num1, num2)}")
            else:
                print("Opción no válida.")
    else:
        print("Usuario o contraseña incorrectos.")

if __name__ == "__main__":
    main()

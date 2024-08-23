### Crear un programa que tenga como clases personas y tenga caracteristicas, atributos, nombre,  apellidos y edad de la persona. implementar los metodos necesarios para inicializar los atributos y mostrar en pantalla los datos e indicar si la persona es mayor de edad o no. 


#creamos nuestra clase

class Persona:
        
 #inicializar los atributos
    def inicializar(self,nombre,apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

#imprimir datos
    def imprimir(self):
        print("nombre: " , self.nombre)
        print("Apellido: ", self.apellido)
        print("Edad: ", self.edad)
 #Comprobar la edad si es mayor(metodo si es mayor de edad)
    def mayor_edad(self):
            if self.edad>=18:
                print("es mayor de edad")
            else:
                print("no es mayor de edad")    

#creamos los atributos
atributo_persona = Persona()
atributo_persona.inicializar("Eren","rojas",22 )
atributo_persona2 = Persona()
atributo_persona2.inicializar("Miksa","lopez",25 )
atributo_persona = Persona()
atributo_persona.inicializar("choperr", "monky", 100 )

 #imprimir
 
atributo_persona.imprimir()
atributo_persona.mayor_edad()
atributo_persona2.imprimir()
atributo_persona2.mayor_edad()


        


        
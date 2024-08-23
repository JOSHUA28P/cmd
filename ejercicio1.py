
class Persona:
        
    def inicializar(self,nombre,apellido,edad,curso):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.curso = curso

    def imprimir(self):
        print("nombre: " , self.nombre)
        print("Apellido: ", self.apellido)
        print("Edad: ", self.edad)
        print("curso: ", self.curso)
 
 
 #Comprobar si aprobo o no aprobo
    def aprobo(self):
            if self.curso>=20:
                print("aprobo la materia")
            else:
                print("no aprobo la materia")    

atributo_persona = Persona()
atributo_persona.inicializar("curso",22 )
atributo_persona2 = Persona()
atributo_persona2.inicializar("Miksa","lopez",25 )
atributo_persona = Persona()
atributo_persona.inicializar("choperr", "monky", 18 )
atributo_persona = Persona()
atributo_persona.inicializar("edad",22 )
 

atributo_persona.imprimir()
atributo_persona.aprobo()
atributo_persona2.imprimir()
atributo_persona2.aprobo()
        


        
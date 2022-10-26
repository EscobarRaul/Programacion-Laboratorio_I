class Persona:
    def __init__(self,id):
        self.id = id
    def mostar(self):
        print(self.id)
    def get_id(self):
        return self.id
        
class Personaje(Persona):
    def __init__(self,nombre=""):
        super().__init__(88)
        self.__nombre = nombre
        self.apellido = ""
        self.lista = ["HOLA","PEPE"]
        
    def get_id(self):
        
        return super().get_id()

    @property
    def edad(self): #Getter
        return self.calcular_edad()

    @property
    def nombre(self): #Getter
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

    def __str__(self):
        return self.__nombre + "HOLA"

    def __len__(self):
        return 8

    def __getitem__(self,index):
        if index == "nombre":
            return self.__nombre 
        else:
            return ""

    def __getitem__(self,index,valor):
        if index == "nombre":
            self.__nombre = valor
        else:
            return ""

    def __iter__(self):
        for i in self.lista:
            yield i #Hace un return pero conserva la posicion en la que se encontraba
        
aux = Personaje("Vero")         
#ITER
contador = 0
for elemento in aux:
    contador +=1
    print(elemento)
print(contador)
    

#SETITEM
# aux = Personaje("Vero")
# aux["nombre"] = "JUAN"
# print(aux["nombre"])

#GETITEM
# aux = Personaje("Vero")
# print(aux["nombre"])
# print(aux.nombre)

#LEN
# aux = Personaje("Vero")
# print(len(aux))

#STR    
# aux = Personaje("Vero")
# print(aux)

#GETTER  
# aux = Personaje("Vero")
# print(aux.nombre)
# aux.nombre = "Juan"


# aux_personaje1 = Personaje("")   
# aux_personaje2 = Personaje("Juana")
# aux_personaje2.mostar() #COMO LLAMAR A UN METODO
# aux_personaje1.mostar()

print(aux.get_id())
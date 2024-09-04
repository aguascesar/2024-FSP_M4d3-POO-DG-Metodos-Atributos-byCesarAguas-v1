# * my_pizza v1 (https://github.com/aguascesar/2024-FSP_M3d14-EstrDatosFunc-DF-Estructuras2-byCesarAguas-v1)
# * Copyright 2024 Cesar Aguas
# * Licensed under AGPL3.0 (https://github.com/aguascesar/2024-FSP_M3d14-EstrDatosFunc-DF-Estructuras2-byCesarAguas-v1/LICENSE)
#  
#   1 - En el archivo pizza.py, crear una clase que permita crear objetos de tipo Pizza.
#Considerar qué atributos de clase debe contener la clase, según la descripción del
#problema.
import ingredientes as i
class Pizza:
    precio = 10000
    tipos_masa = i.masas()
    proteicos = i.proteicos()
    vegetales = i.vegetales()


    #  2 - Agregar un método que permita validar un elemento dentro de una lista de casos posibles. 
    #Este método se debe poder utilizar sin necesidad de crear un objeto de la clase, 
    #y debe recibir 2 argumentos:
    #a. El elemento a validar (un texto).
    #b. Los valores posibles a considerar para el elemento ingresado (una lista de textos).    
    @staticmethod
    def encontrar(elemento,lista_de_casos):
    #   En caso de que el elemento ingresado como primer argumento se encuentre entre la
    #lista de valores posibles ingresada como segundo argumento, el método debe retornar
    #True. En caso contrario, debe retornar False.   
        return elemento in lista_de_casos
    
    #   3 - En el mismo archivo y clase del requerimiento anterior, agregar un método que permita
    #realizar un pedido. Para ello, dentro de la definición de este método, debe solicitar al
    #usuario ingresar el ingrediente proteico, luego el primer ingrediente vegetal, luego el
    #segundo ingrediente vegetal, y finalmente el tipo de masa. Cada ingreso debe
    #almacenarse (o añadirse, si corresponde) en un atributo de la instancia.
    def pedido(self):
        print(f"Por favor ingrese la siguiente informacion.")
        print()
        self.sel_masa = str(input("Masa [tradicional/delgada]: ")).lower()             
        self.proteico_1  = str(input("Ing. proteico [pollo/vacuno/carne vegetal]: ")).lower()
        self.vegetal_1 = str(input("Ing. vegetal [tomate/aceitunas/champiñones]: ")).lower()                        
        self.vegetal_2 = str(input("Ing. vegetal [tomate/aceitunas/champiñones]: ")).lower()
        
        masa = self.encontrar(self.sel_masa,self.tipos_masa)
        proteico = self.encontrar(self.proteico_1,self.proteicos)
        vegetal1 = self.encontrar(self.vegetal_1,self.vegetales)
        vegetal2 = self.encontrar(self.vegetal_2,self.vegetales)
        #   4 - Dentro del mismo método del requerimiento 3, una vez asignados los valores a los
        #atributos de la instancia, debe evaluarse si se trata de un ingreso válido (considerar la
        #información de la descripción), usando el método del requerimiento 2. Si los 3
        #ingredientes y el tipo de masa son válidos, deberá almacenar en un atributo el valor
        #True. En caso contrario, deberá almacenar el valor False. Este atributo permitirá saber
        #si una instancia específica es o no una Pizza válida.
        if masa and proteico and vegetal1 and vegetal2:
            self.validacion = True
        else:
            self.validacion = False

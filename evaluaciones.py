from pizza import Pizza

#   A - Usar la función print(), para que al ejecutar el script se muestre en pantalla los
#valores de los atributos de clase de la clase importada, sin crear una instancia
#de ella.

print(f'''
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|                    JAT Pizza                       |
|                                                    |
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|                                                    |
|                    Bienvenido                      |
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|                                                    | 
|Tenemos las siguientes Masas disponibles:           |
|                                                    |
|{Pizza.tipos_masa}                          |
|                                                    |
|Algunos ingredientes adicionales:                   |
|Proteicos : {Pizza.proteicos}    |
|Vegetales : {Pizza.vegetales}  |
|                                                    |
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|El precio de la pizza: {Pizza.precio}                        |
|                                                    |
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')
#   B - Usar la función print(), para que al ejecutar el script se muestre en pantalla
#si el elemento “salsa de tomate” se encuentra presente en la lista [“salsa de
#tomate", "salsa bbq"]. Para ello use el método creado en el requerimiento
#2, sin crear una instancia de la clase importada.
print(f"El elemento salsa de tomate {'si' if Pizza.encontrar('salsa de tomate', ['salsa de tomate', 'salsa bbq']) else 'no'} se encuentra presente en la lista\n ")


#   C - Crear una instancia de la clase importada, 
solicitud_pizza = Pizza()
#y luego llamar al método del requerimiento 3, 
#para que al ejecutar el script se solicite ingredientes y tipo de masa al usuario.
solicitud_pizza.pedido()

#   D - Usar la función print(), para que al ejecutar el script, luego de que el usuario
#haya ingresado los ingredientes y tipo de masa, se muestre en pantalla los
#ingredientes vegetales, el ingrediente proteico y el tipo de masa de la instancia
#creada en el paso anterior, y si esa instancia es una pizza válida o no.
print(f'''
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|                                                    | 
|Su seleccion:                                       |
|Tipo de masa: {solicitud_pizza.sel_masa}                         |
|                                                    |
|Sus ingredientes adicionales:                      |
|Proteicos : {solicitud_pizza.proteico_1}            |
|Vegetales : {solicitud_pizza.vegetal_1}             |
|            {solicitud_pizza.vegetal_2}             |
|                                                    |
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|Su solicitud de la Pizza {'es' if solicitud_pizza.validacion else 'no es'} válida                  |
|                                                    |
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

''')


#   E - Usar la función print(), para mostrar en pantalla si la clase Pizza es una pizza
#válida o no, haciendo uso del atributo creado en el requerimiento 4, sin crear
#una instancia de la clase. En este punto, la ejecución del script debe mostrar
#un error (todos los pasos anteriores se deben haber ejecutado correctamente).
if Pizza.validacion:
    print("La clase Pizza representa una pizza válida.")
else:
    print("La clase Pizza no representa una pizza válida.")
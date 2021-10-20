#Diccionarios 
#Mapeos desordenados para guardar objetos 
#Los diccionarios utilizan un order basado en par Clave/Valor
#Este para Clave/Valor permite al usuario agarrar objetos sin necesidad de saber la locacion(numero) de indice

#Diccionarios usan brackets {} y: para simbolizar las llaves y su valor asociado 
#Cuando deberiamos escoger una lista o un diccionario? 
#Dic : Objetos retornados por llave 
#  -Desordenados y no se guarda, bueno para cuando no sabes donde se encuentra algo 
#Listas: Objetos retornados por locacion
#  - Puede ser Indice o Slicing 
my_diccionario={'manzanas':'2.90','agua':'2.9','leche':'5.9'}
print(my_diccionario['manzanas'])

my_diccionario={'manzanas':'2.90','kekes':['manzana','platano'],'leche':'5.9'}
print(my_diccionario)

#agregar mas datos
my_diccionario['gaseosa']=20
print(my_diccionario)
#ver llaves 
print(my_diccionario.keys())
#valores
print(my_diccionario.values())



#TUPLAS 
#Las tuplas son similares a las listas. Sin embargo, tienen una diferencia - INMUTABILIDAD 
#Una vez que un element se encuentra en una tupla, este no puede ser re-asignado
#Las tuplas usan parentesis (1,2,3)

t=(1,2,3)
lista=[1,2,3]
print(type(t))
#contar las tuplas 
print(t.count(1))
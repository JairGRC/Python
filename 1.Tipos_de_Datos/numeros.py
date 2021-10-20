a=4+4  
b=4.5+4.56
print(a+b)

#modulos
a=7%4
print(a)

#variables 
vida= 100
dano = 35
print(type (vida))

#Cadena de Texto 
print("Hola \n mundo")
#len devuelve longitud 
print(len("Hola"))



micadena="Hola mundo"
print(micadena[3])
#indexado inverso 
print(micadena[-2])
#resultado: d

#Slicing permite agarrar una subseccion de multiples caracteres, un "slice" de una cadena
#Sintaxis [start:stop:step]->[0:4:2]
"""
Start es un indice numeric para el slice iniciar
Stop es el numero donde paramos el slice 
Step son los pasos que damos
"""
print(micadena[0:7:2])
#resultado: Hl u
x='Hola Mundo'
#mayusculas
x=x.upper()
print(x)
#minusculas
x=x.lower()
print(x)
#separar palabras - tambien funciona con letras por ejm: split('letra')
x=x.split()
print(x)
#resultado: ['Hola','Mundo']

#FORMATO DE IMPRESION DE CADENAS DE TEXTO 
print('Esta {} {} {} {}'.format('es','una','cadena','texto'))

print('Esta {e} {u} {r} {t}'.format(e='es',u='una',r='cadena',t='texto'))

#Formateo de float "{valor:width.precision f}"
resultados=100/888
print("Los resultado son {r:1.3f}".format(r=resultados))

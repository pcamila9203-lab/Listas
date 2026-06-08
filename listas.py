# lista = [1,2,3]
# lista.append(4) para agregar al final lo que esta entre parentecis 
#lista.pop (es para eliminar lista)
# print(lista)
# notas=[]
# ramos=[]
# for i in range(3):
#     ramo= input("ingrese su ramo: ")
#     nota= float(input("Ingrese nota: "))
#     ramos.append(ramo) #esto es para que el usuario ingrese el ramo
#     notas.append(nota) #esto es para que el usuario ingrese la nota 

# print(ramos) #para que imprima las listas se debe imprimir el nombre que le dejo al string lista
# print(notas)

ramos = ['algorismo', 'ingles', 'tic']
notas = [63.0, 65.0, 65.0]

#print(notas [1:2]) cuenta desde la nota 1 a las 2 (65 y 65 )
#print(notas[:2]) #muestras las que estan antes que el 2 
#print (notas[1:]) muestra las que estan despues del 1

# for i in range(len(notas)): #el len te ayuda contar 
#     print (i , notas[i]) #este for es para mostar con posicion las notas 0 63

# print(len(notas)) # te da cuantos elementos tienes 
# print(max(notas)) # te imprime la nota maxima 
# print(min(notas)) #te imprime la nota minima 
#print(round(sum(notas)/ len(notas),)) # te muestras el promedio de la lista 

# for i in range(len(ramos)): #i toma 0123 y el len lee la cantidad de ramos
#     print(ramos[i]) #te lee la lista de ramos muestra todos los ramos 

#for i in range(len(notas)): #i toma 0123 y el len lee la cantidad de ramos
#print(max(notas))

print(notas.index(65)) #muestra la posicion 
print(ramos[notas.index(max(notas))]) #muestra la posicion de la nota y el nombre del ramos 
print("Paula ")
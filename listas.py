# # 1. Control de asistencia
# #  a) Agregue un nuevo estudiante ingresado por teclado al final de la lista.
# # b) Muestre cuántos estudiantes asistieron.
# # c) Ordene alfabéticamente la lista y la muestre.

# asistencia = ["Ana", "Carlos", "Elena", "Tomás"] 
# nombre = input("Ingrese su nombre: ")
# asistencia.append(nombre)

# print("Asistieron",len(asistencia), "estudiante")
# asistencia.sort()
# print(asistencia)
# print("probando")



# # 2. Inventario de una tienda
# # a) Muestre el stock total.
# # b) Indique cuál es el producto con mayor stock y cuál con menor stock.
# # c) Agregue un nuevo valor de stock ingresado por teclado.

# stock = [15, 8, 23, 12, 5]

# print("El stock total es de: ", sum(stock))
# print("el mayor stock en la tienda es de:",max(stock))
# print("El menor stock en la tienda es de,",min(stock))
# cantidad= input("Ingrese un stock: ")
# stock.append(cantidad)


# # 3. Lista de espera de una consulta médica
# # a) Muestre el primer paciente atendido (elimínelo de la lista).
# # b) Agregue un paciente urgente en la primera posición.
# # c) Muestre la lista actualizada.

# pacientes = ["María", "Pedro", "Sofía", "Luis"]

# print(pacientes[0])
# pacientes.pop(0)
# print(pacientes)
# nv_paciente = input("nombre de paciente por urgencia: ")
# pacientes.insert(0,nv_paciente)
# print(pacientes)


# # 4. Notas de una evaluación
# # a) Muestre la nota más alta y la más baja.
# # b) Calcule la suma de todas las notas.
# # c) Muestre las notas ordenadas de menor a mayor sin modificar la lista
# # original.

# notas = [5.4, 6.2, 4.8, 5.9, 3.7]

# print(max(notas))
# print(min(notas))
# print(round(sum(notas)/ len(notas)))
# notas_ordenadas = sorted(notas)
# print("Orden de notas de menor a mayor: ", notas_ordenadas)
# print("Lista original: ", notas)

# # 5. Carrito de compras
# # a) Agregue un nuevo precio ingresado por teclado.
# # b) Elimine el último producto agregado.
# # c) Muestre el total de la compra y la cantidad de productos.

# precios = [2500, 1800, 3200, 1500]
# nuevo_precio = int(input("Ingrese un precio: "))
# precios.append(nuevo_precio)
# print(precios)
# precios.pop(4)
# print(precios)
# print("El total es de ",sum(precios))
# print("La cantidad de productos fueron: ",len(precios))

# # 6. Ranking de puntajes
# #  a) Ordene los puntajes de mayor a menor.
# # b) Muestre el puntaje máximo y el mínimo.
# # c) Indique cuántos puntajes hay registrados.


# puntajes = [1200, 850, 2300, 1750, 980]

# print("Los putajes son: ",puntajes)
# punajes_ordenados = sorted(puntajes, reverse=True)
# print("El orden de mayor a menor de los puntajes son: ", punajes_ordenados)
# print("El puntaje max fue: ",max(puntajes))
# print("El puntaje min fue: ",min(puntajes))
# print("La cantidad de puntajes fueron: ", len(puntajes))

# # 7. Biblioteca escolar
# # a) Agregue un nuevo libro al final.
# # b) Elimine un libro cuyo nombre sea ingresado por teclado.
# # c) Muestre la lista ordenada alfabéticamente.

# libros = ["El Principito", "1984", "Drácula", "Harry Potter"]
# nuev_libro = input("Ingrese un libro: ")
# libros.append(nuev_libro)
# print(libros)
# libros.pop(4)
# print(libros)
# libros.sort()
# print(libros)

# print("Miercoles 10")
# print("Proximo ejercicio a conticuación")

# # 8. Registro de temperaturas
# # a) Muestre la temperatura más alta y la más baja.
# # b) Calcule la suma de todas las temperaturas.
# # c) Indique cuántos días fueron registrados.


# temperaturas = [18, 20, 17, 22, 19, 21, 16]

# print("Temperatura alta: ", max(temperaturas))
# print("Temperaura baja: ", min(temperaturas))
# print("El total de las temperaturas es: ", sum(temperaturas))
# print("El total de días fueron: ", len(temperaturas))

# # 9. Cola de atención en un banco
# # a) Atienda al primer cliente (elimínelo de la lista).
# # b) Agregue un nuevo cliente al final.
# # c) Muestre la cantidad de clientes que quedan esperando.


# clientes = ["José", "Patricia", "Camila", "Felipe"]

# print("Clientes por atender son: ",clientes)
# print("Primer cliente atendido: ",clientes[0])
# clientes.pop(0)
# print(clientes)
# clientes.append("Juanita")
# print(clientes)
# print("Quedan: ",len(clientes),"clientes")

# 10. Gastos mensuales
# a) Muestre el gasto total del período.
# b) Indique el gasto mayor y el menor.
# c) Agregue un nuevo gasto ingresado por teclado.
# d) Muestre los gastos ordenados de menor a mayor.

# gastos = [12000, 8500, 23000, 15000, 9800]

# print("El gasto total es: ", sum(gastos))
# print("E gasto mayor fue: ",max(gastos))
# print("El menor gasto fue: ",min(gastos))
# nuevo_gasto = int(input("Ingrese un nuevo gasto: "))
# gastos.append(nuevo_gasto)
# gastos.sort()
# print(gastos)

# Desafío Integrador: Administración de un cine
# Construya un programa que permita realizar las siguientes acciones:
# 1. Agregar las ventas de un nuevo día.
# 2. Eliminar el último día registrado.
# 3. Mostrar la cantidad de días registrados.
# 4. Mostrar el total de entradas vendidas.
# 5. Mostrar el día con mayor y menor cantidad de ventas.
# 6. Mostrar una copia de las ventas ordenadas de menor a mayor.
# 7. Finalmente, ordenar la lista original y mostrarla.

ventas = [120, 95, 150, 80, 110]
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
print(ventas)
venta_nueva = int(input("Ingrese las ventas del dias: "))
ventas.append(venta_nueva)
ventas.pop(4)
print(ventas)
print("Los dias registrados fueron", len(ventas))
print("El total es de: ", sum(ventas))
print(f"El dia {dias[ventas.index(max(ventas))]} con {max(ventas)} ventas fue la mayor")
print(f"El dia {dias[ventas.index(min(ventas))]} con {min(ventas)} ventas fue la menor")
print(f"Las listas original es: ", zip({dias(ventas)}))




#diccionario explicado de la profesora:
# ventas={"Lunes": 120,
#         "Martes": 95,
#         "Miercoles": 150,
#         "Jueves": 80,
#         "Viernes":110}

# for llave in ventas:
#     print(llave, ventas[llave])

# lista = [1,3,5,7]
# for elemento in lista:
#     print(elemento)
#     palabra = "Paula"

# for caracter in palabra:
#     print(caracter)



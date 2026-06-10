# 1. Control de asistencia
#  a) Agregue un nuevo estudiante ingresado por teclado al final de la lista.
# b) Muestre cuántos estudiantes asistieron.
# c) Ordene alfabéticamente la lista y la muestre.

asistencia = ["Ana", "Carlos", "Elena", "Tomás"] 
nombre = input("Ingrese su nombre: ")
asistencia.append(nombre)

print("Asistieron",len(asistencia), "estudiante")
asistencia.sort()
print(asistencia)
print("probando")



# 2. Inventario de una tienda
# a) Muestre el stock total.
# b) Indique cuál es el producto con mayor stock y cuál con menor stock.
# c) Agregue un nuevo valor de stock ingresado por teclado.

stock = [15, 8, 23, 12, 5]

print("El stock total es de: ", sum(stock))
print("el mayor stock en la tienda es de:",max(stock))
print("El menor stock en la tienda es de,",min(stock))
cantidad= input("Ingrese un stock: ")
stock.append(cantidad)


# 3. Lista de espera de una consulta médica
# a) Muestre el primer paciente atendido (elimínelo de la lista).
# b) Agregue un paciente urgente en la primera posición.
# c) Muestre la lista actualizada.

pacientes = ["María", "Pedro", "Sofía", "Luis"]

print(pacientes[0])
pacientes.pop(0)
print(pacientes)
nv_paciente = input("nombre de paciente por urgencia: ")
pacientes.insert(0,nv_paciente)
print(pacientes)


# 4. Notas de una evaluación
# a) Muestre la nota más alta y la más baja.
# b) Calcule la suma de todas las notas.
# c) Muestre las notas ordenadas de menor a mayor sin modificar la lista
# original.

notas = [5.4, 6.2, 4.8, 5.9, 3.7]

print(max(notas))
print(min(notas))
print(round(sum(notas)/ len(notas)))
notas_ordenadas = sorted(notas)
print("Orden de notas de menor a mayor: ", notas_ordenadas)
print("Lista original: ", notas)

# 5. Carrito de compras
# a) Agregue un nuevo precio ingresado por teclado.
# b) Elimine el último producto agregado.
# c) Muestre el total de la compra y la cantidad de productos.

precios = [2500, 1800, 3200, 1500]
nuevo_precio = int(input("Ingrese un precio: "))
precios.append(nuevo_precio)
print(precios)
precios.pop(4)
print(precios)
print("El total es de ",sum(precios))
print("La cantidad de productos fueron: ",len(precios))

# 6. Ranking de puntajes
#  a) Ordene los puntajes de mayor a menor.
# b) Muestre el puntaje máximo y el mínimo.
# c) Indique cuántos puntajes hay registrados.


puntajes = [1200, 850, 2300, 1750, 980]

print("Los putajes son: ",puntajes)
punajes_ordenados = sorted(puntajes, reverse=True)
print("El orden de mayor a menor de los puntajes son: ", punajes_ordenados)
print("El puntaje max fue: ",max(puntajes))
print("El puntaje min fue: ",min(puntajes))
print("La cantidad de puntajes fueron: ", len(puntajes))

# 7. Biblioteca escolar
# a) Agregue un nuevo libro al final.
# b) Elimine un libro cuyo nombre sea ingresado por teclado.
# c) Muestre la lista ordenada alfabéticamente.

libros = ["El Principito", "1984", "Drácula", "Harry Potter"]
nuev_libro = input("Ingrese un libro: ")
libros.append(nuev_libro)
print(libros)
libros.pop(4)
print(libros)
libros.sort()
print(libros)

print("Miercoles 10")
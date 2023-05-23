#obtener un valor de la lista según su posición.
lista=[1,2,"Hola Mundo desde la lista",4,"posición 4"]

print(lista[2])#el segundo elemento de la lista
print("ultimo elemento de la lista: ",lista[-1])#el último elemento de la lista
print("El penultimo elemento",lista[-2])
#agregar un nuevo elemento a la lista
lista.append("nuevo valor agregado con append")
lista.append(51)
lista.append(52)
lista.append(53)

lista_b=[54,55,56,1]
lista.extend(lista_b)
#agregar algo en la posición [2] de la lista
lista.insert(2,"Objeto insertado en esta posición")
lista.remove("posición 4")#busca el elemento y lo borra de la lista
lista.reverse()#ordena la lista al revez
lista_b.sort()#ordena la lista de mayor a menor
lista_b.sort(reverse=True)
print("Toda la lista: ")
print(lista_b)#imprime toda la lista
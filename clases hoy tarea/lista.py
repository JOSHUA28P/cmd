#crear lista

lista = [5, 4, 7, 9, 3]
print(lista)

a =[2024, "algoritmia", 0.54]
print(a[1])
print(a[0])
print(a[2])
#indice
print(a[-1])
print(a[-2])

#modificar el valor de la lista

a[2]=12.59
print(a)

#eliminar un elemento de la lista

lista1 = [2024, 2023, 2022, 2021, 2020]
del lista1[4]
print(lista1)

#Iterar listas

lista2 = [17, 18, 19, 20]
for l in lista:
    print(l)

#
lista3 = [159, 753, 456]
for index, li in enumerate(lista3):
    print(index,li)

#Ordene los elementos de menor a mayor

lista3.sort()
print(lista3)

#Ordene los elementos de mayor a menor
lista3.sort(reverse=True)
print(lista3)
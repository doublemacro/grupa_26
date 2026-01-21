
lista3 = [3, 10, 4, 100, 35, 50, 90, 87, 99, 500, 1000, 1]
# index   0   1  2    3   4   5   6   7   8    9    10 11

print(lista3)
# lista3[1:3] -> [10, 4]
# slice syntax: list_variable[start_slice:end_slice]
print(lista3[1:4])

# faceti un slice de la mijlocul listei pana la sfarsitul listei
# ex: [3, 10, 4, 100, 35, 50, 90, 87, 99] -> [35, 50, 90, 87, 99]
# trebuie sa aflam: 1. care este mijlocul liste? 2. care este sfarsitul listei?

# n + 1 / 2
# n -> nr de elem din lista.

# // -> operator de impartire intreaga. 3 // 2 -> 1 ;    3 / 2 -> 1.5
print((len(lista3) + 1) // 2)
# mijlocul listei: (len(lista3) + 1) // 2
print(lista3[(len(lista3) + 1) // 2 : len(lista3)])

lista1 = ["apple", "orange", "banana"]
#              0         1         2
#             -3        -2        -1
lista2 = [30, 50, 100]

# lista4 -> ["apple", "orange", "banana", 30, 50, 100]

lista4 = lista1 + lista2
lista1.extend(lista2)

print(lista1)

lista1.insert(2, "banana")
print(lista1)
lista1.remove("banana")
lista1.remove("banana")

print(lista1)
print(lista1.pop())
print(lista1.pop())
print(lista1.pop())
print(lista1)

lista1.clear()

print(lista1)

print("===========Sortare============")

lista5 = [3, 10, 4, 100, 35, 50, 90, 87, 99, 500, 1000, 1]
lista5.sort()
print(lista5)

lista5.sort(reverse=True)
print(lista5)

lista5.reverse()
print(lista5)







# Intrebare 1.
# Se da urmatorul cod:

v1 = "Hello World"
#     0123456789 10
print(v1[0], v1[1], v1[-1])

# Ce se printeaza?
# 1. Eroare! Index out of bounds
# 2. "H l o"
# 3. Nimic
# 4. "H e d"

# Raspuns corect 4


# primitive data type. int
x1 = 10

def change(x1):
    x1 = 11


change(x1)
print(x1)

# Ce se printeaza?

# 1. Eroare! x1 nu a fost declarat!
# 2. 10
# 3. 11
# 4. None

# Raspuns corect 2.


# tip de date complex, intr-un fel nu e primitiv.
x2 = [10]
#      0

def change(x2):
    x2[0] = 11

change(x2)
print(x2)

# Ce se printeaza?

# 1. Eroare! Index out of bounds!
# 2. [10]
# 3. [11]
# 4. None

# Raspuns corect 3.



# tip de date complex, intr-un fel nu e primitiv.
x3 = {
    "numar": 10
}
#      0

def change(x3):
    x3["numar"] = 11

change(x3)
print(x3)

# Ce se printeaza?

# 1. Eroare! Index out of bounds!
# 2. {"numar": 10}
# 3. {"numar": 11}
# 4. None

# Raspuns corect 3.



print("=========Curs functii 06==========")

# Ex:
# primim o lista de numere intregi. Separati-le in numere pare si impare, si salvati rezultatul intr-un dictionar. Returnati dictionarul cu rezultat.

ex_dictionar = {
    "odd_numbers": [3, 5, 11, 13, 201],
    "even_numbers": [2, 4, 8, 10, 12, 200, 340],
    "odd_total": 233,
    "even_total": 576
}

def is_even(nr):
    return nr % 2 == 0

def list_total(list1):
    total = 0
    for n in list1:
        total = total + n
    return total


def process_data(list1):
    # o sa primeasca list1 = [3, 5, 10, 11, 300]
    # O sa returneze, de exemplu:

    # ex_dictionar = {
    #     "odd_numbers": [3, 5, 11, 13, 201],
    #     "even_numbers": [2, 4, 8, 10, 12, 200, 340],
    #     "odd_total": 233,
    #     "even_total": 576
    # }

    result = {}
    odd_list = []
    even_list = []

    for n in list1:
        if is_even(n):
            even_list.append(n)
        else:
            odd_list.append(n)

    result["odd_numbers"] = odd_list
    result["even_numbers"] = even_list
    result["odd_total"] = list_total(odd_list)
    result["even_total"] = list_total(even_list)
    return result


data_list = [0, 5, 11, 31, 40, 52, 100, 999]
var2 = process_data(data_list)
print(var2)


# builtin functions and tools:
print("========Other functions=========")

# map(), filter(), reduce(), sorted(), functii lambda

lista2 = [3, 5, 10, 20]
# 3  ->  6
# 5  -> 10
# 10 -> 20
# 20 -> 40

def mult_2(nr):
    return nr * 2

# lista3 = []
# for x in lista2:
#     lista3.append(mult_2(x))
# print(lista3)

def pow_2(nr):
    return nr ** 2

result1 = list(map(pow_2, lista2))
print(result1)

# iterators and generators.
# iter1 = map(pow_2, lista2)
#
# for x in iter1:
#     print(x)

# lambda x: x/5
# def div_5(x):
#     return x/5

result2 = list(map(lambda x: x/5, lista2))
print(result2)

# functie_neanonima = lambda a, b: a+b
# print(functie_neanonima(3, 6))
# print(functie_neanonima(10, 300))

# Filter:

nr_pare = list(filter(lambda x: x % 2 == 0, lista2))
print(nr_pare)

nr_mari_5 = list(filter(lambda x: x > 11, lista2))
print(nr_mari_5)


lista5 = [7, 10, 14, 13, 30, 60]

# rezult = {
#     7: "impar",
#     10: "par",
#     14: "par",
#     13: "impar"
# }

# ["impar", "par", "par", ....]
strings = list(map(lambda x: "par" if x % 2 == 0 else "impar", lista5))
print(strings)

result = {}

for i in range(len(lista5)):
    nr = lista5[i]
    choice_nr = strings[i]
    # aici se creaza perechile de chei - valoare.
    result[nr] = choice_nr

print(result)

# lambda x: "par" if x % 2 == 0 else "impar"
# def par_impar(x):
#     if x % 2 == 0:
#         return "par"
#     else:
#         return "impar"




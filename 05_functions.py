import copy

var1 = "hello"

def change_variable(param1):
    param1 = "this is not a hello."


print(var1)
# pass by value.
change_variable(var1)
print(var1)

var2 = [30, 100]

def change_variable_list(param1):
    param1.append(99)
    param1.clear()

print(var2)
# pass by reference.
change_variable_list(var2)
print(var2)



# max si suma nr dintr-o lista.

lista2 = [40, 90, 100, 10, 4, 1]

def get_total(param1):
    total = 0
    for nr in param1:
        total = total + nr
    return total

print(get_total(lista2))

def get_max(param1):
    max = param1[0]
    for nr in param1:
        if nr > max:
            max = nr
    return max

print(get_max(lista2))

print("============Dictionar============")

student = {
    "name": "Adrian",
    "age": 32,
    "weight": 70.0,
    "backpack": ["keys", "wallet", "camera", "phone"],
    0: "nothing at all",
    (1, 2): "alpha and omega"
}

print(student)
print(student["name"])
print(student["backpack"][2])


for k in student.keys():
    print(k)


for key, value in student.items():
    print(key, "---", value)

print(student)
student["age"] = 33
print(student)
student["address"] = "Brasov"
print(student)
# eroare, arunca exceptie, opreste programul.
# print(student["hhh"])

# student["hhh"] = "assassin"
print(student.get("hhh", "default value"))

student.pop("address")
print(student)
# student.clear()

if "address" in student:
    print("Avem adresa pentru acest student")
else:
    print("Studentul acesta nu are adresa!")

# shallow copy!
student_doi = student.copy()

student_doi["restante"] = 3
print("Student original:")
print(student)
print("Studentul doi cu restante:")
print(student_doi)


print("==========Shallow Copy Drawbacks==========")

# student_doi["backpack"].append("casti")
# print(student_doi)
# print(student)

# deep copy example!
student_trei = copy.deepcopy(student)
student_trei["backpack"].append("casti")
print(student_trei)
print("Studentul original")
print(student)


print("===========Function dict exercises==========")

# creeaza o functie care aduna toate numerele din dictionar.

dict2 = {
    "name": "Omega",
    "dimensions": 6,
    "size": 13,
    "count": -1,
    "axis": "y",
    "trees": "all"
}

def add_all_numbers(param1):
    total = 0
    for key in dict2.keys():
        valoare = dict2[key]
        if isinstance(valoare, int):
            total = total + valoare
    return total


# check if var4 is integer:
var4 = "100"
print(isinstance(var4, int))

# check if var4 is integer or float number:
print(isinstance(var4, (int, float)))

print(add_all_numbers(dict2))

print("==============Odd/Even Numbers=============")

# 5 / 2 -> 2, rest 1
# print(17 % 2)

def is_even(nr):
    return nr % 2 == 0

lista3 = [5, 10, 4, 30, 25, 7]

# Adunam toate numerele pare.

def add_all_evens(param1):
    total = 0
    for nr in param1:
        if is_even(nr):
            total = total + nr

    return total

rezultat = add_all_evens(lista3)
print(rezultat)




var1 = [0, 1, 2, 3]

# Tuplu:

coordonate_punct1 = (3, 5)
coordonate_punct2 = (0, 10)
#                    0,  1

persoana1 = ("Adrian", 32, "Brasov", "Tutore", True, 300, 185, 70)
#                   0   1         2         3     4    5    6   7

# print(coordonate_punct1)
# print(coordonate_punct2)
print(persoana1[3])

# assign:
# error:
# persoana1[3] = "Student"
print(persoana1[3])

persoana2 = ("Adrian", 32, "Brasov", "Student", True, 300, 185, 70)

# CTRL + SPACE for autocomplete

tuplu2 = ("Tudor", (30, "Cluj", "Tamplar", ("Universitate", "Europa", ("Sursa Divina", ("Pur Existenta")))))

# tuplu2[1]          -> (30, "Cluj", "Tamplar", ("Universitate", "Europa", ("Sursa Divina", ("Pur Existenta"))))
# tuplu2[1][3]       -> ("Universitate", "Europa", ("Sursa Divina", ("Pur Existenta")))
# tuplu2[1][3][2]    -> ("Sursa Divina", ("Pur Existenta"))
# tuplu2[1][3][2][1] -> "Pur Existenta"

print(tuplu2[1][3][2][1])

# 7:42

print("=========END===========")

# END TUPLES


# SETS
# SETS - data structure

# {3, 4, 100, 200, 5, 9, 0}
# {}
# {3, 4, 3}

var2 = {3, 4, 10, 0, 90, 90}
print(var2)

var2.add(100)

print(var2)
var2.remove(10)
print(var2)

# complexitate
# O(n)

persoane = ["Tudor", "Maria", "Vlad", "Adrian", "Flavia", "Vlad", "Marius"]
print(persoane)
var4 = set(persoane)
print(var4)

# 7 pasi
# Complexitatea codului astuia este O(n) -> Liniar
if "Marius" in persoane:
    print("Marius este printre noi.")
else:
    print("Marius nu este printre noi.")

# 1 Pas
# Complexitatea este O(1) -> Constant
if "Marius" in var4:
    print("Marius este printre noi.")
else:
    print("Marius nu este printre noi.")

# hashes:
# Marius -> 2309458034875956734453
# Vlad   -> 9234895739452367585678

# END SETS

print("============END============")

# Lists + Strings

str1 = "LOG: Hello this is Vlad the Impaler."
str2 = "WARN: My story is way overblown."
str3 = "ERROR: )(*^&#(*%^@*&%$*&^@#%$#)!#&^!#(*&$^(*%~~~~`````"
list3 = ["adrian", "client", "studenti"]
list4 = [str1, str2, str3]
# list4 = ["Hello this is Vlad the Impaler.", "My story is way overblown.", ")(*^&#(*%^@*&%$*&^@#%$#)!#&^!#(*&$^(*%~~~~`````"]
print(list4)
# task: split all the strings in our list, split them using the ":" character.
# example: "LOG: Hello this is Vlad the Impaler." -> ["LOG", " Hello this is Vlad the Impaler."]

# print(list4[0].split(":"))

# 0, 1, 2
print(len(list4))
print(list(range(len(list4))))


for i in range(len(list4)):
    # print("Elementul de pe pozitia: ")
    # print(i)
    # print(list4[i])
    list4[i] = list4[i].split(":")

print(list4)

# list4:
# [
#  "LOG: Hello this is Vlad the Impaler.",
#  "WARN: My story is way overblown.",
#  "ERROR: )(*^&#(*%^@*&%$*&^@#%$#)!#&^!#(*&$^(*%~~~~`````"
#  ]

# ->

# list4:
# [
#  ['LOG', ' Hello this is Vlad the Impaler.'],
#  ['WARN', ' My story is way overblown.'],
#  ['ERROR', ' )(*^&#(*%^@*&%$*&^@#%$#)!#&^!#(*&$^(*%~~~~`````']
#  ]

# print("============")

# list5 = [10, 20, 30]
# list5[1] = 100
# print(list5)









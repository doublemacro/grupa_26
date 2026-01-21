

def user_hello(name):
    print(name)
    print("Hello World!")
    print(f"This is {name} speaking. I am happyty to be here.")


user_hello("Adrian")
user_hello("Jack")
user_hello("Tom")


def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

result1 = add(2, 10)
print(result1 + 20)

result2 = multiply(3, 15)
print(result2)
# (2 + 10) * 13

# print((2 + 10) * 13)

result3 = multiply(add(2, 10), 13)
print(result3)

# ((7 + 14) * (8 + 4)) + 100

result4 = add(multiply(add(7, 14), add(8, 4)), 100)
print(result4)


# print(lista3[(len(lista3) + 1) // 2 : len(lista3)])

def slice_list_in_half(param_list):
    return param_list[ len(param_list) // 2 : len(param_list) ]


lista1 = [40, 99, 101, 8, 67, 1, 13, 888, 777]

rezultat = slice_list_in_half(lista1)
print(rezultat)

print(slice_list_in_half([10, 20, 30, 555, 35325, 123]))
print(slice_list_in_half([1, 3, 5, 1000, 2394029349, 23423, 2]))
print(slice_list_in_half(list(range(1, 999))))


def slice_first_half(param_list):
    print("starting to slice!")
    print("and then returning result!")
    return param_list[0 : len(param_list) // 2]
    # ce e dupa "return" nu ruleaza! linia de dedesubt nu o sa ruleze.
    print("finished operation!")

print(slice_first_half([3, 50, 14, 99, 87, 56, 2]))

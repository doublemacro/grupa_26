
# Mostenire, pentru Clase.
# overwrite

class Animal:
    def __init__(self, name="Amoeba"):
        self.name = name

    def action(self):
        print("I'm searching for food!")


class Cat(Animal):
    # Non-default parameter needs to be on the left side, and all parameters with default value need to be on the right.
    def __init__(self, stripes, name="Cat"):
        super().__init__(name)
        self.stripes = stripes

    def purr(self):
        print("Prrrrrrrrrrr")

    def action(self):
        # putem sa accesam metoda originala action() din clasa din care mostenim, cu super()
        super().action()
        print("Hunting for mice and rats!")

class Dog(Animal):
    def action(self):
        print("Runs around, looking for squirrels.")
        print("Licks your face afterwards.")


print("Animal::")
anim1 = Animal("Lizard")
anim1.action()
print(anim1.name)

print("Cat::")
cat1 = Cat("Red", name="Leo")
cat1.purr()
cat1.action()
print(cat1.name)
print(cat1.stripes)

# Polimorfism.

cat2 = Cat("Orange", name="Skitty")
cat3 = Cat("Black", name="Skittles")
dog1 = Dog("Hunter")
dog2 = Dog("PawPaw")

animal_park = [cat2, cat3, dog1, dog2]

print("Animal Park::")

for v in animal_park:
    print(v.name)
    v.action()





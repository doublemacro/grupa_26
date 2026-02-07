
class Cat:
    def __init__(self, name, owner = None):
        self.name = name
        self.owner = owner

    def __str__(self):
        if self.owner is None:
            return f"Cat: {self.name}."
        else:
            return f"Cat: {self.name}, with owner: {self.owner}."

    def __repr__(self):
        if self.owner is None:
            return f"Cat('{self.name}')"
        else:
            return f"Cat('{self.name}', '{self.owner}')"

catvar1 = Cat("Spot", "Iulian")
cat2 = Cat("Shadow")

print(catvar1)
print(cat2)

pisici = [catvar1, cat2]
print(pisici)

reprezentare_str = str(catvar1)
print(reprezentare_str)
print(type(reprezentare_str))

cats = [Cat('Spot', 'Iulian'), Cat('Shadow', 'None')]
print(cats)

print("==============")
cat4 = Cat("Ginger")
cats_2 = [cat4]
print(cat4)
print(cats_2)

cat5 = Cat('Ginger', 'Oscar')


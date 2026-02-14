
class Cat:

    behaviour = "Feline"
    tail_type = "Long and Fluffy"

    def __init__(self, name):
        # name is an instance property.
        self.name = name


Cat.behaviour = "Changed Behaviour"
cat1 = Cat("Shadow")
cat2 = Cat("Spot")
print(cat1.name)
print(cat1.behaviour)

cat1.behaviour = "Lazy and sleepy."
print(cat1.behaviour)

print(cat2.behaviour)

# https://peps.python.org/pep-0008/#maximum-line-length

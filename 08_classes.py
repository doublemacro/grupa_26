
text = """
Strings can be manipulated in many ways!
You can split them, slice them, and change their case.

    Indentation matters sometimes.
Whitespace can be tricky. Hello

Have fun exploring string methods like:
lower(), upper(), strip(), replace(), and split().

Iterator
"""

# Functie care numara cuvintele dintr-un string.

def count_words(string1):
    return len(string1.split(" "))

def count_words_starting_i(string1):
    # numara toate cuvintele care incep cu i sau I
    words_list = string1.split()
    total = 0
    for word in words_list:
        if word.startswith("i") or word.startswith("I"):
            total = total + 1

    return total

def generate_report(string1):
    word_count = count_words(string1)
    words_starting_with_i = count_words_starting_i(string1)

    report = f"""
Din sirul de caractere original, avem in total:
{word_count} Cuvinte
{words_starting_with_i}  Cuvinte care incep cu i
"""
    return report

result = count_words(text)
print(result)

result2 = count_words_starting_i(text)
print(result2)

# Genereaza un raport:
"""
Din sirul de caractere original, avem in total:
36 Cuvinte
2  Cuvinte care incep cu i
"""

report = generate_report(text)
print(report)


print("Converting to class:")

# text_processor1 = TextProcessor(text)
# report2 = text_processor1.generate_report()
# print(report2)

class TextProcessor:
    def __init__(self, param1):
        self.text = param1

    def count_words(self):
        return len(self.text.split(" "))

    def count_words_starting_i(self):
        # numara toate cuvintele care incep cu i sau I
        words_list = self.text.split()
        total = 0
        for word in words_list:
            if word.startswith("i") or word.startswith("I"):
                total = total + 1

        return total

    def generate_report(self):
        word_count = self.count_words()
        words_starting_with_i = self.count_words_starting_i()

        report = f"""
Din sirul de caractere original, avem in total:
{word_count} Cuvinte
{words_starting_with_i}  Cuvinte care incep cu i
"""
        return report


text_processor_1 = TextProcessor(text)
report2 = text_processor_1.generate_report()
print(report2)


print("==========Parametri============")


param1 = "Hello"
print("=========ne jucam cu parametrii===========")
print()

# se defineste o functie
def fc1(param1):
    print(param1)

def fc2():
    return "Another Hello!"

# se apeleaza acea functie
fc1("This is not a hello")
fc1(fc2())
fc1("")

print("============Joaca 2=============")

def fc3(p1, param2=10, param3=20, param1=30):
    print(p1)
    print(param2)
    print(param3)
    print(param1)


# fc3("2", "3", "1")

fc3("Not hello", param2=4, param3=99, param1=50)






















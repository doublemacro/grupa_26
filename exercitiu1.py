
# 1. Creati o functie "top_students" care extrage toti studentii cu un test_score mai mare de 90, si returneaza o lista cu acei studenti.

# 2. Creaza o functie "extract_students" care extrage toti studentii "bachelor" si "masters", intr-un dictionar si il returneaza. Dictionarul arata in urmatorul fel:

example_dict = {
    "bachelor": [{"name": "Mason Dubois", "age": 21, "test_score": 71, "role": "bachelor"}, {"name": "Ethan Singh", "age": 20, "test_score": 79, "role": "bachelor"}],
    "masters": [{"name": "Isabella Nowak", "age": 25, "test_score": 89, "role": "masters"}, {"name": "Isabella Nowak", "age": 25, "test_score": 89, "role": "masters"}]
}

# 3. Creaza o functie "student_balance" care returneaza "bachelor" daca sunt mai multi bachelor decat masters, si "masters" daca sunt mai multi masters decat bachelor.

students = [
    {"name": "Emma Thompson", "age": 21, "test_score": 88, "role": "bachelor"},
    {"name": "Liam Chen", "age": 22, "test_score": 76, "role": "bachelor"},
    {"name": "Sofia Rodriguez", "age": 24, "test_score": 92, "role": "masters"},
    {"name": "Noah Patel", "age": 20, "test_score": 65, "role": "bachelor"},
    {"name": "Ava Müller", "age": 23, "test_score": 95, "role": "masters"},
    {"name": "Lucas Kim", "age": 19, "test_score": 82, "role": "bachelor"},
    {"name": "Isabella Nowak", "age": 25, "test_score": 89, "role": "masters"},
    {"name": "Mason Dubois", "age": 21, "test_score": 71, "role": "bachelor"},
    {"name": "Olivia Rossi", "age": 22, "test_score": 94, "role": "masters"},
    {"name": "Ethan Singh", "age": 20, "test_score": 79, "role": "bachelor"},
]


print("======================================================================================================================================================")
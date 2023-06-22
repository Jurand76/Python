nested_dict = {
    "fruits": {"apple": 3, "banana": 4, "cherry": 5},
    "vegetables": {"carrot": 7, "broccoli": 2, "cabbage": 6}
}

# Utwórz nowy słownik, który zawiera tylko te produkty, których liczba jest większa niż 4
filtered_dict = {category: {item: count for item, count in items.items() if count > 4} for category, items in nested_dict.items()}
print(filtered_dict) # Wynik: {'fruits': {'cherry': 5}, 'vegetables': {'cabbage': 6}}

students = [("Ania", 3.5), ("Kamil", 4.5), ("Ola", 4.0), ("Piotr", 5.0), ("Ewa", 3.0)]

filtered_students = [(student[0], student[1]) for student in students if student[1] >= 4.0 ]

print(filtered_students)

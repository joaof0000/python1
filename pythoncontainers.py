# Exercise 1
students = ["Alice", "Bob", "Charlie"]

# Print second student's name
print(students[1])

# Print last student's name
print(students[-1])


# Exercise 2
foods = ("Pizza", "Burger", "Salad")

# Print out the foods using a for loop
for food in foods:
    print(f"{food} is a good food")

# Exercise 3
for food in foods[-2:]:
    print(food)


# Exercise 4
home_town = {
    "city": "Arcadia",
    "state": "California",
    "population": 58000
}

print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")

# Exercise 5
for key, value in home_town.items():
    print(f"{key} = {value}")

# Exercise 6
cohort = []

for index, student in enumerate(students):
    cohort.append({
        'student': student,
        'fav_food': foods[index]
    })

for item in cohort:
    print(item)


# Exercise 7
awesome_students = [f"{student} is awesome!" for student in students]

for string in awesome_students:
    print(string)

# Exercise 8
filtered_foods = [food for food in foods if 'a' in food.lower()]

for food in filtered_foods:
    print(food)


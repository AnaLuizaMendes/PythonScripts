# List Comprehensions
scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name in scores if scores.get(name) >= 65]
print(passed)
print('\n')

names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.split()[0].lower() for name in names]
print(first_names)
print('\n')

multiples_3 = [x * 3 for x in range(1, 21)]
print(multiples_3)
print('\n')
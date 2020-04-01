# access the flower dictionary and find the flower with the same first letter of the user input name
with open('flowers.txt') as f:
    flower_dict = {}
    for line in f:
        flower_dict[line.split(':')[0]] = line.split(':')[1].strip()
print(flower_dict)

name = input('Enter your First [space] Last name only: ')
first_letter = name[:1]
print("Unique flower name with the first letter: {}".format(flower_dict.get(first_letter)))


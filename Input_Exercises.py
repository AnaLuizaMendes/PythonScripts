names = input("Enter students names separated by commas: ").split(',')
assignments = input("Enter students missing assignments separated by commas: ").split(',')
grades = input("Enter students grades separated by commas: ").split(',')
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
i = 0
for name in names:
    final_grade = int(assignments[i]) * 2 + int(grades[i])
    print(message.format(name.title(), assignments[i], grades[i], final_grade))
    i += 1
# another way of doing this would be using zip
# for name, assignment, grade in zip(names, assignments, grades):
# then you can access each first, then second, ... element in the lists together

def party_planner(cookies, people):
    leftovers = None
    num_each = None

    try:
        num_each = cookies // people
        leftovers = cookies % people

    except ZeroDivisionError:
        print("Zero is not a valid number of people.\n"
              "Please insert a valid number.\n")

    return (num_each, leftovers)

# The main code block is below
lets_party = 'y'
while lets_party == 'y':

    cookies = int(input("How many cookies are you baking? "))
    people = int(input("How many people are attending? "))

    cookies_each, leftovers = party_planner(cookies, people)

    if cookies_each:  # if cookies_each is not None
        message = "\nLet's party! We'll have {} people attending, they'll each get to eat {} cookies, and we'll have {} left over."
        print(message.format(people, cookies_each, leftovers))

    lets_party = input("\nWould you like to party more? (y or n) ")


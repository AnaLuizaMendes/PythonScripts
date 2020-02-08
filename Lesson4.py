# Lesson 4 - Practising
# Calculating Factorial in Python

number = 20
product = 1
current = 1

while current <= number:
    product *= current
    current += 1

print(product)

# Option 2

number = 20
product = 1

for each in range(2, (number + 1)):
    product *= each

print(product)

# How to count from a number to another number until a final number

start_num = 2  # provide some start number
end_num = 26  # provide some end number that you stop when you hit
count_by = 2  # provide some number to count by
break_num = 0

if end_num > start_num:
    while break_num <= end_num:
        start_num += count_by
        break_num = start_num
        result = break_num
else:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."

print(result)

# Write a while loop that finds the largest square number
# less than an integer limit and stores it in a variable nearest_square

limit = 40
num = 1

while num*num < limit:
    nearest_square = num*num
    num += 1

print(nearest_square)

## Please use this space to test and run your code
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69,
            113, 166]
odd_list = []
i = 0

while len(odd_list) < 5:
    if num_list[i] % 2 != 0:
        odd_list.append(num_list[i])
    i += 1

print(sum(odd_list))

# Write a while loop using break statement to create a string with exactly 140 characters
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""

for headline in headlines:
    if len(news_ticker) + len(headline) <= 140:
        news_ticker += headline + " "

    else:
        for character in headline:
            if len(news_ticker) + len(character) <= 140:
                news_ticker += character
            else:
                break

print(news_ticker)
print(len(news_ticker))

print('Your code should check if each number in the list is a prime number\n')
check_prime = [26, 39, 51, 53, 57, 79, 85]
prime_number = False

for number in check_prime:
    i = 2
    while i < (number - 2):
        if number % i == 0:
            prime_number = True
            break
        i += 1

    if prime_number:
        print('{} is not a prime number, because {} is a factor of {}'.format(number, i, number))
    else:
        print("{} is a prime number.".format(number))












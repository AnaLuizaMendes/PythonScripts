# Create a string and break it in exactly 140 characters
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

## Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]

for number in check_prime:
    i = 2
    while i < number:
        if number % i == 0:
            print("{} is not a prime number, because {} is a factor of {}".format(number, i, number))
            break
        if i == (number - 1):
            print('{} is not prime'.format(number))
        i += 1

## Zip exercise
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
for point in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}: {}, {}, {}".format(*point))

for point in points:
    print(point)





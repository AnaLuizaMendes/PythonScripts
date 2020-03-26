# Learning how to make a def function


def readable_time(days):
    # getting the integer that represents the number of weeks
    weeks = days // 7
    # getting the integer that represents the number of remaining days
    rem_days = days % 7
    string = '{} week(s) and {} day(s).'.format(weeks, rem_days)
    return string


print(readable_time(40))


def population_density(population, land_area):
    pop_density = population / land_area
    return pop_density


test1 = population_density(20, 4)
print("Result: {}".format(test1))

counter = 0


def increment(number):
    number += 1
    return number


counter = increment(counter)
print(counter)

#Lesson 3 - part 1 - exercises

#def fuction

def multiply(a, b):
    a = a * b
    print(a)

def printy(a):
    a = a + 'ify'
    print(a)

multiply(2, 3)
printy('test')

def add(a, b):
    print(a + b)

#set {} - unordered and mutable (unique values)

set_1 = {1, 2, 4, 57, 1, 2, 65, 23, 3}
print(set(set_1))

set_1.remove(57)
print(set_1)

my_list = [1, 2, 3, 45, 65, 12, 1, 45, 75, 95, 88, 452, 652, 123, 452]
my_list = set(my_list)
print(my_list)
print(len(my_list))
print(my_list.pop())
print(my_list)


names = ['Rob', 'Vinnie', 'Joe', 'Ritchie', 'Luciana', 'Leona', 'Rob', 'Ana', 'Luciana']

print(len(names))

names = set(names)
print(len(names))

print(max(names))
print(sorted(names))
print('Vinnie' in names)

#Dictionary {} - unordered and mutable (unique) - pairs of elements (keys and value)

population = {'Shanghai': 17.8, 'Istanbul': 13.3, 'Karachi': 13.0, 'Mumbai': 12.5}

print('Shanghai' in population)
population['Dublin'] = 15.4
print(population)

print(population.get('Shanghai'))

x = population.get('Shanghai')
print(x is None)
print(x is not None)
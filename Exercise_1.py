#testing hackerrank challengings

#if-else problem
n = int(input())
if 2 <= n <= 5 and n % 2 == 0:
   message = ('Not Weird')
elif 6 <= n <= 20 and n % 2 == 0:
    message = ('Weird')
elif n > 20 and n % 2 == 0:
    message = ('Not Weird')
else:
    message = ('Weird')
print(message)




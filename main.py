import array
list = []
n = int(input('How many numbers: '))
total = 0

for i in range(n):
    value = int(input('Enter value: '))
    total += value

avg = total/n

print('Average is ' + str(avg))

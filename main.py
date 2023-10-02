numbers = []

n = int(input('How many numbers: '))
total = 0

largest = None
smallest = None

for i in range(n):
    value = int(input('Enter value: '))

    if largest is None or value > largest:
        largest = value
    if smallest is None or value < smallest:
        smallest = value
    
    total += value

    numbers.append(value)

avg = total / n

print('Average is ' + str(avg))
print('Largest number is ' + str(largest))
print('Smallest number is ' + str(smallest))

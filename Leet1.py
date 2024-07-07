import os

array = []
seen_numbers = set()
a = True

while a ==True:
    user_input = input("Enter number, type stop to finish ")
    if user_input.lower() == 'stop':
        a = False
    else: 
        try:
            number = int(user_input)
            if number not in seen_numbers:
                array.append(number)
                seen_numbers.add(number)
        except ValueError:
            print('type a valid number')

try:
    target = int(input('enter target number'))
except ValueError:
    print('enter a valid number')
    target = None

if target is not None:
    found = False
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == target:
                print(f'two number that sum to {target} are: {[i]} and {[j]}')
                found = True

    if not found:
        print(f'No 2 numbers that sum up to {target}')



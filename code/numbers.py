'''
Write a python program to input integer values until a 0 is entered.
For each input integer if its odd, store in a dictionary under the key 'odd' 
and if its even, store in a dictionary under the key 'even'.

After a zero is entered, print the dictionary.

For example, if the input is:
2 3 5 4 6 0 

The output should be:
{'odd': [3, 5], 'even': [2, 4, 6]}
'''
numbers = {'odd': [], 'even': []}
while True:
    user_number = int(input("enter a number: "))
    if user_number == 0:
        break
    if user_number % 2 == 0:
        numbers['even'].append(user_number)
    else:
        numbers['odd'].append(user_number)

print(numbers)

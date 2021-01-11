# Write some code that creates a list of integers, loops through each element of the list and only prints out even numbers!

list = [1, 2, 3, 4, 5, 6]

for x in list:
    if(x % 2 == 0):
        print(x)
    else:
        continue

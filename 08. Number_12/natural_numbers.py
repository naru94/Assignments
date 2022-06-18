from random import randint

list_even = []

count = 0

while (count < 10):
    num = randint(1, 100)
    if(num%2 == 0):
        list_even.append(num)
        count = count + 1

print("List of natural numbers: ", list_even)

num_of_ele = len(list_even)

print("Number of elements: ", num_of_ele)

list_even.reverse()

print("Reverse List: ", list_even)

list_even.sort(reverse=False)

print("Ascending: ", list_even)

list_even.sort(reverse=True)

print("Descending: ", list_even)

list_even[4] = 100

print("Updated List: ", list_even)

list_square = []

for i in list_even:
    list_square.append(i**2)

print("Square: ", list_square)
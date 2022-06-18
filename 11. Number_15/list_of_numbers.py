from random import randint

list_of_numbers = []

count = 0

while (count < 10):
    num = randint(1, 100)
    list_of_numbers.append(num)
    count = count + 1
print("List: ", list_of_numbers)

input_index = int(input("Enter the Index: "))

new_list = list_of_numbers[5:(input_index-2)]

print("New List: ", new_list)
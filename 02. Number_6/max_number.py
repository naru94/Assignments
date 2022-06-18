size = int(input("How many numbers do you wish to enter: "))

my_list = []

for i in range(size):
    input_num = int(input("Enter a number: "))
    my_list.append(input_num)

print("List: ", my_list)

maximum = my_list[0]

for i in my_list:
    if maximum < i:
        maximum = i

print("Maximum: ", maximum)

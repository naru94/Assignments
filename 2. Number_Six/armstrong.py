input_num = input("Enter a number: ")

length_num = len(input_num)
print("Length of number: ", length_num)

input_num = int(input_num)
sum = 0
temp = input_num


# 123

while temp > 0:
    digit = temp % 10                # 123 % 10 = 3      # 12 % 10 = 2   # 1 % 10 = 1            # exit
    sum = sum + digit**length_num    # 3**3              # 3**3 + 2**3   # 3**3 + 2**3 + 1**3
    temp = temp // 10                # 123 // 10 = 12    # 12 // 10 = 1  # 1 //10 = 0

if sum == input_num:
    print("The number is an Armstrong number")
else:
    print("The number is not an Armstrong number")


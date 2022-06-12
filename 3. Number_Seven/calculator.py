def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def quot(a, b):
    return a // b

def rem(a, b):
    return a % b

def div(a, b):
    return a / b

input_num_1 = int(input("Enter the 1st number: "))
input_num_2 = int(input("Enter the 2nd number: "))

operation = input("Enter the operation (add, sub, mul, quot, rem, div) : ")

if(operation == "add"):
    result = add(input_num_1, input_num_2)
    print("Addition of " + str(input_num_1) + " and " + str(input_num_2) + " = " + str(result))
elif(operation == "sub"):
    result = sub(input_num_1, input_num_2)
    print("Subtraction of " + str(input_num_1) + " and " + str(input_num_2) + " = " + str(result))
elif(operation == "mul"):
    result = mul(input_num_1, input_num_2)
    print("Multiplication of " + str(input_num_1) + " and " + str(input_num_2) + " = " + str(result))
elif(operation == "quot"):
    result = quot(input_num_1, input_num_2)
    print("Quotient of " + str(input_num_1) + " and " + str(input_num_2) + " = " + str(result))
elif(operation == "rem"):
    result = rem(input_num_1, input_num_2)
    print("Remainder in " + str(input_num_1) + " and " + str(input_num_2) + " = " + str(result))
elif(operation == "div"):
    result = div(input_num_1, input_num_2)
    print("Division of " + str(input_num_1) + " and " + str(input_num_2) + " = " + str(result))

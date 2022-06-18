input_num = int(input("Enter the number: "))

prime = True

if input_num == 1:
    print("The input number 1 is neither prime nor composite")

elif input_num > 1:
    for i in range(2, input_num):
        if input_num%i == 0:
            prime=False
            break;

if prime:
    print("The input number " + str(input_num) + " is Prime")
else:
    print("The input number " + str(input_num) + " is Composite")
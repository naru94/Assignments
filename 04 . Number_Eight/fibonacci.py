# 0, 1, 1, 2, 3, 5, 8, 13, 21

num_terms = int(input("Enter the numbers of terms: "))

n1 = 0;
n2 = 1;
count = 0

if(num_terms <= 0):
    print("Enter a postive number")
elif(num_terms == 1):
    print("Fibonacci series: ", n1)
elif(num_terms > 1):
    print("Fibonacci series: ")
    while(count < num_terms):
        print(n1)
        nth = n1 + n2

        n1 = n2
        n2 = nth

        count = count + 1

A = "Python Programming Language"
B = "Best in the World"

word_gram = A[10] + A[11] + A[12] + A[13]
print("Word: ", word_gram)

word_gram_sliced = A[10:14]
print("Word: ", word_gram_sliced)

word_world_sliced_1 = B[12:17]
print("Word: ", word_world_sliced_1)

word_world_sliced_2 = B[-5:]
print("Word: ", word_world_sliced_2)

upper_A = A.upper()
print("Upper case A: ", upper_A)

upper_B = B.upper()
print("Upper case A: ", upper_B)

reverse_string = A[::-1]
print("Reversed: ", reverse_string)

concatenate_result = A + " "+ B
print("Result: ", concatenate_result)



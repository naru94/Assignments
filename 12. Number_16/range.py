range_list = list()

count = 0

for i in range(5, 100, 3):
    if(count < 18):
        range_list.append(i)
        count = count + 1

print("List: ", range_list)


count = 0
new_list = [x for x in range(5, 100, 5) if count < 18]
print("New List: ", new_list)


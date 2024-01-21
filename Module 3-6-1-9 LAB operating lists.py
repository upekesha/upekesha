my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
print("original list ", my_list)
my_list_unique = my_list
my_list_unique.sort()


print("sorted list ", my_list_unique)

hits = 0

for number in my_list_unique:
    if number in my_list:
        hits += 1
print("number hits: ",hits)


print("list w/ unique elements only:", my_list_unique)

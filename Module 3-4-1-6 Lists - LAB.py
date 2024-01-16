##3.4.1.6 LAB
hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.
print("\nOriginal List:",hat_list) #original list

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
hat_list[2]= int(input("Enter a number to replace middle of list: "))

# Step 2: write a line of code that removes the last element from the list.
del(hat_list[-1])

# Step 3: write a line of code that prints the length of the existing list.
print("\nList's length:",len(hat_list))
print(hat_list)

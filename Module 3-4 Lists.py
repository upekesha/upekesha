#3.4.1.2 part A
numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("\nPrevious list content:", numbers)  # Printing previous list content.

#3.4.1.2 part B
numbers[1] = numbers[4]# Copying value of the fifth element to the second.
print("New list content: ", numbers)  # Printing Current list content.


#3.4.1.3
print(numbers[0]) # Accessing the list's first element.
print(numbers)# Printing the whole list.

print("\nList length:", len(numbers))  # Printing the list's length.

###3.4.1.4 Operations on lists

del numbers[1]  # Removing the second element from the list.
print("New list's length:", len(numbers))  # Printing new list length.
print("\nNew list content:", numbers)  # Printing current list content.

### 3.4.1.5
print(numbers[-1]) #last one in the list
print(numbers[-2]) #2nd to last one in the list
print(numbers[-4]) #4th from last one , i.e. first element in list



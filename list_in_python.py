my_list = [1, "apple", 3.14]

print(my_list)


# # Append (Add to end):

# Python

my_list.append("cherry")
print(my_list)


# Insert (Add at specific position):

# Python

# # insert(index, item)

my_list.insert(1, "mango")
print(my_list)
# Result: ["apple", "mango", "banana", "cherry"]


# Update (Change an item):

# Python

# Access by index and assign new value
my_list[0] = "kiwi"
print(my_list)
# Result: ["kiwi", "mango", "banana", "cherry"]



# Result: ["apple", "banana", "cherry"]

# Lists in Python

# What it is: An ordered, mutable (changeable) collection of items.

# Syntax: Uses square brackets [].

# Key Feature: You can store mixed data types (integers, strings, etc.) in one list.

# Example: my_list = [1, "apple", 3.14]
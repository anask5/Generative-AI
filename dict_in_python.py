my_dict = {"name": "Alex", "score": 95}
print(my_dict)

# Dictionaries in Python

# What it is: A collection of Key and Value pairs. It is unordered (conceptually) and mutable.

# Syntax: Uses curly braces {} with colons :

# Key Feature: You use the unique "key" to look up the "value" instantly.

# Syntax is exactly the same as adding!
# If the key exists, it updates. If not, it adds.
my_dict["score"] = 90
print(my_dict)
# Result: {"name": "Alex", "age": 21, "city": "New York"}

# Syntax: dict[new_key] = new_value
my_dict["name"] = "Luke"
print(my_dict)
# Result: {"name": "Alex", "age": 20, "city": "New York"}
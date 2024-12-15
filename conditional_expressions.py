# Conditional expression = A one-line sorcut fot the if-else statement (ternary operator)
# Print or assign one of the two values based on a condition
# X if condition else Y
num = 6
a = 6
b = 7
age = 25
temperature = 30
user_role = "admin"

print("Positive" if num > 0 else "Negative")
print("EVEN" if num % 2 == 0 else "ODD")
max_num = a if a > b else b
min_num = a if a < b else b 
print(max_num)
status = "Adult" if age >= 18 else "Child"
print(status)
weather = "HOT" if temperature > 20 else "COLD"
print(weather)
access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(access_level)
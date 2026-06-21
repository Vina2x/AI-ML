a= 5
b=9
sum= a+b
# normal formatting

print("Language is {}".format("Python"))
print("Sum of {} and {} is {}".format(a,b,sum))

# Index based formatting

print("Sum of {1} and {0} is {2}".format(a,b,sum))

# F string

print(f"Sum of {a}+{b} is: {sum}")
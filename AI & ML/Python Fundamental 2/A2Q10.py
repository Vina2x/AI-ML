# Number Guessing Game...

n= int(input("Enter a number: "))
secretNum= 57

if n<secretNum:
    print("Too Low!")

elif n>secretNum:
    print("Too High!")

else:
    print("Correct!")
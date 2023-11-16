try:
    num = float(input("Enter a number: "))
except:
    print("Something went wrong!")

try:
    num = float(input("\nEnter a number: "))
except ValueError:
    print("That was not a number!")

for value in (None, "Hi!"):
    try:
        print("Attempting to convert", value, "->",end="")
        print(float(value))
    except(TypeError, ValueError) :
        print("Something went wrong!")
for value in (None, "Hi!"):
     try:
        print("Ateempting to convert", value, "->",end="")
        print(float(value))
     except(TypeError, ValueError):
        print("I Can only convert string or number!")
     try:
        num = float(input("\nEnter a number: "))
     except ValueError as e:
        print("Not a number! Or as Python would say\n",e)
      
try:
    num = float(input("\nEnter a number: "))
except(ValueError):
    print ("That was not a number!")
else:
    print ("You entered the number", num)


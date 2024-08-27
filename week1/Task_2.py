#Create a program that uses conditional statements to determine if a number is positive, negative, or zero.

Number=int(input("Enter Number: "))

if Number<0:
    print("Number is negative")

elif Number>0:
    print("Number is positive")

else:
    print("Number is zero")
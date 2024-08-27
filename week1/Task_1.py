#Write a Python program to perform basic arithmetic operations (addition, subtraction,multiplication, division).

Number1=int(input("Enter Number 1: "))
Number2=int(input("Enter Number 2: "))

print("1.Addition")
print("2.Substraction")
print("3.Multiplition")
print("4.Division")

choice=int(input("Enter your choice: "))

match(choice):

    case 1:
        print(Number1+Number2)

    case 2:
        print(Number1-Number2)

    case 3:
        print(Number1*Number2)

    case 4:
        print(Number1/Number2)

    case _:
        print("invalid chocie")
        


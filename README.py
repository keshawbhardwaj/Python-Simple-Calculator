# Python-Simple-Calculator
#python proram for calculator
input1 = int(input("enter 1st number: "))
input2 = int(input("enter 2nd number: "))
input3 = input('+,-,*,/ = ')
if input3 == '+':
    print(input1 + input2)
elif input3 == '-':
    print(input1-input2)
elif input3  == '*':
    print(input1*input2)
elif input3=='/':
    print(input1/input2)
else:
    print("Unexpected Error")

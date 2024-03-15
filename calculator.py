#calculator
def calculator():
    num1=int(input("Enter a number :"))
    num2=int(input("enter a number :"))
    opr=input("Enter a operator :")
    print("Number 1=",num1)
    print("Number 2=",num2)
    if opr=='+':
        print("the addition is=",(num1+num2))
    elif opr=='-':
        print("the subtraction is=",(num1-num2))
    elif opr=='*':
        print("the multiplication is=",(num1*num2))
    elif opr=='/':
        print("the division is=",(num1/num2))
    elif opr=='%':
        print("the modulo is=",(num1%num2))
    else:
        print("invalid operator !")

calculator()

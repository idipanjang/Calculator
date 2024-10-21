num1=int(input("Enter Value: "))
opr=input("Enter opr example(+,-,*,/): ")
num2=int(input("Enter Value: "))


if opr == "+":
    print(num1+num2)

elif opr == "-":
    print(num1-num2)

elif opr == "*":
    print(num1*num2)
elif opr == "/":
    print(num1/num2)
else:
    print("invalid opr")

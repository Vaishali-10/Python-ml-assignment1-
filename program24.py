num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
op=input("enter (+,-,*,/):")
if op=="+":
    print("sum:",num1+num2)
elif op=="-":
    print("difference:",num1-num2)
elif op=="*":
    print("product:",num1*num2)
elif op=="/":
    print("division:",num1/num2)
else:
    print("invalid input")
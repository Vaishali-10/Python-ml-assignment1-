x=input("enter f for fahrenheit & c for celsius:")
if x=="f":
    temp1=int(input("enter temprature (in fahrenheit):"))
    celsius=((temp1-32)*5)/9
    print("temprature in degree celsius:",celsius)
elif x=="c":
    temp2=int(input("enter temprature (in celsius):"))
    fah=((temp2*9)/5)+32
    print("temprature in degree celsius:",fah)
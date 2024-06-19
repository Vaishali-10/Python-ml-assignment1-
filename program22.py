n=int(input("enter no of elements:"))
list1=[]
for i in range(1,n+1,1):
    num=int(input("enter number:"))
    list1.append(num)
print("your list:",list1)
list1.sort()
print("max number:",list1[-1])
print("min number:",list1[0])
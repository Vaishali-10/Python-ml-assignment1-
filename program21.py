n=int(input("enter no of elements:"))
list1=[]
count=0
for i in range(1,n+1,1):
    element=input("enter element:")
    list1.append(element)
string=input("enter element you want to count:")
for i in range(0,len(list1),1):
    if list1[i]==string:
        count+=1
print("your list:",list1)
print(string,"occured",count,"times.")
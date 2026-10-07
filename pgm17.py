li=list()
n=int(input("Enter the list size"))
for i in range(0,n):
    a=int(input("Enter the number"))
    li.append(a)
print("List:",li)
result=[num for num in li if num%2!=0]
print("new list:",result)
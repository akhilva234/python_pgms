s1=input("Enter the string 1")
s2=input("Enter the string 2")

pos = int(input("Enter position to swap"))

a=list(s1)
b=list(s2)
a[pos],b[pos]=b[pos],a[pos]
result=''.join(a)+''.join(b)
print(result)
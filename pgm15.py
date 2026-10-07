dict1=dict()
dict2=dict()
n1=int(input("Enter size of 1st dictionary:"))
n2=int(input("Enter size of 2nd dictionary:"))

print("Enter dictionary1 key and value pairs")
for i in range(0,n1):
    key=input("Enter the key:")
    value=input("Enter the value:")
    dict1[key]=value

print("Enter dictionary2 key and value pairs")
for i in range(0,n2):
    key=input("Enter the key:")
    value=input("Enter the value:")
    dict2[key]=value
print("dictionary 1:",dict1)
print("dictionary 2:",dict2)
dict1.update(dict2)
print("Merged dictionary:",dict1)

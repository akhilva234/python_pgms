def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
result=gcd(num1,num2)
print(result)
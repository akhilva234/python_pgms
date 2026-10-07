def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b):
    return a/b if b!=0 else "Cannot Divide by 0"

def mod(a,b):
    return a%b if b!=0 else "Cannot Divide by 0"

print("\n..Select Operation..\n")
print("1.Add | 2.Subtract | 3.Multiply|4.Divide|5.Modulus")
choice = input("enter choice(1-5)")
num1=float(input("Enter first number"))
num2 = float(input("Enter second number"))
if choice == '1':
    print(f"Result:{add(num1,num2)}")
elif choice == '2':
    print(f"Result:{sub(num1,num2)}")
elif choice == '3':
    print(f"Result:{mul(num1,num2)}")
elif choice == '4':
    print(f"Result:{div(num1,num2)}")
elif choice == '5':
    print(f"Result:{mod(num1,num2)}")
else:
    print("invalid choice")
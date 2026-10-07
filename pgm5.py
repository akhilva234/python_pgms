num=int(input("Enter the number"))
n=int(input("How many multiples do you want?"))
print(f"\nThe first {n} multiples of {num} are:")
for i in range(1,n+1):
    print(f"{num}X{i}={num*i}")

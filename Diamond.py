n= int(input("Enter: "))
# n=n//2
for i in range(1,n+1):
    for k in range(n-i):
        print(" ",end="")
    for j in range(i*2-1):
        print("*", end="")
    print()
    
for i in range(n,0,-1):
    for k in range(n-i):
        print(" ",end="")
    for j in range(i*2-1):
        print("*", end="")
    print()
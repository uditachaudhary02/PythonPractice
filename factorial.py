n=int(input("enter no."))
fact=1
if n<0:
    print("no factorial")
elif n==0:
    print("factorial is 1")
else:
    for i in range(1,n+1):
        fact*=i
    print(f"factorial of {n}is{fact}")
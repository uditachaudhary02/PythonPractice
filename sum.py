n=int(input("enter any no"))
sum=0
while n>0:
    digit=n%10
    sum+=digit
    n=n//10
print(sum)

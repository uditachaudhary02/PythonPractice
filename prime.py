n=int(input("enter any number:"))
if n>1:
    for i in range(2,n):
        if(n%i)==0:
            print("it is not prime no.")
            break
    else:
        print("it is prime no,")
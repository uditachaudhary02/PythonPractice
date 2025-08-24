n1=float(input("enyter no"))
n2=float(input("enter no."))
op=input("enter operator")
if op=='+':
   print(n1+n2)
elif op=='-':
   print(n1-n2)
elif op=='*':
   print(n1*n2)
elif op=='/':
     if n2 != 0:
         print(n1 / n2)
     else:
         print("Error! Division by zero.")
else:
    print("invalid operator")
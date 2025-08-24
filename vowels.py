string=input("enter any string")
vowels="AEIOUaeiou"
count=0
for i in string:
    if i in vowels:
        count +=1
print("number of vowels are:",count)

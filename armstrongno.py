num = int(input("Enter a number: "))
original = num
n = len(str(num))   # number of digits
total = 0

while num > 0:
    digit = num % 10              # get last digit
    total += digit ** n           # add digit^n
    num //= 10                    # remove last digit

if total == original:
    print(original, "is an Armstrong number")
else:
    print(original, "is NOT an Armstrong number")
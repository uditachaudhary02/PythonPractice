n=list(map(int,input("enter elements").split()))
large=list(set(n))
large.sort()
if len(large)<2:
    print("2nd largest no does not exist")
else:
    print("2nd largest no is",large[-2])
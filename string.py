s=input("enter any string")
freq={}
for i in s:
    freq[i]=freq.get(i,0)+1
print(freq)
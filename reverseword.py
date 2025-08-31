class solution:
    def reverseword(self, s: str) -> str:
        s=input("enter any string")
        words=s.split(" ")
        reverseword=words[::-1]
        print (" ".join(reverseword))

obj=solution()
obj.reverseword("s")
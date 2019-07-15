alp=int(input())
h=input()
s=list(map(int,h.split()))
if len(s)==alp:
    for i in range(0,alp):
        if s[i]==i:
            print(s[i],end=" ")

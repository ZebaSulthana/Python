alp=int(input())
h=input()
flag=0
s=list(map(int,h.split()))
if len(s)==alp:
    for i in range(0,alp):
        if s[i]==i:
            flag=1
            print(s[i],end=" ")
if flag!=1:    
    print("-1")
    

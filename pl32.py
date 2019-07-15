alp=input()
a=list(map(int,alp.split()))
al=input()
s=list(map(int,al.split()))
if len(s)==a[0]:
    if a[1] in s:
        print("Yes")
    else:
        print("No")
    

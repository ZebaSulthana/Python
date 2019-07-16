alp=int(input())
k=input()
h=list(map(int,k.split()))
for i in h:
    if h.count(i)==1:
        print(i)

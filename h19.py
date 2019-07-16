alp=input()
a=list(map(int,alp.split()))
num=a[0]
k=a[1]
l=[]
h=[]
t=[]
for i in range(num):
    j=input()
    s=list(map(int,j.split()))
    l=l+s
for i in range(0,k):
    h.append(l[i])
for i in range(k,k*2):
    t.append(l[i])
h.sort()
t.sort()
for i in h:
    if i in t:
        print(i,end=" ")

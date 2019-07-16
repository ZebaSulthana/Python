alp=int(input())
k=input()
h=list(map(int,k.split()))
flag=0
for i in range(len(h)-1):
    for j in range(i+1,len(h)):
        if h[i]==h[j]:
            print(h[i])
            flag=1
            break
    if flag==1:
        break
if flag!=1:
    print("unique")
    
    

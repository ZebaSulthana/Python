alp=input()
a=alp.split()
flag=0
for i in a[0]:
    for j in a[1]:
        if i==j:
            print("yes")
            flag=1
            break
    if flag==1:
        break
if flag!=1:
    print("no")

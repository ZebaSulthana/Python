alp=input()
for i in range(1,len(alp)):
    if ord(alp[i])>ord(alp[0]):
        anse=alp[i:]
        break
print(anse)

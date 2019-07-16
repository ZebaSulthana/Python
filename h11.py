alp=input()
h=alp.split()
s=""
for i in h:
    s+=i[::-1]
    s+=" "

print(s)

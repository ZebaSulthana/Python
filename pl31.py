alp=input()
o=0
c=0
if alp.startswith(')') or alp.endswith('('):
    print("no")
else:
    for i in alp:
        if i=='(':
            o+=1
        elif i==')':
            c+=1
    if o==c:
        print("yes")
    else:
        print("no")

alp=int(input())
h=input()
a=list(map(int,h.split()))
str1=""
a.reverse()
for i in a:
    str1+=str(i)+"->"
a=str1.strip('->')
print(a)

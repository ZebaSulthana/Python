alp=int(input())
h=input()
s=list(map(int,h.split()))
if len(s)==alp:
    s.sort(reverse=True)
    k=[str(i) for i in s]
    m=int("".join(k))
    print(m)

alp=(input())
a=list(map(int,alp.split()))
g1=a[0]
g2=a[1]

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
print(gcd(g1,g2))

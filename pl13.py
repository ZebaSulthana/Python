alp=int(input())
summ=0
dig=0
while(alp>0):
    dig=alp%10
    summ+=dig*dig
    alp=alp//10
print(summ)

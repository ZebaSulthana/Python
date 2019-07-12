tt=int(input())
re=0
while(tt>0):
  digit=tt%10
  re=re*10+digit
  tt=tt//10
print(re)

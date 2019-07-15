l=int(input())
alp=input()
sft=""
vo=['a','e','i','o','u','A','E','I','O','U']
for i in alp:
    if i not in vo:
        sft+=i
print(sft[::-1])


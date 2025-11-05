#1
m: int = int(input())
n: int = int(input())

for i in range(m,n+1):
    if i%17==0 or i%10==9 or (i%3==0 and i%5==0):
        print(i)


#2

n: int = int(input())
for i in range(1,n):
    if(5<=i<=9) or (17<=i<=37) or (78<=i<=87):
        continue
    print(i)

#3

m: int = int(input())

for i in range(3):
    print(m, end=' ')
print('/n')
for i in range(3):
    print(m, end= ' ' )
print('/n')
for i in range(3):
    print(m, end= ' ' )
print('/n')


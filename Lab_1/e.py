s,n = map(int,input().split())
p = 0
for i in range(2, s-1):
    if s%i==0:
        p+=1
        break
if (s<=500 and p==0 and n%2==0):
    print('Good job!')
else:
    print('Try next time!')
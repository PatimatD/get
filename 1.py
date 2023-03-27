a=list(map(str,input().split()))
c=''
d=''
for i in range(len(a)):
    c=c+str(a[i])
    k=''.join(reversed(a[len(a)-1-i]))
    d=d+k
if d==c:
    print('Yes')
else:
    print('No')

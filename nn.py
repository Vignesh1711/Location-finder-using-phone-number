a=input()
b=input()
a=a[::-1]
b=b[::-1]
p=0
asum=0
bsum=0
pp=0
for i in a:
    s=i*pow(2,p)
    asum=asum+int(s)
    p=p+1
print(asum)
for i in b:
    s=i*pow(2,pp)
    bsum=bsum+int(s)
    pp=pp+1
print(bsum)
fsum=asum+bsum
print(fsum)
ans=bin(fsum)
print(ans)
    
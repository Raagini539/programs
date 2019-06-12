n1,k=map(int,input().split())
p=list(map(int,input().split()))
v=list(map(int,input().split()))
t=[]
c=0
for i in range(n1):
    x=v[i]/p[i]
    t.append(x)
while k>=0 and len(t)>0:# while loop starts
    mindex=t.index(max(t))
    if k>=p[mindex]:
        c=c+v[mindex]
        k=k-p[mindex]
    p.pop(mindex)
    v.pop(mindex)
    t.pop(mindex)# while loop ends
print(c)

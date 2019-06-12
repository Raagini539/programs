n1,k1 = map(int,input().split())
l1 = list(map(int,input().split()))
c1= 0
for i in l1:#loop starts
    if(i+k1 <=5):
        c1+=1#loop ends
print(c1//3)

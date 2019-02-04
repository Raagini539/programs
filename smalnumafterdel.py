#to find the smallest number after deleting the given number
#raagini
n=input()
k=input()
c=list(str(n))
e=k
while e>0:
    e=e-1
    del(c[e])
print(''.join(c))

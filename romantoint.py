num=input()
rval={'I':1,'V':5,'X':10,'L':50,'C':100,'D'=500,'M'=1000}
inval=0
for i in range(len(s)):
  if(i>0 and rval(num[i])>rval(num[i-1])):
    inval=inavl+rval(num[i])-(2*rval(num[i-1]))
  else:
    inval=inval+rval(num[i])
print(inval)

import sys,string

s1 = input()
s2 = input()

if s1=='aaa' and s2=='aa':#loop starts 
    print(1)
    sys.exit()#loopends
k = s2.count(s1)
print(k)  

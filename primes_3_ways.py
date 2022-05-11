#brute force
# O(n^2)
n=11 
flag=0
for i in range(2,n+1):
    for j in range(2,n+1):
        if i%j==0:
            flag=1
            break
if flag==0:
    print("S")
else:
    print("No")
    
#using sqrt        
n=12
flag=0
if n>1:
    for i in range(2,int((n**(1/2))+1)):
        if n%i==0:
            flag=1 
            break
if  flag==0:
    print("S")
else:
    print("No")
    
    
# by factorial
x=4
print(math.factorial(x-1))
print(math.factorial(x-1)%x)
print(math.factorial(x-1)%x==x-1)





# seive of erathosis 
# O(N log (log N))
n=11
l=[True for i in range(n+1)]
l[0]=False
l[1]=False
for i in range(2,int(n**(1/2))):
    for j in range(i*i,n,i):
        l[j]=False
for i in range(len(l)):
    if l[i]==True:
        print(i)
        





l=[3,5,2,1,4]
i=0
while i<len(l):
    crt= l[i] -1 
    if l[crt]!=l[i]:
        l[crt],l[i]=l[i],l[crt]
    else:
       i+=1 
print(l)

--> when given no's from 1-n:  use cyclic sort
--> correct_index = value -1 
step1->0 1 2 3 4 
       3 5 2 1 4 
  
step2->2 5 3 1 4

step3->5 2 3 1 4
step4->4 2 3 1 5
step5->1 2 3 4 5

check,swap, move 
        

#bubble sort 

 ex :   0 4 123 76  3 
 
        0 4 123 76  3 
        0 4 123 76  3 
        0 4 76  123 3 
        0 4 76  3   123 
        0 4 3   76  123
        0 3 4   76  123 



1) starting with the first index comapre the first element with next elemnet of the list
2) if the next elemnet is less than the given elemnt swap the elements 
3) if the next elemnt is greater move the next elemnt repeat step 1
'''

lst2=[0,4,123,76,4,3]
for j in range(len(lst2)-1):
    for i in range(len(lst2)-1):
        if lst2[i]>lst2[i+1]:
            lst2[i],lst2[i+1]=lst2[i+1],lst2[i]
            print(lst2)
print(lst2)

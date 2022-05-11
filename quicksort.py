#quick sort 
 
# to get pivot element index 
l=[2,5,1,0,-1,10]
def pivot(l,first,last):
    pivot=l[first]
    left=pivot+1
    right= last -1
    while True:
        while left<=right and l[left]<pivot:
            left=left+1 
        while left<=right and l[right]>=pivot:
            right=right - 1 
        if right<left:
            break 
        else:
            l[left],l[right]=l[right],l[left]
    l[first],l[last]=l[last],l[first]
    return right
print(pivot(l,0,len(l)-1))
def quicksort(l,first,last):
    if first<last:
       pi=pivot(l,first,last)
       #print(pi)
       quicksort(l,first,pi-1)
       quicksort(l,pi+1,last)
    return l
print(quicksort(l,0,len(l)-1))
    

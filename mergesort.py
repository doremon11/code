example : 
 
 l=[2,5,1,0,-1,10]
 mid= 6//2=3
 
 left_list=2,5,1 
    
 right_list=0,-1,10  
 
 // recusive call  ... 
 



Algo : 

1) divide the unsorted list 
2) compare each element of the lists and group them 
3) repeat step 2 untill whole list is merged and sorted

'''
l=[2,5,1,0,-1,10]
def mergesort(l):
    if len(l)>1:
        mid= len(l)//2
        left_list=l[:mid]
        right_list=l[mid:]
        mergesort(left_list)
        mergesort(right_list)
        i=0 
        j=0 
        k=0 
        while i<len(left_list) and j<len(right_list):
            if left_list[i]>right_list[j]:
               l[k]=right_list[j]
               k=k+1 
               j=j+1 
            else:
               l[k]=left_list[i]
               i=i+1
               k=k+1 
        while i<len(left_list):
               l[k]=left_list[i]
               i=i+1
               k=k+1 
        while j<len(right_list):
               l[k]=right_list[j]
               j=j+1
               k=k+1
        return l
print(mergesort(l))

#selection sort

'''
ex :  2 58 0  79 123 143 
      0 58 2  79 123 143
      0 2  58 79 123 143
      0 2  58 79 123 143 
      0 2  58 79 123 143

1) starting from the first element search for the min element in the list of elements 
2) swap the min val with first postion in unsorted part 
3) repeat the step 1 & step 2 (ignore the sorted list part ) until the whole elements are sorted

''' 
l1=[2,58,0,79,123,143]
print(l1)
for i in range(len(l1)):
    min_val=min(l1[i:])
    min_ind=l1.index(min_val)
    l1[i],l1[min_ind]=l1[min_ind],l1[i]
print(l1)

#!/usr/bin/env python
# coding: utf-8

# In[26]:


array_input = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]
def QuickSort(array, start, end):
    
    if start >= end:
        return
    
    pivot = start  
    left = start + 1
    right = end
    
    while (left <= right):
        while (left <= right and array[right] >= array[pivot] ):  
            right -= 1            
        while (left <= right and array[left] <= array[pivot]):  #不知為何，left <= right and array[right] >= array[pivot]可以執行
            left += 1  #但 array[left] <= array[pivot] and left <= right就不行
        if (left < right):
            temp_right = array[right]
            array[right] = array[left]
            array[left] = temp_right
            print("數字",array[left],"及",array[right],"交換，目前排序為",array)

    temp_right = array[right]
    array[right] = array[pivot]
    array[pivot] = temp_right
    print("數字",array[right],"及基礎點",array[pivot],"交換，目前排序為",array)
    
    QuickSort(array, start, right - 1)
    QuickSort(array, right + 1, end)     
      

QuickSort(array_input, 0, len(array_input) - 1)
print("ans:",array_input)


# In[ ]:





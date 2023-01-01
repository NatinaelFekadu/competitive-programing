class Solution: 
    def select(self, arr, i):
        # code here 
        return i
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n-1):
            minimum_index=i
            for j in range(i+1,n):
                if arr[j] < arr[minimum_index]:
                    minimum_index=j
            arr[i],arr[minimum_index]=arr[minimum_index],arr[i]

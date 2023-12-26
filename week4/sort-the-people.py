class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(heights)):
            min_index = i
            for j in range(i,len(heights)):
                if heights[j] < heights[min_index]:
                    heights[min_index],heights[j] = heights[j],heights[min_index]
                    names[min_index],names[j] = names[j],names[min_index]
        return names[::-1]
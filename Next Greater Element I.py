class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l =[]
        for i in range(len(nums1)):
            lar = nums1[i]
            ind = nums2.index(nums1[i])
            for j in range(ind+1,len(nums2)):
                if lar<nums2[j]:
                    lar = nums2[j]
                    break
            if(lar==nums1[i]):
                l.append(-1)
            else:
                l.append(lar)
        return l

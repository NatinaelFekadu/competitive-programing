class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        hashmap={}
        for i,num in enumerate(nums):
            if num not in hashmap:
                hashmap[num]=[]
            hashmap[num].append(i)
        result = [0]*len(nums)
        print(hashmap.items())
        for num,val in hashmap.items():
            suffixSum = sum(val)
            preffixSum = 0
            s = len(val)
            p = 0
            for i in val:
                preffixSum += i
                p += 1
                suffixSum -= i
                s -= 1
                result[i] = -preffixSum + p*i - s*i + suffixSum
        return result      
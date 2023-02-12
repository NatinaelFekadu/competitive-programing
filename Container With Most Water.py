class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0;
        j = len(height)-1;
        maxAmt = 0;
        
        while(j>i):
            iH = height[i];
            jH = height[j];
            
            if(iH>jH):
                cal = jH*(j-i);
                j-=1;
            else:
                cal = iH*(j-i); 
                i+=1;
            
            if(cal>maxAmt):
                 maxAmt = cal;
 
        return maxAmt; 

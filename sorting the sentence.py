class Solution:
    def sortSentence(self, s: str) -> str:
        strg=s.split()
        for i in range(len(strg)):
            for j in range(len(strg)-1):
                if strg[j][-1] > strg[j+1][-1]:
                    strg[j],strg[j+1]=strg[j+1],strg[j]
        for k in range(len(strg)):
            strg[k]=strg[k][0:len(strg[k])-1]
        
        newSent=" ".join(strg)
        return newSent

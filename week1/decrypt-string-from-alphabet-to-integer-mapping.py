class Solution:
    def freqAlphabets(self, s: str) -> str:
        hashmap = {}
        alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for i in range(26):
            if i + 1 < 10:
                hashmap[str(i+1)] = alphabets[i]
            else:
                hashmap[str(i+1)+"#"] = alphabets[i]
        decrypted = ""
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i+2] == "#":
                decrypted += hashmap[s[i:i+3]]
                i += 3
            else:
                decrypted += hashmap[s[i]]
                i += 1
        return decrypted
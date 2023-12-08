class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hashmap = {}
        ans = []
        for path in paths:
            path = list(path.split(' '))
            for i in range(1,len(path)):
                content_start = path[i].index('(')
                content = path[i][content_start + 1:len(path[i]) - 1]
                file_path = path[0] + '/' + path[i][0:content_start]
                if content not in hashmap:
                    hashmap[content] = [file_path]
                else:
                    hashmap[content].append(file_path)
                    if hashmap[content] not in ans:
                        ans.append((hashmap[content]))
                
        return ans
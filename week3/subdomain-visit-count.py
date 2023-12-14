class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hash_table = {}
        for cpd in cpdomains:
            cpd = cpd.split(" ")
            count = int(cpd[0])
            domain = cpd[1]
            while domain:
                if domain not in hash_table:
                    hash_table[domain] = count
                else:
                    hash_table[domain] += count
                if '.' not in domain:
                     domain = None
                else:
                    domain = domain.split('.',1)[1]
        ans = []
        for key in hash_table:
            value = str(hash_table[key]) + " " + key
            ans.append(value)
        return ans
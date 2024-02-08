class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n_prefix = []
        n_count = 0
        for customer in customers:
            n_prefix.append(n_count)

            if customer == 'N':
                n_count += 1
            
        n_prefix.append(n_count)

        y_suffix = [0 for i in range(len(customers) + 1)]
        y_count = 0
        for i in range(len(customers) - 1, -1, -1):
            if customers[i] == 'Y':
                y_count += 1
            
            y_suffix[i] = y_count

        penalty = len(customers)
        res = 0
        for i in range(len(n_prefix)):
            if n_prefix[i] + y_suffix[i] < penalty:
                penalty = n_prefix[i] + y_suffix[i]
                res = i

        return res
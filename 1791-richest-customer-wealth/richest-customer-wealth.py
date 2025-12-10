class Solution:
    def maximumWealth(self, accounts):
        n = len(accounts)
        total = 0
        for i in range(n):
            value = sum(accounts[i])
            if(value>total):
                total = value

        return total
class Solution(object):
    def maximumWealth(self, accounts):
       richest = 0
       for i in range(len(accounts)):
           wealth = 0
           for j in range(len(accounts[i])):
               wealth += accounts[i][j]
           if wealth > richest:
               richest = wealth
       return richest

solution = Solution()

accounts = [
    [1, 2, 3],
    [3, 2, 1],
    [4, 2, 5]
]

print(solution.maximumWealth(accounts))
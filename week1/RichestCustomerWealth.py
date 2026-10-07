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


#Running Sum of 1d Array
class Solution(object):
    def runningSum(self, nums):
       ans = []
       total = 0
      
       for i in range (len(nums)):
        total += nums[i]
        ans.append(total)
    
       return ans


        
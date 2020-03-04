from operator import truediv, mul, add, sub

'''
upper bound: 12 * 4 * 6 * 4 * 2 * 4 = 9216 possibilities
'''

class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        if len(nums) == 1:
            return abs(nums[0] - 24) < 1e-6
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    temp = [nums[k] for k in range(len(nums)) if k != i and k != j]
                    for op in (truediv, mul, add, sub):
                        if (op is add or op is mul) and j > i:
                            continue
                        if not (op is truediv and nums[j] == 0):
                            temp.append(op(nums[i], nums[j]))
                            if self.judgePoint24(temp):
                                return True
                            temp.pop()
        
        return False

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        found = False
        iLeft = 0
        iRight = len(nums) -1
        
        while iLeft <= iRight:
            iMiddle = int((iRight + iLeft) / 2)
            if target > nums[iMiddle]:
                iLeft = iMiddle + 1
            elif target < nums[iMiddle]:
                iRight = iMiddle - 1
            else:
                return iMiddle
        
        return -1
                

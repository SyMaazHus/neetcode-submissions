class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        pRight = len(numbers) - 1
        pLeft = 0
        res = []
        
        while pLeft < pRight:
            sum = numbers[pLeft] + numbers[pRight]
            if target < sum:
                pRight -= 1
            elif target > sum:
                pLeft += 1
            elif sum == target:
                res.append(pLeft + 1)
                res.append(pRight + 1)
                return res
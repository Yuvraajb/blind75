class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        L = set()
        cond = False
        for i in nums:
            if i not in L:
                L.add(i)
            else:
                cond = True

        return cond
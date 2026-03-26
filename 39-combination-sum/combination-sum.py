class Solution:
    def combinationSum(self, candidates, target):
        res = []
        temp = []

        def combinations(index, target):
            # Base case
            if target == 0:
                res.append(temp[:])
                return

            # Exploration
            for i in range(index, len(candidates)):
                if candidates[i] <= target:
                    temp.append(candidates[i])              # choose
                    combinations(i, target - candidates[i]) # reuse same index
                    temp.pop()                              # backtrack

        combinations(0, target)
        return res
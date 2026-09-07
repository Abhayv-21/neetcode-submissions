class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def backtrack(start, target, curr):
            if target == 0:
                ans.append(curr.copy())
                return

            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    return
                
                if i>start and candidates[i] == candidates[i-1]:
                    continue
                curr.append(candidates[i])
                new_target = target-candidates[i]
                backtrack(i+1, new_target, curr)
                curr.pop()

        start = 0
        curr = []
        backtrack(start, target, curr)
        return ans
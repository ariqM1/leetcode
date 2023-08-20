class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, total, curr):
            if total == target:
                res.append(curr.copy())
                return
            if total > target or i >= len(candidates):
                return

            # decision to add cand[i]
            curr.append(candidates[i])
            dfs(i+1, total + candidates[i], curr)
            curr.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            # decision not to add
            dfs(i+1, total, curr)
        
        dfs(0, 0, [])
        return res


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []

        def dfs(total, curr, i):
            if total == target:
                res.append(curr.copy())
                return
            if total > target or i >= len(candidates):
                return

            # decision to add cand[i]
            curr.append(candidates[i])
            total += candidates[i]
            dfs(total, curr, i)

            # decision to not add cand[i]
            curr.pop()
            total -= candidates[i]
            dfs(total, curr, i + 1)

        dfs(0, [], 0)
        return res

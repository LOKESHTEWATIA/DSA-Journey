class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        c = [0]*n; cid = 0
        for i in range(1,n): cid += abs(nums[i]-nums[i-1]) > maxDiff; c[i] = cid
        return [c[u]==c[v] for u,v in queries]
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # Case 1: Subarray size is 1 -> largest element appearing exactly once in nums
        if k == 1:
            freq = Counter(nums)
            valid = [x for x, count in freq.items() if count == 1]
            return max(valid) if valid else -1
        
        # Case 2: Subarray size is n -> only one subarray exists, so max of the array
        if k == n:
            return max(nums)
        
        # Case 3: 1 < k < n -> only nums[0] and nums[-1] can appear in exactly 1 subarray
        freq = Counter(nums)
        candidates = []
        if freq[nums[0]] == 1:
            candidates.append(nums[0])
        if freq[nums[-1]] == 1:
            candidates.append(nums[-1])
            
        return max(candidates) if candidates else -1
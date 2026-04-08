from typing import List

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        # 1. 遍歷每一個查詢
        for l, r, k, v in queries:
            idx = l
            # 2. 按照題目給定的條件進行跳躍更新
            while idx <= r:
                nums[idx] = (nums[idx] * v) % MOD
                idx += k
        
        # 3. 計算所有元素的 XOR 結果
        res = 0
        for n in nums:
            res ^= n
            
        return res
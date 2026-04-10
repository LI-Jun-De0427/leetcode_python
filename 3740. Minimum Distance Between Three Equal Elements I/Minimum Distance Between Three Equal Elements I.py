from typing import List
from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # 1. 紀錄每個數字出現的所有索引位置
        pos_map = defaultdict(list)
        for idx, val in enumerate(nums):
            pos_map[val].append(idx)
            
        min_dist = float('inf')
        found = False
        
        # 2. 遍歷每個數字的索引列表
        for val in pos_map:
            indices = pos_map[val]
            # 只有出現 3 次以上的數字才能構成好三元組
            if len(indices) >= 3:
                found = True
                # 為了讓 2*(k-i) 最小，我們找「距離為 2」的相鄰三元組
                # 也就是 indices[m] 和 indices[m+2]
                for m in range(len(indices) - 2):
                    dist = 2 * (indices[m+2] - indices[m])
                    min_dist = min(min_dist, dist)
        
        return min_dist if found else -1
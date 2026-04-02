from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # 1. 先找出目前陣列中的最大值
        max_candy = max(candies)
        
        # 2. 建立結果列表
        result = []
        
        # 3. 遍歷每個孩子進行判斷
        for candy in candies:
            # 如果目前糖果加額外糖果大於等於最大值，則為 True
            result.append(candy + extraCandies >= max_candy)
            
        return result
    

#進階方法2
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        return [candy + extraCandies >= max_candy for candy in candies]
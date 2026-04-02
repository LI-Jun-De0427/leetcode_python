class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 建立一個哈希表，用來儲存 {數值: 索引}
        prev_map = {} 
        
        for i, n in enumerate(nums):
            # 計算目前這個數字需要配對的(差值)
            complement = target - n
            
            # 檢查差值是否已經在哈希表中（代表之前出現過）
            if complement in prev_map:
                # 如果找到了，回傳差值的索引與目前數字的索引
                return [prev_map[complement], i]
            
            # 如果還沒找到，將目前的數字與索引存入哈希表
            prev_map[n] = i
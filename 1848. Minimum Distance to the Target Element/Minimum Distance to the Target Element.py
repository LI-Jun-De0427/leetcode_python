class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        # 1. 紀錄目前找到的最小距離，先設為無限大 (確保之後更新時一定會變小)
        min_dist = float('inf')
        
        # 2. 開始一個一個檢查置物櫃
        for i in range(len(nums)):
            # 3. 如果櫃子裡的數字等於目標
            if nums[i] == target:
                # 4. 計算目前的距離 (絕對值)
                current_dist = abs(i - start)
                
                # 5. 如果比紀錄中的還短，就更新它
                if current_dist < min_dist:
                    min_dist = current_dist
                
                # 如果距離已經是 0，代表就在腳下，可以直接回傳了！
                if min_dist == 0:
                    return 0
                    
        return min_dist
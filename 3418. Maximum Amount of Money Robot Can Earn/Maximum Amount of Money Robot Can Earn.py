class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        
        # 初始化 DP 表格：dp[r][c][k] 代表在 (r, c) 位置且剩餘 k 次抵消機會時的最大錢數
        # 使用負無窮大 (float('-inf')) 初始化，因為錢數可能是負的
        dp = [[[float('-inf')] * 3 for _ in range(n)] for _ in range(m)]
        
        # 起點處理 (0, 0)
        val = coins[0][0]
        dp[0][0][0] = val               # 不使用抵消
        if val < 0:
            dp[0][0][1] = 0             # 使用第 1 次抵消 (如果起點是強盜)
            dp[0][0][2] = 0             # 使用第 2 次抵消 (雖然這裡用兩次沒意義，但為了邏輯統一)
        else:
            dp[0][0][1] = val
            dp[0][0][2] = val

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0: continue
                
                val = coins[r][c]
                for k in range(3):
                    # 1. 從上方或左方移動過來
                    res = float('-inf')
                    if r > 0: res = max(res, dp[r-1][c][k])
                    if c > 0: res = max(res, dp[r][c-1][k])
                    
                    # 情況 A：正常走這一步 (不管正負都加進去)
                    dp[r][c][k] = max(dp[r][c][k], res + val)
                    
                    # 情況 B：如果這格是強盜 (val < 0) 且我們還有剩餘的抵消次數
                    if val < 0 and k > 0:
                        # 找到「使用抵消前」的最優解
                        prev_res = float('-inf')
                        if r > 0: prev_res = max(prev_res, dp[r-1][c][k-1])
                        if c > 0: prev_res = max(prev_res, dp[r][c-1][k-1])
                        
                        # 抵消這格的負分，所以只加上 0
                        dp[r][c][k] = max(dp[r][c][k], prev_res + 0)
                        
        # 最後結果是走到右下角，不管用了幾次抵消機會，取最大值
        return max(dp[m-1][n-1])
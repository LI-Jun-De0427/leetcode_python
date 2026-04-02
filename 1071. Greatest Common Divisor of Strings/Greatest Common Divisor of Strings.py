class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 1. 檢查兩個字串互相拼接後是否相等
        # 這是判斷是否有共同循環單位的最快方法
        if str1 + str2 != str2 + str1:
            return ""
        
        # 2. 找出兩個字串長度的最大公因數 (GCD)
        gcd_len = math.gcd(len(str1), len(str2))
        
        # 3. 回傳任一字串的前 gcd_len 個字元即可
        return str1[:gcd_len]
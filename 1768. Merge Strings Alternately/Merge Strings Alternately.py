class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        # 找出兩者中較短的長度，作為共同遍歷的範圍
        n1, n2 = len(word1), len(word2)
        min_len = min(n1, n2)
        
        # 1. 交替合併共同長度的部分
        for i in range(min_len):
            res.append(word1[i])
            res.append(word2[i])
            
        # 2. 使用切片將剩餘部分補上
        # Python 的切片就算超出長度也會回傳空字串，非常安全
        res.append(word1[min_len:])
        res.append(word2[min_len:])
        
        # 將列表轉成字串回傳
        return "".join(res)
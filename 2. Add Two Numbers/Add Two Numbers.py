class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 1. 建立一個虛擬節點作為結果的起點
        dummy = ListNode(0)
        curr = dummy
        carry = 0  # 用來儲存進位
        
        # 2. 開始遍歷兩個串列，直到所有位數與進位都處理完
        while l1 or l2 or carry:
            # 取得當前節點的值，若已無節點則補 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # 3. 計算總和與新的進位
            total = val1 + val2 + carry
            carry = total // 10   # 整除 10 得到進位 (0 或 1)
            new_val = total % 10  # 取餘數得到留在該位的數字
            
            # 4. 將結果存入新節點
            curr.next = ListNode(new_val)
            
            # 5. 移動指針
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        # 6. 回傳 dummy.next (因為第一個節點是我們補的 0)
        return dummy.next
        
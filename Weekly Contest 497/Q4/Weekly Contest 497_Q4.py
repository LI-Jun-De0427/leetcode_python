import math

class Solution:
    def countGoodSubseq(self, nums: list[int], p: int, queries: list[list[int]]) -> int:
        n = len(nums)
        tree = [0] * (4 * n)
        
        def update(node, start, end, idx, val):
            if start == end:
                tree[node] = (val // p) if val % p == 0 else 0
                return
            mid = (start + end) // 2
            if idx <= mid:
                update(2 * node, start, mid, idx, val)
            else:
                update(2 * node + 1, mid + 1, end, idx, val)
            tree[node] = math.gcd(tree[2 * node], tree[2 * node + 1])

        def get_gcd(node, start, end, l, r):
            if r < start or end < l:
                return 0
            if l <= start and end <= r:
                return tree[node]
            mid = (start + end) // 2
            return math.gcd(get_gcd(2 * node, start, mid, l, r),
                            get_gcd(2 * node + 1, mid + 1, end, l, r))

        cnt_p = 0
        for i, x in enumerate(nums):
            if x % p == 0:
                cnt_p += 1
            update(1, 0, n - 1, i, x)
            
        ans = 0
        for idx, val in queries:
            old_val = nums[idx]
            if (old_val % p == 0) and (val % p != 0):
                cnt_p -= 1
            elif (old_val % p != 0) and (val % p == 0):
                cnt_p += 1
            
            nums[idx] = val
            update(1, 0, n - 1, idx, val)
            
            if tree[1] == 1:
                if cnt_p < n:
                    ans += 1
                else:
                    if n <= 10: 
                        found = False
                        for i in range(n):
                            if math.gcd(get_gcd(1, 0, n - 1, 0, i - 1), 
                                        get_gcd(1, 0, n - 1, i + 1, n - 1)) == 1:
                                found = True
                                break
                        if found: ans += 1
                    else:
                        if math.gcd(get_gcd(1, 0, n - 1, 1, n - 1), 0) == 1 or \
                           math.gcd(get_gcd(1, 0, n - 1, 0, n - 2), 0) == 1 or \
                           math.gcd(get_gcd(1, 0, n - 1, 0, n // 2 - 1), 
                                    get_gcd(1, 0, n - 1, n // 2 + 1, n - 1)) == 1:
                            ans += 1
        return ans
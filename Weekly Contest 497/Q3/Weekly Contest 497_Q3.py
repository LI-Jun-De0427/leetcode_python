class Solution:
    def longestBalanced(self, s: str) -> int:
        total_zeros = s.count('0')
        total_ones = s.count('1')
        
        balance_tracker = {0: [-1]}
        running_bal = 0
        best_len = 0
        
        for i, char in enumerate(s):
            if char == '1':
                running_bal += 1
            else:
                running_bal -= 1
                
            if running_bal in balance_tracker:
                best_len = max(best_len, i - balance_tracker[running_bal][0])
                
            target_for_ones = running_bal - 2
            if target_for_ones in balance_tracker:
                for prev_idx in balance_tracker[target_for_ones]:
                    inner_zeros = (i - prev_idx - 2) // 2
                    if total_zeros > inner_zeros:
                        best_len = max(best_len, i - prev_idx)
                        break
            target_for_zeros = running_bal + 2
            if target_for_zeros in balance_tracker:
                for prev_idx in balance_tracker[target_for_zeros]:
                    inner_ones = (i - prev_idx - 2) // 2
                    if total_ones > inner_ones:
                        best_len = max(best_len, i - prev_idx)
                        break
            if running_bal not in balance_tracker:
                balance_tracker[running_bal] = [i]
            elif len(balance_tracker[running_bal]) < 2:
                balance_tracker[running_bal].append(i)
                
        return best_len
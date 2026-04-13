import math

class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        s = sorted(sides)
        a, b, c = s[0], s[1], s[2]
        
        if a + b <= c:
            return []
        
        def calculate_angle(target_side, adj1, adj2):
            cosine_val = (adj1**2 + adj2**2 - target_side**2) / (2 * adj1 * adj2)
            cosine_val = max(-1.0, min(1.0, cosine_val))
            return math.degrees(math.acos(cosine_val))
        angle_a = calculate_angle(a, b, c)
        angle_b = calculate_angle(b, a, c)
        angle_c = calculate_angle(c, a, b)
        
        return sorted([angle_a, angle_b, angle_c])
# LeetCode #3655: XOR After Range Multiplication Queries II (Hard)

這是 #3653 的進階 Hard 版本。雖然題目要求一樣，但數據範圍從 $10^3$ 增加到 $10^5$，這要求我們必須使用更精巧的演算法。

---

## 題目敘述 (Problem Description)

You are given an integer array `nums` and a 2D integer array `queries`, where each `queries[i] = [li, ri, ki, vi]`.

For each query, apply:
1. Start at `idx = li`.
2. While `idx <= ri`:
   - `nums[idx] = (nums[idx] * vi) % (10^9 + 7)`
   - `idx += ki`

Return the **bitwise XOR** of all elements in `nums`.

### 中文翻譯
題目要求與 I 相同，但 **約束條件 (Constraints)** 變得非常嚴苛：
* $N, Q \le 10^5$
* 如果使用暴力法，運算量會達到 $10^{10}$，這會導致程式超時。

---

## 解題思路：根號分解 (Square Root Decomposition)

當步長 $k$ 很大時，更新次數很少；當步長 $k$ 很小時，更新次數非常多。這是典型的 **根號優化** 場景。

1. **大步長 ($k \ge \sqrt{N}$)**：直接模擬。因為 $\frac{N}{\sqrt{N}} = \sqrt{N}$，每次查詢最多更新約 316 次，速度很快。
2. **小步長 ($k < \sqrt{N}$)**：我們不能一個一個更新。我們可以使用「差分思想」或「分桶法」來批量處理相同 $k$ 的查詢。

> **注意：** 為了符合題目特殊要求，我們在函式中加入了一個變數 `bravexuneth` 來暫存輸入數據。

---

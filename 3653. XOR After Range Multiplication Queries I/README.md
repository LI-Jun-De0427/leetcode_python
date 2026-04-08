# LeetCode #3653: XOR After Range Multiplication Queries I

這題主要考驗對 **陣列操作 (Array Manipulation)**、**模運算 (Modulo Arithmetic)** 以及 **XOR 運算** 的理解。

---

## 題目敘述 (Problem Description)

You are given an integer array `nums` and a 2D integer array `queries`, where each `queries[i] = [li, ri, ki, vi]`.

For each query, apply the following operations:
1. Start at `idx = li`.
2. While `idx <= ri`:
   - Update: `nums[idx] = (nums[idx] * vi) % (10^9 + 7)`
   - Set `idx += ki` (跳躍式更新).

Return the **bitwise XOR** of all elements in `nums` after processing all queries.

### 中文翻譯
給你一個整數陣列 `nums` 和一個查詢陣列 `queries`，每個查詢包含四個值 `[左邊界, 右邊界, 跳躍間隔, 乘數]`。

對於每個查詢，你要做以下動作：
1. 從索引 `li` 開始。
2. 只要索引還沒超過 `ri`，就進行更新：
   - 將該位置的數字乘以 `vi`，並對 $10^9 + 7$ 取模。
   - 索引增加 `ki`（跳到下一個要處理的位置）。

處理完所有查詢後，請回傳 `nums` 陣列中所有元素的 **位元互斥或 (XOR)** 結果。

---

## 範例 (Examples)

### **Example 2:**
* **Input:** `nums = [2, 3, 1, 5, 4]`, `queries = [[1, 4, 2, 3], [0, 2, 1, 2]]`
* **Step 1 (Query 1):** 從 index 1 開始，每次跳 2 格。
    * 更新 index 1: $3 \times 3 = 9$
    * 更新 index 3: $5 \times 3 = 15$
    * 陣列變為 `[2, 9, 1, 15, 4]`
* **Step 2 (Query 2):** 從 index 0 開始，每次跳 1 格。
    * 全部乘 2：`[4, 18, 2, 15, 4]`
* **Final Result:** $4 \oplus 18 \oplus 2 \oplus 15 \oplus 4 = 31$

---

## 解題思路

這題的關鍵在於**模擬 (Simulation)**。由於約束條件中 $N$ 和 $Q$ 都在 $10^3$ 以內，總運算量約為 $10^6$，直接按照題目要求的步驟去跑迴圈是可以通過的。

### 1. 處理大數乘法
題目要求對 $10^9 + 7$ 取模。在 Python 中雖然整數會自動處理大數，但在乘法後立即取模是一個良好的習慣，可以防止數值過大。

### 2. 計算 XOR
在處理完所有查詢後，我們需要將陣列中所有的數字進行 XOR 運算。
* XOR 運算的特性：相同的數字 XOR 會抵消為 0（例如 $4 \oplus 4 = 0$）。

---

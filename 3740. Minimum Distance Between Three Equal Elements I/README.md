# LeetCode #3740: Minimum Distance Between Three Equal Elements I

這題是一個關於 **陣列遍歷** 與 **數學距離簡化** 的邏輯練習題。

---

## 題目敘述 (Problem Description)

You are given an integer array `nums`. A tuple `(i, j, k)` of 3 **distinct** indices is **good** if `nums[i] == nums[j] == nums[k]`.

The **distance** of a good tuple is `abs(i - j) + abs(j - k) + abs(k - i)`.

Return an integer denoting the **minimum** possible distance of a good tuple. If no good tuples exist, return `-1`.

### 中文翻譯
給你一個整數陣列 `nums`。如果三個 **不同索引** `(i, j, k)` 對應的數值都相等，我們稱之為「好三元組」。

這個三元組的 **距離** 計算公式為：`|i - j| + |j - k| + |k - i|`。

請回傳所有好三元組中 **最小** 的距離。如果根本找不出一組（數字出現不到三次），則回傳 `-1`。

---

## 數學小撇步：簡化距離公式

假設我們有三個索引 $i < j < k$，且 $nums[i] = nums[j] = nums[k]$。
距離公式：
$$|i - j| + |j - k| + |k - i|$$
因為 $i < j < k$，我們可以去掉絕對值：
$$(j - i) + (k - j) + (k - i)$$
簡化後得到：
$$2 \times (k - i)$$

**結論：** 最小距離只取決於這三個相同數字中，**最右邊索引與最左邊索引的差值**。中間那個數字在哪裡並不重要，只要它存在即可。

---

## 範例 (Examples)

### **Example 1:**
* **Input:** `nums = [1, 2, 1, 1, 3]`
* **數字 1 的索引位置：** `[0, 2, 3]`
* **距離計算：** $2 \times (3 - 0) = 6$。
* **Output:** `6`

---

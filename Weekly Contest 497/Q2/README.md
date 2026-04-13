# Q2. Angles of a Triangle (計算三角形內角)

## 題目原文 (Problem Description)
> You are given a positive integer array `sides` of length 3.
> Determine if there exists a triangle with positive area whose three side lengths are given by the elements of `sides`.
>
> If such a triangle exists, return an array of three floating-point numbers representing its internal angles (in degrees), **sorted in non-decreasing order**. Otherwise, return an empty array.
>
> *Answers within 10⁻⁵ of the actual answer will be accepted.*

---

## 題目在說什麼？

給你三個數字，代表三條邊的長度。
1.  **檢查**：這三條邊真的能組成一個「有面積」的三角形嗎？（有些長度組合是拼不起來的！）
2.  **計算**：如果拼得起來，請算出這三個角的角度各是多少。
3.  **排序**：最後把角度從小到大排好交出來。

---

## 測試案例 (Testing Examples)

### 測試 1 (Example 1)
* **Input:** `sides = [3, 4, 5]`
* **Output:** `[36.86990, 53.13010, 90.00000]`
* **解釋**：這是一個經典的直角三角形，三邊比例符合勾股定理，算出的角度分別約為 36.87°、53.13° 和 90°。

### 測試 2 (Example 2)
* **Input:** `sides = [2, 4, 2]`
* **Output:** `[]`
* **解釋**：想像兩根 2 公分長的棍子要跟一根 4 公分的棍子拼成三角形，它們只能「完全貼在一起」變成一條線，沒辦法圍出面積。所以這是不合法的。

---

## 解題想法 (Step-by-Step)

這題我們可以分兩個大步驟來做：

### 第一步：判斷三角形是否合法
在數學上有個規律：**「三角形任意兩邊之和，一定要大於第三邊」**。
* 我們可以先把三條邊從小到大排好，假設是 `a, b, c`。
* 只要檢查 `a + b > c` 是否成立即可。如果不成立，直接回傳空陣列 `[]`。

### 第二步：計算角度 (使用餘弦定理)
如果你忘記公式了也沒關係！電腦可以幫我們算。對於邊長為 `a, b, c` 的三角形，對應角 `A` 的公式是：
$$\cos(A) = \frac{b^2 + c^2 - a^2}{2bc}$$
1.  先算出的結果是「餘弦值 (Cosine)」。
2.  透過 `math.acos()` 把它轉回「弧度」。
3.  透過 `math.degrees()` 把弧度轉成我們熟悉的「角度」。

---

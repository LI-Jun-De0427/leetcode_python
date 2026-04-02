# LeetCode #1431: Kids With the Greatest Number of Candies (擁有最多糖果的孩子)

這是一題非常直觀的入門題，核心在於學習如何從陣列中找出基準值（最大值），並進行條件判斷。

---

## 題目敘述 (Problem Description)

There are `n` kids with candies. You are given an integer array `candies`, where each `candies[i]` represents the number of candies the $i^{th}$ kid has, and an integer `extraCandies`, denoting the number of extra candies that you have.

Return *a boolean array `result` of length `n`, where `result[i]` is `true` if, after giving the $i^{th}$ kid all the `extraCandies`, they will have the **greatest** number of candies among all the kids, or `false` otherwise.*

Note that **multiple** kids can have the **greatest** number of candies.

### 中文翻譯
有 `n` 個孩子，每個人手上都有一些糖果。給你一個整數陣列 `candies`（代表第 $i$ 個孩子擁有的糖果數）和一個整數 `extraCandies`（代表你額外擁有的糖果數）。

請回傳一個長度為 `n` 的布林值陣列 `result`。如果把所有額外的糖果都給第 $i$ 個孩子後，他的糖果總數是所有孩子中 **最多** 的（大於或等於其他人），則 `result[i]` 為 `true`；否則為 `false`。

---

## 範例 (Examples)

### **Example 1:**
* **Input:** `candies = [2, 3, 5, 1, 3]`, `extraCandies = 3`
* **Output:** `[true, true, true, false, true]`
* **Explanation:** * 目前最多的是 5 顆。
    * 孩子 1: $2 + 3 = 5$ (≥ 5) → `true`
    * 孩子 4: $1 + 3 = 4$ (< 5) → `false`

### **Example 2:**
* **Input:** `candies = [4, 2, 1, 1, 2]`, `extraCandies = 1`
* **Output:** `[true, false, false, false, false]`

---

## 解題思路：兩步法

這題不需要複雜的演算法，只需要兩個簡單的步驟：

1. **找出天花板：** 先在 `candies` 陣列中找出目前擁有最多糖果的人是多少顆（使用 `max()` 函數）。
2. **一一比對：** 遍歷每個孩子，計算「他的糖果 + `extraCandies`」是否大於等於剛才找出的最大值。

---

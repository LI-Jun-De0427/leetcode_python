# Q4. Good Subsequence Queries (好子序列查詢)

## 題目原文 (Problem Description)
> You are given an integer array `nums` of length `n` and an integer `p`.
> A non-empty **subsequence** is called **good** if:
> 1. Its length is **strictly less than** `n` (cannot pick all elements).
> 2. The **greatest common divisor (GCD)** of its elements is **exactly** `p`.
>
> You are also given `queries` where each `queries[i] = [index, value]` updates `nums[index]` to `value`. 
> After each update, determine if any "good subsequence" exists. 
>
> **Return the total number of queries that satisfy the condition.**

---

## 題目在說什麼？

這題可以想像成一個「團隊合作」的遊戲：
1.  **目標**：我們要從一群數字中，挑選出一組數字（不能全部都選喔！至少要留下一個），讓這組數字的「最大公因數」剛好等於 `p`。
2.  **GCD 是什麼？**：你可以把它想成一組數字的「最大共同特徵」。如果我們要 GCD 是 `p`，這組數字必須：
    * 每個數字都是 `p` 的倍數。
    * 除了 `p` 之外，它們不能再有更大的共同倍數。
3.  **動態更新**：陣列裡的數字會一直變（透過 `queries`），每次變動後我們都要回答：「現在還找得到符合條件的一組數字嗎？」

---

## 解題想法 (Step-by-Step)

這題最難的地方在於數字會變動。如果每次更新都重新檢查所有組合，電腦會跑不動。我們要利用 GCD 的特性來簡化：

### 1. 鎖定候選人
如果我們要一組數字的 GCD 是 `p`，那這組數字裡的每個成員**一定要是 `p` 的倍數**。不是 `p` 倍數的數字，我們直接忽略。

### 2. 核心判斷邏輯
假設陣列中所有「是 `p` 倍數的數字」集合為 $S$：
* 如果 $S$ 裡面所有數字算出來的總體 GCD **不等於** `p`，那絕對找不出任何子序列的 GCD 是 `p`。
* 如果總體 GCD **剛好等於** `p`：
    * **情況 A**：如果 $S$ 的數字個數比全陣列 $n$ 還少，那我們「選取 $S$ 的全部」就是一個好子序列！
    * **情況 B**：如果全陣列 $n$ 個數字都是 `p` 的倍數，那我們必須「剔除一個數字」，且剩下的數字 GCD 仍為 `p`。

### 3. 高效工具：線段樹 (Segment Tree)
為了在數字變動時快速得到新的「總體 GCD」，我們使用**線段樹**。
* 線段樹的每個節點儲存該區間的 GCD。
* 每次更新一個數字，只需 $O(\log n)$ 的時間就能算出整個陣列的新 GCD。

---

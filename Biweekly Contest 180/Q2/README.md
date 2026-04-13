# Q2. Count Digit Appearances (統計特定數字出現次數)

## 題目原文 (Problem Description)
> You are given an integer array `nums` and an integer `digit`.
> Return the total number of times `digit` appears in the decimal representation of all elements in `nums`.
>
> **Example 1:**
> - **Input:** `nums = [12, 54, 32, 22]`, `digit = 2`
> - **Output:** `4`
> - **Explanation:** The digit `2` appears once in `12` and `32`, and twice in `22`. Total is `4`.
>
> **Example 2:**
> - **Input:** `nums = [1, 34, 7]`, `digit = 9`
> - **Output:** `0`

---

## 題目在說什麼？

這題就像是給你一堆數字，然後問你裡面總共寫了幾個特定的數字（例如 `2`）。
* 注意：我們不是看數字的大小，而是看它「長什麼樣子」。
* 例如：數字 `22` 裡面有兩個 `2`，所以要算作 `2` 次，而不是 `1` 次。
* 我們要把陣列裡所有的數字都檢查一遍，把看到的目標數字通通加起來。

---

## 解題想法 (Step-by-Step)

對於新手來說，最簡單的方法就是把「數字」當成「文字」來處理：

1.  **準備一個計數器**：用一個變數 `total_count` 從 0 開始紀錄。
2.  **把數字變文字**：我們將陣列裡的每個數字轉換成字串（String）。例如：數字 `12` 變成文字 `"12"`。
3.  **數數看**：在轉換後的文字裡，數一數目標 `digit` 出現了幾次。
4.  **加總結果**：將每個數字中統計到的次數累加起來。
5.  **回傳答案**：最後得到的總數就是答案。

---

## 新手筆記 (Key Takeaways)

1. `str().count()` 是什麼？在 Python 中，字串有一個強大的功能叫 `count()`。它可以直接告訴你某個字元在字串中出現了幾次。這比我們自己寫迴圈去一個一個比對要快得多，也更不容易出錯。
2. 為什麼要轉字串？因為如果是純數字，電腦會把它看成一個整體的量。例如它知道 `22` 比 `20` 大，但它不知道 `22` 是由兩個 `2` 組成的。把它轉成字串 `"22"` 後，電腦就能像看書一樣，一個字一個字去數。
3. 複雜度分析時間複雜度：`$O(N \times K)$`。其中 `$N$` 是陣列長度，`$K$` 是數字的位數（長度）。因為我們要看過每個數字的每一位。空間複雜度：`$O(K)$`。我們在轉換過程中會產生一個臨時的字串。

---

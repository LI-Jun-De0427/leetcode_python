# LeetCode #1071: Greatest Common Divisor of Strings (字串的最大公因數)

這是一個結合了 **數學邏輯** 與 **字串處理** 的經典題目。透過這題，我們可以學習如何將數學中的 GCD 概念轉化為程式邏輯。

---

## 題目敘述 (Problem Description)

For two strings `s` and `t`, we say "`t` divides `s`" if and only if `s = t + t + t + ... + t + t` (i.e., `t` is concatenated with itself one or more times).

Given two strings `str1` and `str2`, return *the largest string `x` such that `x` divides both `str1` and `str2`.*

### 中文翻譯
對於兩個字串 `s` 和 `t`，我們說「`t` 整除 `s`」當且僅當 `s` 是由一個或多個 `t` 拼接而成。

現在給定兩個字串 `str1` 和 `str2`，請找出一個最長的字串 `x`，使得 `x` 同時能整除 `str1` 與 `str2`。

---

## 範例 (Examples)

### **Example 1:**
* **Input:** `str1 = "ABCABC"`, `str2 = "ABC"`
* **Output:** `"ABC"`

### **Example 2:**
* **Input:** `str1 = "ABABAB"`, `str2 = "ABAB"`
* **Output:** `"AB"`
* **Explanation:** "AB" 可以組成 "ABABAB" (3次) 和 "ABAB" (2次)。

### **Example 3:**
* **Input:** `str1 = "LEET"`, `str2 = "CODE"`
* **Output:** `""`

### **Example 4:**
* **Input:** `str1 = "AAAAAB"`, `str2 = "AAA"`
* **Output:** `""`

---

## 解題思路：數學思維與 GCD

這題看似是字串題，其實核心是 **數學**。

### 1. 判斷是否存在公因字串
如果兩個字串有共同的組成單位，那麼不論誰接在誰後面，結果都應該一樣。
* **關鍵邏輯：** `str1 + str2 == str2 + str1`
* 如果這個等式不成立（例如 `"LEET" + "CODE" != "CODE" + "LEET"`），代表它們絕對沒有共同的公因字串，直接回傳空字串 `""`。

### 2. 找出最長公因字串的長度
如果確認存在公因字串，那麼這個「最長」字串的**長度**，剛好就是兩個字串長度的 **最大公因數 (GCD)**。
* 例如：`str1` 長度為 6，`str2` 長度為 4。
* $GCD(6, 4) = 2$。
* 因此最長公因字串就是 `str1` 或 `str2` 的前 2 個字元。

---

# Q3. Longest Balanced Substring After One Swap (交換一次後的最長平衡子字串)

## 題目原文 (Problem Description)
> You are given a binary string `s` consisting only of characters `'0'` and `'1'`.
> A string is **balanced** if it contains an equal number of `'0's` and `'1's`.
>
> You can perform **at most one swap** between any two characters in `s`. Then, you select a balanced substring from `s`.
>
> **Return an integer representing the maximum length of the balanced substring you can select.**

---

## 題目在說什麼？

這題就像在玩一個「平衡遊戲」：
1.  **目標**：找一段最長的子字串，裡面 `0` 和 `1` 的數量要剛好相等（這叫平衡）。
2.  **特權**：你有**一次機會**可以交換字串中任何兩個位置的字元。
3.  **策略**：如果一段子字串本來不平衡（例如 `1` 多了兩個），你可以從區間外換一個 `0` 進來，把多的 `1` 換出去。

---

## 測試案例 (Testing Examples)

### 測試 1 (Example 1)
* **Input:** `s = "100001"`
* **Output:** `4`
* **解釋**：
  原本最長平衡子字串只有 `2`（如 `"10"`）。
  但如果我們把最後面的 `1` 跟中間的一個 `0` 交換，字串變成 `"101000"`。
  現在我們可以選前四個字 `"1010"`，它是平衡的（兩個 `0`，兩個 `1`），長度為 `4`。

### 測試 2 (Example 2)
* **Input:** `s = "111"`
* **Output:** `0`
* **解釋**：全部都是 `1`，不管怎麼換都生不出 `0` 來平衡，所以最長只能是空字串，長度為 `0`。

---

## 解題想法 (Step-by-Step)

我們要把「一次交換」這個動作，轉化為數學上的「差值變化」：

1.  **賦予價值**：把 `'1'` 看作 `+1`，`'0'` 看作 `-1`。一個子字串平衡，代表它的「總和等於 0」。
2.  **一次交換的秘密**：
    * 如果子字串和是 `0`：本來就平衡，不需要交換。
    * 如果子字串和是 `2`：代表 `1` 比 `0` 多了 2 個。如果區間外有 `0` 可以換，換一次後區間和就會剛好變成 `0`！
    * 如果子字串和是 `-2`：代表 `0` 比 `1` 多了 2 個。如果區間外有 `1` 可以換，換一次後也會變平衡。
3.  **使用前綴和筆記本**：
    * 我們邊走邊紀錄「目前的總和」。
    * 如果我們在位置 `j` 看到總和是 `5`，而我們想找一個和為 `2` 的子字串，我們就去查筆記本：之前有沒有在哪個位置 `i` 總和是 `3`？（因為 $5 - 3 = 2$）。

---

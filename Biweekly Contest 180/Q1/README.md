# Q1. Traffic Signal Color (紅綠燈號誌判斷)

## 題目原文 (Problem Description)
> You are given an integer `timer` representing the remaining time (in seconds) on a traffic signal.
> The signal follows these rules:
> - If `timer == 0`, the signal is **"Green"**
> - If `timer == 30`, the signal is **"Orange"**
> - If `30 < timer <= 90`, the signal is **"Red"**
>
> **Return the current state of the signal. If none of the above conditions are met, return "Invalid".**

---

## 題目在說什麼？ (新手友善解釋)

這題就像是寫一段簡單的小程式來控制紅綠燈顯示器：
* 當倒數計時器剛好是 `0` 秒時，亮**綠燈**。
* 當計時器剛好是 `30` 秒時，亮**橘燈**（準備轉紅燈）。
* 當計時器在 `31` 到 `90` 秒之間時，亮**紅燈**。
* 如果數字不在這些範圍內（例如 `5` 秒或 `100` 秒），就顯示「無效 **Invalid**」。

---

## 測試案例 (Testing Examples)

### 測試 1 (Example 1)
* **Input:** `timer = 60`
* **Output:** `"Red"`
* **解釋**：因為 60 介於 31 到 90 之間（符合 `30 < timer <= 90`），所以是紅燈。

### 測試 2 (Example 2)
* **Input:** `timer = 5`
* **Output:** `"Invalid"`
* **解釋**：數字 5 不符合任何一條規則（不是 0，不是 30，也不在 31~90 之間），所以回傳無效。

---

## 解題想法 (Step-by-Step)

我們可以使用程式語言中最常用的 `if-elif-else` 邏輯來處理：

1.  **先檢查綠燈**：如果 `timer` 等於 0，回傳 "Green"。
2.  **再檢查橘燈**：如果 `timer` 等於 30，回傳 "Orange"。
3.  **接著檢查紅燈**：如果 `timer` 大於 30 **且** 小於等於 90，回傳 "Red"。
4.  **最後處理其他情況**：如果上面的條件都不成立，通通回傳 "Invalid"。

---

## 新手筆記 (Key Takeaways)

1. **條件判斷的順序**
  在寫 `if-elif` 時，程式會從上往下檢查。一旦符合其中一個條件，後面的就不會再看了。這對於處理數值範圍非常重要。

2. **Python 的簡潔範圍寫法**
  在很多程式語言（如 Java 或 C++）中，你需要寫成 `timer > 30 && timer <= 90`。但在 Python 中，你可以直接寫成 `30 < timer <= 90`，這讀起來就像數學公式一樣自然。

3. **嚴格相等 == vs 賦值 =**
  新手常犯的錯誤是把判斷相等的` == `寫成一個` =`。記得在` if `判斷句中，我們要用兩個等號來問電腦：「這兩個數字相等嗎？」

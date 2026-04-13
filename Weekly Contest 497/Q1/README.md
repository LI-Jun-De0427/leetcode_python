# Q1. Find the Degree of Each Vertex

## 題目原文 (Problem Description)
> You are given a 2D integer array `matrix` of size `n x n` representing the adjacency matrix of an undirected graph with `n` vertices labeled from 0 to `n - 1`.
> - `matrix[i][j] = 1` indicates that there is an edge between vertices `i` and `j`.
> - `matrix[i][j] = 0` indicates that there is no edge between vertices `i` and `j`.
>
> The **degree** of a vertex is the number of edges connected to it.
>
> **Return an integer array `ans` of size `n` where `ans[i]` represents the degree of vertex `i`.**
---

## 題目在說什麼？

想像你在參加一個派對，每個人都有一個編號（從 0 開始）。這張矩陣（`matrix`）就像是一張「好友清單」。
* 如果矩陣的第 `i` 行、第 `j` 列寫著 `1`，代表編號 `i` 的人和編號 `j` 的人是好朋友。
* 題目要求的 **「度數 (Degree)」**，其實就是想問：**「每個人分別有多少個好朋友？」**

---

## 解題想法 (Step-by-Step)

這題的邏輯非常直觀，我們可以這樣思考：

1.  **觀察每一行**：在矩陣中，第 `i` 行紀錄了所有與頂點 `i` 相關的連線。
2.  **數數看有多少個 1**：如果這行裡面有三個 `1`，就代表有三個邊連到這個頂點。
3.  **計算總和**：因為矩陣中只有 `0` 和 `1`，我們只要把「每一行的數字全部加起來」，得到的結果就是該頂點的度數。
4.  **存入結果**：將每一行算出來的總和依序放入一個陣列中，最後回傳這個陣列。

---
## 測試案例 (Testing Examples)

### 測試 1 (Example 1)
<img src="https://github.com/user-attachments/assets/5658e338-021f-4157-b451-55a5fab94712" alt="Example 1 Graph" width="350px" />

* **Input:** `matrix = [[0,1,1],[1,0,1],[1,1,0]]`
* **Output:** `[2,2,2]`
* **解釋**：
  - 頂點 0 連接到 1 和 2，所以度數是 **2**。
  - 頂點 1 連接到 0 和 2，所以度數是 **2**。
  - 頂點 2 連接到 0 和 1，所以度數是 **2**。

---

### 測試 2 (Example 2)
<img src="https://github.com/user-attachments/assets/6efb91d5-ffe0-4546-9e19-b3884393206c" alt="Example 2 Graph" width="350px" />

* **Input:** `matrix = [[0,1,0],[1,0,0],[0,0,0]]`
* **Output:** `[1,1,0]`
* **解釋**：
  - 頂點 0 連接到 1，度數為 **1**。
  - 頂點 1 連接到 0，度數為 **1**。
  - 頂點 2 沒有連接任何頂點，度數為 **0**。

---

### 測試 3 (Example 3)
* **Input:** `matrix = [[0]]`
* **Output:** `[0]`
* **解釋**：只有一個頂點且沒有邊，所以度數為 **0**。

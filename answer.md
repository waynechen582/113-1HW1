# 第1次作業-作業-HW1
>
>學號：112111219
><br />
>姓名：陳恩偉
><br />
>作業撰寫時間：120 (mins，包含程式撰寫時間)
><br />
>最後撰寫文件日期：2023/10/07
>

本份文件包含以下主題：(至少需下面兩項，若是有多者可以自行新增)
- [x] 說明內容
- [x] 個人認為完成作業須具備觀念

1. 請解釋何謂git中下列指令代表什麼？並舉個例子，同時必須說明該例子的結果。其指令有add、commit、push、fetch、pull、branch、checkout與merge。

Ans:
1. add
功能： 將變更加入暫存區。
舉例： git add file.txt
說明： 將 file.txt 這個檔案的修改加入暫存區，準備提交。
結果： 檔案變更會被標記為準備提交，但還未真正提交到版本庫。
2. commit
功能： 將暫存區的變更提交到本地版本庫。
舉例： git commit -m "新增一個功能"
說明： 將暫存區的所有變更提交，並加上註解 "新增一個功能"。
結果： 變更會被永久保存到本地版本庫，並產生一個新的提交記錄。
3. push
功能： 將本地的提交推送到遠端版本庫。
舉例： git push origin main
說明： 將本地的 main 分支推送到遠端名為 origin 的版本庫。
結果： 遠端版本庫的內容會與本地保持一致。
4. fetch
功能： 從遠端版本庫下載最新的提交，但不合併到本地分支。
舉例： git fetch origin
說明： 從遠端名為 origin 的版本庫下載所有新的提交。
結果： 本地會新增遠端分支的引用，但本地分支的內容不會改變。
5. pull
功能： 從遠端版本庫下載最新的提交，並合併到本地分支。
舉例： git pull origin main
說明： 從遠端名為 origin 的版本庫下載最新的提交，並合併到本地的 main 分支。
結果： 本地分支的內容會與遠端保持一致。
6. branch
功能： 創建新的分支。
舉例： git branch feature
說明： 創建一個名為 feature 的新分支。
結果： 會產生一個新的分支，指向當前的提交。
7. checkout
功能： 切換到指定的分支。
舉例： git checkout feature
說明： 切換到名為 feature 的分支。
結果： 工作目錄會切換到指定分支的狀態。
8. merge
功能： 將一個分支合併到另一個分支。
舉例： git merge feature
說明： 將 feature 分支合併到當前分支。
結果： 如果沒有衝突，兩個分支的變更會被合併；如果有衝突，需要手動解決衝突後再提交。



2. 於專案下的檔案—**hw1.py**，撰寫註解，以說明該程式每列中之背後意義。

    該hw1.py題目如下：

    ```
    統計字母數。假設今天輸入一句子，句子中有許多單字，單字皆為英文字母小寫，
    請統計句子中字母出現的字數，輸出實需要照字母排序輸出，且若該字母為0則不輸出

    如輸入
    this is an apple
    輸出
    a: 2
    e: 1
    h: 1
    i: 2
    l: 1
    n: 1
    p: 2
    s: 2
    t: 1
    ```

Ans:
```py
from typing import List

def countLetters(sentence: str) -> List[int]:
    letterCount: List[int] = [0] * 26 # 初始化字母出現次數為0

    for char in sentence: #迴圈，逐一檢查每個字元
        if char.isalpha(): #如果是字母
            index = ord(char) - ord('a') # 計算字母在列表中的索引
            letterCount[index] += 1 # 相應字母出現次數加1

    return letterCount #回傳
pass #沒有就跳過

def printLetterCount(letterCount: List[int]) -> None:

    for i in range(26): #迴圈，逐一檢查所有字母索引
        if letterCount[i] > 0: #如果次數大於0
            print(f"{chr(i + ord('a'))}: {letterCount[i]}") # 輸出字母及次數
pass

inputSentence: str = "this is an apple" #定義字串並賦予值
letterCount: List[int] = countLetters(inputSentence) #計算每個字母出現的次數
printLetterCount(letterCount) #計算結果以子定格式輸出
```

3. 請新增檔案**hw1_2.py，**輸入一個正整數(N)，其中$1\le N \le 100000$，請將該正整數輸出進行反轉

    ```
    如輸入
    1081

    輸出
    1801

    如輸入
    1000

    輸出
    1
    ```

Ans:
逐一取出個位數。
將取出的數字移到新數字的最高位。
重複上述步驟直到原數字變為0。
取餘數 (%) 取得個位數，整數除法 (//) 移除個位數。
把數字拆解成一位一位的字，然後再以相反的順序組合起來。

4. **[課外題]**：請找尋資料，說明何謂**單元測試**，請新增檔案**hw1_3.py**，並利用溫度計攝氏轉華氏撰寫單元測試。

Ans:
單元測試是一種軟體測試方法，用來檢驗程式碼中的最小可測試單元是否正確地實現了預期的功能。


## 個人認為完成作業須具備觀念

開始寫說明，需要說明本次練習需學會那些觀念 (需寫成文章，需最少50字，並且文內不得有你、我、他三種文字)且必須提供完整與練習相關過程的notion筆記連結

Git 版本控制： 掌握 add、commit、push 等基本指令，並研究分支管理。

Python 程式設計： 加強 Python 語法熟練度，並嘗試優化程式碼。在數字反轉的練習中，比較能夠了不同演算法的效率。

單元測試： 了解到單元測試的重要性，並開始撰寫簡單的測試案例。
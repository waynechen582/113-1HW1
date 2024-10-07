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
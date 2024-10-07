def reverse_integer(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num

num = int(input("請輸入一個正整數:"))
result = reverse_integer(num)
print("反轉後:", result)
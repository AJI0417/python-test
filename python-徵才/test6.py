# 星號畫菱形

s = 5
x = 1
while x <= s:
    y = 1
    n = abs(x - s//2 - 1)
    print(" " * n, end="")
    print("*" * (s - 2 * n))
    x += 1

# 最大公因數

x = int(input("please input a number: "))
y = int(input("please input a number: "))
if x > y:
    c = x
else:
    c = y
for k in range(c, 2, -1):
    if x % k == 0 and y % k == 0:
        print("The highest common factor is : ", k)
        break

# 費式級數

def Fibonacc(n):
    if n < 2:
        return n
    else:
        return Fibonacc(n-1)+Fibonacc(n-2)


num = int(input("please input a number : "))

print("The Fibonacc number", num, "is : ")
for i in range(num):
    print(Fibonacc(i), end=" ")

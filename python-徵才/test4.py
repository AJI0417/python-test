# 身分證字號最後一碼(檢查碼)產生器
"""
代號	數值	縣市
 A	    10	  台北市
 B	    11	  台中市
 C	    12	  基隆市
 D	    13	  台南市
 E	    14	  高雄市
 F	    15	  台北縣
 G	    16	  宜蘭縣
 H	    17	  桃園縣
 I	    34	  嘉義市
 J	    18	  新竹縣
 K	    19	  苗栗縣
 L	    20	  台中縣
 M	    21 	  南投縣
 N	    22	  彰化縣
 O	    35	  新竹市
 P	    23	  雲林縣
 Q	    24	  嘉義縣
 R	    25	  台南縣
 S	    26	  高雄縣
 T	    27	  屏東縣
 U	    28	  花蓮縣
 V	    29	  台東縣
 W	    32	  金門縣
 X	    30	  澎湖縣
 Y	    31	  陽明山
 Z	    33	  連江縣
"""


idcheck = [10, 11, 12, 13, 14, 15, 16, 17, 34, 18, 19, 20,
           21, 22, 35, 23, 24, 25, 26, 27, 28, 29, 32, 30, 31, 33]
TotalVal = 0
idcode = ""
while (len(idcode) != 10):
    idcode = input("please input ID Number :")

print("ID Number : " + idcode)
CapVal = idcheck[ord(idcode[0])-65]
idcode11 = str(CapVal) + idcode[1:10]
TotalVal = int(idcode11[0])

for index, item in enumerate(idcode11[1:10]):
    m = int(item) * (9 - index)
    TotalVal = TotalVal + m

TotalVal = TotalVal + int(idcode11[10])
print("ID Number is ", end='')
if TotalVal % 10 == 0:
    print("real")
else:
    print("error")

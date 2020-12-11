import json
import numpy as np
import os

x = np.eye(3,4,-1)
print(x)

try:
    print(y)
except NameError:
    print("an exception occurred")
except:
    print("error")

try:
    print("hello")
except:
    print("error")
finally:
    print("don't have error")





prince = 55
it = 567
quantity = 3
txt = "{0}The {2}price is {1:.2f} dollars"
print(txt.format(prince,quantity,it))

#读取文件
# f = open("demofile.txt")
# print(f.read())
# print(f.readline())
# print(f.readline())
# for x in f:
#     print(x)
# f.close()


# #文件写入
# #打开文件，并将内容追加到文件中
# w = open("demofile.txt","a")
# w.write("Now the file has more content")
# w.close()
# #追加后，打开并读取该文件
# f = open("demofile.txt")
# print(f.read())
#
# #"a"是追加，"w"是覆盖内容
# f = open("demofile.txt","w")
# f.write("啥都没了")
# f.close()
# #打开并读取文件
# f = open("demofile.txt","r")
# print(f.read())

#删除文件
os.remove("demofile.txt")
#检查文件是否存在，然后删除
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("这个文件不存在")
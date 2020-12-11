from myModule import person1 as p
import platform
a = p["age"]
print(a)
x = platform.system()
print(x)
y = dir(platform)
print(y)
print(platform.uname_result)
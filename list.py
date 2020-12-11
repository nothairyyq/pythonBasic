thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist2 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thislist[2:5])
print(thislist2[2:5])
x = list(thislist2)
x[1]="1"
y = tuple(x)
print(y)
thistuple = tuple(("apple", "banana", "cherry")) # 请注意双括号
print(thistuple)
thistuple = ("apple", "banana", "cherry")
print(thistuple)

thisset = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}
thisset.add("1")
print(thisset)
for i in thisset:
    print(i)
thisset.update({"1","2","3"})
print(thisset)
print(len(thisset))
thisset.remove("3")
thisset.discard("1")
print(thisset)
w = thisset.pop()
print(w)
print(thisset)

thisset.clear()
print(thisset)

thisset1 = {"3","4","6",9}
thisset.update(thisset1)
print(thisset)
j = {thisset.update(thisset1)}
print(j)

thisdit = {"brand": "Porsche",
  "model": "911",
  "year": 1963
           }
for t in thisdit:
    for t1 in thisdit:
        print(t+":"+t1)

for t,t1 in thisdit.items():
    print(t,t1)

thisdit.popitem()
print(thisdit)

z = dict(thisdit)
print(thisdit)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist.pop(0)
print(thislist)


def my_fun(fname = "1" ):
    print(fname+"hello,java")
my_fun()

def eat(fruites):
    for x in fruites:
        print(x)
food = ("1","2","3")
food2 = "hello"
eat(food)
eat(food2)

def my_number(x):
    return x**x
print(my_number(80))

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Phoebe", "Jennifer", "Rory")

def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result
tri_recursion(6)

x = lambda a : a + 10
print(x(5))
x = lambda a,b,c: a*b**c
print(x(1,2,3))

def myfunc(n):
    return lambda a: a*n
print(myfunc(5))
myfifth = myfunc(5)
print(myfifth(5))



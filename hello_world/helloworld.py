print ("hello world")

if 5 > 2 :
	print(" 5 is bigger than 2")
else:
        	print("5 is less than 2")

x = 5
#comment blue
'''
weqwqewq
'''
y = "hhee"
yy = {}
aa = []
pp = None

print(type(x))
print(type(x))
print(type(yy))
print(type(aa))
print(type(pp))

x = ("apple", "banana", "cherry")
print(type(x))


a, b, c = 9, "Mycroft", [2, 3,4,5]
print(a)
print(b)
print(c)

e,f,g,h = c
print(e)
print(f)
print(g)
print(h)


def aFunc() -> None:
	x = "Python "
	y = "is "
	z = "awesome"
	print(x + y + z)


aFunc()
def aFunc1() -> None :
	x = 5
	y = "John"
	print(x, y)


aFunc1()

print(type(x))

x = "awesome"
print(type(x))
def myfunc():
  print("Python is " + x)

myfunc()

x = "awesome22"

def myfunc():
  x = "fantastic"
  print("Python is nside same func name" + x)

myfunc()

print("Python is " + x)


def myfunc():
  global x
  x = "fantasticFromLocalFunction-W-Global"

myfunc()

print("Python is " + x)


x = ["apple", "banana", "cherry"]
print(type(x))

x = [3,4,5]
print(type(x))



print ("=============\n\n\n\n Data TYPES \n")
x = "hello word"
print ("hello word ",  type(x))
x = 20
print ("20",  type(x), x)

x = 20.5
print ("20.5 ",  type(x), x)
x = 4j
print ("4j ",  type(x), x)
x = ["apple", "pie"]
print ("[\"apple\", \"pie\"] ",  type(x), x)
x = ("pine", "apple")
print ("(\"apple\", \"pie\") ",  type(x), x)
x = range (34, 40)
print ("range(3)",  type(x), x)
x = {"name" : "Eurus", "age" : 32}
print ("\"name\" : \"Eurus\", \"age\" : 32",  type(x), x)
x = frozenset({"apple", "pie", "is", "hot"})
print ("wth is fronzenset used for?",  type(x), x)
x = True
print ("True",  type(x), x)
x = b"Hello"
print ("bHello?",  type(x), x)
x = bytearray(5)
print ("bytearray(5)",  type(x), x)
x = memoryview(bytes(5))
print ("memoryview((bytes(5))",  type(x), x)
x = None
print ("None",  type(x), x)





























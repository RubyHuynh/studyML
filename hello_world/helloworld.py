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
aa = {}
pp = None

print(type(x))
print(type(yy))
print(type(aa))
print(type(pp))


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

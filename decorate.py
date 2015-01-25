def f1():
	a=1000
	def f2():
		print a
	return f2
print 'f1:', f1()()
##########
def f2():
	a=1000
	def f2():
		print a
	return f2()
print 'f2:', f2()
##########
def f3(x):
	def f2(y):
		print x**y
	return f2
f=f3(10)
print 'f3:', f(2)
##########
def f4(x):
	f=lambda x, y: x**y
	return f
f=f3(10)
print 'f4:', f(2)
##########

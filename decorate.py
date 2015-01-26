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
def f5():
	global num
	num = 0
	def f(name):
		global num
		print num, name
		num += 1
	return f
f=f5()
print 'f5:', f('wang')
print 'f5:', f('teng')
print 'f5:', f('fei')
##########
class C1(object):
	"""docstring for C1"""
	def __init__(self, arg):
		super(C1, self).__init__()
		self.arg = arg
	def f(self, name):
		print self.arg, name
		self.arg += 1
c=C1(10)
print 'C1:', c.f('wang')
##########

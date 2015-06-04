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
<<<<<<< HEAD

# num = 1
# def add_num():
# 	# print num
# 	num = num + 1
# 	print num
# add_num()

def f6(L):
	if not L:
		return 0
	else:
		print L[0], L[1:]
		return L[0] + f6(L[1:])
print 'f6: ', f6(range(5))

def f7(l):
	res = 0
	for x in l:
		if not isinstance(x, (list, tuple)):
			res += x
		else:
			res += f7(l)
	return res
print 'f7: ', f7(range(5))

def f8(x):
	a, b = 0, 1
	while b<x:
		print a, b
		a, b = b, a+b
print 'f8: ', f8(10)


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))

student_tuples = [  
    ('john', 'A', 15),  
    ('jane', 'B', 12),  
    ('dave', 'B', 10),  
]  
student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
print 'student_objects: ', dir(student_objects[0])
print 'student_objects: ', dir(student_objects[0].__module__)
sorted(student_objects, key=lambda student: student.age)   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
from operator import itemgetter, attrgetter, methodcaller
print sorted(student_objects, key=attrgetter('age', 'name'))
print sorted(student_tuples, key=itemgetter(2, 1), reverse=False)

messages = ['critical!!!', 'hurry!', 'standby', 'immediate!!']
print sorted(messages, key=methodcaller('count', '!'))

l = [range(4), range(4)]
print l
for w, x, y, z in l:
	print w, x, y, z

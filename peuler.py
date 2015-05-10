# project Euler
def p1():
	num = 0
	for i in range(1,1000):
		if i%3 == 0:
			num += i
		if i%5 == 0:
			num += i
		if i%15 == 0:
			num = num - i
	return num
				
# print(p1())
# another
# result = 0
# for i in range(1,1000):
# 	if i%3 == 0 or i%5 == 0:
# 		result += i
# print(str(result))

def p2(n = 4000000):
	result = 0
	a,b = 1,2
	while b < n:
		if b % 2 == 0:
			result += b
		a,b = b,a+b
	# print(result)
# p2(4000000) 

# time checker
# if __name__ == '__main__':
# 	from timeit import Timer
# 	statement = "%s()" % 'p2'
# 	t = Timer(statement, "from __main__ import p2")
# 	print("%.9f" % min(t.repeat(3, 50000)))
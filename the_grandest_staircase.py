from __future__ import division
from itertools import combinations, repeat


def length_long(n):
	return n * (n+1) / 2

def answer(n):
	print('n', n)
	summ = 0
	for i in range(2, int(round(n/2.0))):
		print ('i', i)
		x = combinations(list(range(1,n)), i)
		length  = len(filter(lambda y: sum(y) == n, x))

		print('length', length)

		
		x = combinations(list(range(1,n)), i)
		print ('test even', len(list(x))/(n-2)/3)
		print len(list(x))
		if length > 0:
			summ += length
		else:
			break
	return summ
		
print answer(9)
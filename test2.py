def generous_approach(lambs, n):
	henchmen_num = n + 1
	print('n = ', n, '2 ** n = ', 2 ** n, 'lambs = ', lambs)
	if 2 ** n <= lambs:
		return generous_approach(lambs - 2 ** n, n + 1)
	else:
		prev_val = (2 ** n) / 2
		prev_prev_val = prev_val / 2
		print(prev_prev_val + prev_val)
		if(prev_prev_val + prev_val <= lambs):
			return n + 1
		return n


def greedy_approach(lambs, n, prev_val, prev_prev_val):
	if n == 0:
		return greedy_approach(lambs - 1, n + 1, 1, 0)
	elif n == 1:
		return greedy_approach(lambs - 1, n + 1, 1, 1)
	elif prev_prev_val + prev_val <= lambs:
		return greedy_approach(lambs - prev_prev_val - prev_val, n + 1, prev_prev_val + prev_val, prev_val)
	else:
		return n

gen = greedy_approach(21, 0, 0, 0)
print(gen)
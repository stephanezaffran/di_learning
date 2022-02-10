from functools import reduce


picture = [
	[0, 0, 0, 1, 0, 0, 0],
	[0, 0, 1, 1, 1, 0, 0],
	[0, 1, 1, 1, 1, 1, 0],
	[1, 1, 1, 1, 1, 1, 1],
	[0, 0, 0, 1, 0, 0, 0],
	[0, 0, 0, 1, 0, 0, 0]
]

for i in picture:
	txt = ""
	for j in i:
		if j == 0:
			txt += " "
		else:
			txt += "*"
	print(txt, end='')
	print('')


# sort function with reduce

def swap(a, b):
	print(f"a:{a} and b:{b}")
	if a > b:
		d = a
		a = b
		b = d
	print(f"a:{a} and b:{b}")
	return b


my_list = [6, 5, 4, 3, 2, 1]
reduced_list = reduce(swap, my_list)


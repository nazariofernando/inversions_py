from merge_sort import divide

f = open('array.txt', 'r')
array = []
for line in f:
	array.append(int(line))

print divide(array)[1]

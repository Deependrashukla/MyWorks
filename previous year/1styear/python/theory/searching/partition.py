part = 0
swap_p = 0
comparision = 0
p = 0
def partition(b, h, k):
	global swap_p, comparision, p
	i = h 
	pivot = b[h]
	j = k + 1
	p += 1
	while i < j - 1 :
		comparision += 1
		if pivot > b[i + 1]:
			b[i] , b[i + 1] = b[i + 1], b[i]
			swap_p += 1
			# h += 1
			i += 1

		else:
			b[i + 1], b[j - 1] = b[j - 1], b[i + 1]
			swap_p += 1
			j -= 1
		# i += 1

	return i

# print(partition([5,1,8,1,2,3,8,4,9],0,6))

def quick_sort(b,h,k):
	global part
	if h == k + 1:
		return

	j = partition(b, h, k)
	part += 1
	quick_sort(b, h, j - 1)
	quick_sort(b, j + 1, k)
	
# lst = [5,4,3,2,1,5,7,9,7,7,8,5,2,1,5,11,54,5,6,2,0,2,8,3,8]
# lst = [0, 2, 6, 41, 9, 8, 9, 7, 6, 3, 4, 2, 1, .5]
# lst =[3,2,65,7,698,4,76,86,2,6,5,87,4,90,76,36,0,56,3,2,66,76,3,87,31,84,96,34,65,2,5,98,5,5,43,2,2,34,4,5,5,5,66,6,5,4,22,344,5,5,6,6,6]
lst = [5,2,4,3,1,7,8,9,3]
# (quick_sort(lst, 0, len(lst) - 1))
# print(lst)
# print(part)
print(swap_p, comparision)
print(p)

# 240
# 240
# 311
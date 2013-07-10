import array
import random

# Quicksort

def swap(data, posA, posB):
	tmp = data[posA]
	data[posA] = data[posB]
	data[posB] = tmp


# Description: 		In-place quicksort using recursion
# Improvements:		Better pivot, less recursion
# Limitation:		Bad pivot can lead to O(n**2)
# Time complexity:	O(n log n) (assuming reasonable distribution)
# Space complexity:	O(log n) (for call stack)
def quicksort_risky(data = array.array('f', [random.random() for i in range(10000)])):
	length = len(data)
	if length < 2:
		return data
	quicksort_r(data, 0, length-1)
	return data


def quicksort_r(data, start, end):
	if start >= end:
		return
	pivotPos = (start + end) >> 1
	pivot = data[pivotPos]	
	i = start
	j = end
	while i <= j:
		while i <= end and data[i] < pivot:
			i += 1
		while j >= 0 and data[j] > pivot:
			j -= 1		
		if i <= j:
			swap(data, i, j)
			i += 1
			j -= 1	
	if i < end:
		quicksort_r(data, i, end)
	if start < j:
		quicksort_r(data, start, j)
			
			
			
			
# Description: 		In-place quicksort using recursion
# Improvements:		Tim-sort
# Limitation:		None
# Time complexity:	O(n log n) 
# Space complexity:	O(log n) (for call stack)
def quicksort(data = array.array('f', [random.random() for i in range(10000)])):
	length = len(data)
	if length < 2:
		return data
	quicksort_r2(data, 0, length-1)
	return data			
			
			
# Median of three, swapping not strictly necessary
def good_pivot(data, start, end):
	mid = (start + end) >> 1
	if data[mid] <= data[start]:
		if data[mid] >= data[end]:
			return mid
		if data[start] <= data[end]:
			swap(data, start, mid)
			return start
		swap(data, mid, end)
		return end
	else:
		if data[mid] <= data[end]:
			return mid
		if data[start] >= data[end]:
			swap(data, start, mid)
			return start
		swap(data, mid, end)
		return end		
	
		
def quicksort_r2(data, start, end):
	if start >= end:
		return
	pivotPos = good_pivot(data, start, end)
	pivot = data[pivotPos]	
	i = start
	j = end
	while i <= j:
		while i <= end and data[i] < pivot:
			i += 1
		while j >= 0 and data[j] > pivot:
			j -= 1		
		if i <= j:
			swap(data, i, j)
			i += 1
			j -= 1	
	if i < end:
		quicksort_r2(data, i, end)
	if start < j:
		quicksort_r2(data, start, j)			
			
			
			
			
def test():
	res = quicksort()
	for i in range(1,10000):
		if res[i-1] > res[i]:
			print("Error")
			
			
			
			
			
import math, sys, time
import numpy as np
from matplotlib import pyplot as plt

# https://www.geeksforgeeks.org/insertion-sort/
def insertionSort(arr): 
	for i in range(1, len(arr)): 
		key = arr[i] 
		j = i-1
		while j >= 0 and key < arr[j] : 
				arr[j + 1] = arr[j] 
				j -= 1
		arr[j + 1] = key

# https://www.geeksforgeeks.org/merge-sort/
def mergeSort(arr):
	if len(arr) >1:
		mid = len(arr)//2
		L = arr[:mid]
		R = arr[mid:]
		mergeSort(L)
		mergeSort(R)
		i = j = k = 0		 
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i+= 1
			else:
				arr[k] = R[j]
				j+= 1
			k+= 1
		while i < len(L):
			arr[k] = L[i]
			i+= 1
			k+= 1
		while j < len(R):
			arr[k] = R[j]
			j+= 1
			k+= 1

is_time = []
ms_time = []
n = range(1, 75, 1)

for i in n:
	is_temp = []
	ms_temp = []
	ts_temp = []
	for j in range(10):
		arr = np.random.rand(i)

		start = time.monotonic()
		insertionSort(np.copy(arr))
		stop = time.monotonic()
		is_temp.append(stop - start)

		start = time.monotonic()
		mergeSort(np.copy(arr))
		stop = time.monotonic()
		ms_temp.append(stop - start)

	is_time.append(np.mean(is_temp))
	ms_time.append(np.mean(ms_temp))

is_time = 1000 * np.array(is_time)
ms_time = 1000 * np.array(ms_time)

plt.plot(n, is_time, label="Insertion Sort")
plt.plot(n, ms_time, label="Merge Sort")
plt.legend()
plt.xlabel("Size of array (N)")
plt.ylabel("Run-Time of Algorithm (milli-second)")
plt.show()
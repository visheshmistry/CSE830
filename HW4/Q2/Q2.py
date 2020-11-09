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

def timSort(arr, hybrid_constant):
	length = len(arr)
	if length >1:
		if (length < hybrid_constant):
			insertionSort(arr)
		else:
			mid = len(arr)//2
			L = arr[:mid]
			R = arr[mid:]
			timSort(L, hybrid_constant)
			timSort(R, hybrid_constant)
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

################################### Part A ###############################

n = range(1, 50, 1)
k = range(5, 50, 5)
ts_time = np.zeros((len(k), len(n)))

for i in range(len(n)):
	for j in range(len(k)):
		for m in range(10):
			arr = np.random.rand(n[i])
			start = time.monotonic()
			timSort(np.copy(arr), k[j])
			stop = time.monotonic()
			ts_time[j,i] = ts_time[j,i] + (stop - start)
		ts_time[j,i] = ts_time[j,i] / 10

ts_time = 1000 * ts_time

for j in range(len(k)):
	plt.plot(n, ts_time[j, :], label="k=" + str(k[j]))

plt.legend()
plt.xlabel("Size of array (N)")
plt.ylabel("Run-Time of Tim-Sort (milli-second)")
# plt.show()
plt.savefig("Q2_A.png", dpi=500, bbox_inches="tight")

################################### Part B ###############################

is_time = []
ms_time = []
ts_time = []
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

		start = time.monotonic()
		timSort(np.copy(arr), 17.5)
		stop = time.monotonic()
		ts_temp.append(stop - start)

	is_time.append(np.mean(is_temp))
	ms_time.append(np.mean(ms_temp))
	ts_time.append(np.mean(ts_temp))

is_time = 1000 * np.array(is_time)
ms_time = 1000 * np.array(ms_time)
ts_time = 1000 * np.array(ts_time)

plt.plot(n, is_time, label="Insertion Sort")
plt.plot(n, ms_time, label="Merge Sort")
plt.plot(n, ts_time, label="Tim Sort (k=17.5)")
plt.legend()
plt.xlabel("Size of array (N)")
plt.ylabel("Run-Time of Algorithm (milli-second)")
# plt.show()
plt.savefig("Q2_B.png", dpi=500, bbox_inches="tight")







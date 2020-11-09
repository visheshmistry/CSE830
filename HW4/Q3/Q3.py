import time
from matplotlib import pyplot as plt
from BTrees.OOBTree import OOBTree

# Dictionary based on hash table
# https://mail.python.org/pipermail/python-list/2000-March/048085.html
dict_hashtable = {}

# Dictionary based on binary tree
# https://pythonhosted.org/BTrees/
dict_binarytree = OOBTree()

dict_ht_time = []
dict_bt_time = []
dict_insertions = []

num_insertions = 1
to_break = False
while (1):
	dict_insertions.append(num_insertions)
	dict_hashtable = {}
	dict_binarytree = OOBTree()

	start = time.monotonic()
	for i in range(num_insertions):
		dict_hashtable[i] = str(i)
	stop = time.monotonic()
	dict_ht_time.append(stop - start)
	if (dict_ht_time[-1] > 3):
		to_break = True

	start = time.monotonic()
	for i in range(num_insertions):
		dict_binarytree.update({i: str(i)})
	stop = time.monotonic()
	dict_bt_time.append(stop - start)
	if (to_break or dict_bt_time[-1] > 3):
		break

	num_insertions = num_insertions * 10

plt.plot(dict_insertions, dict_ht_time, label="Dictionary using Hash Table")
plt.plot(dict_insertions, dict_bt_time, label="Dictionary using Binary Tree")
plt.legend()
plt.xlabel("Number of Insertions (N)")
plt.xscale("log")
plt.ylabel("Run-Time of Algorithm (seconds)")
# plt.show()
plt.savefig("Q3.png", dpi=500, bbox_inches="tight")
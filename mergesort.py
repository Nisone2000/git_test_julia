def assignment(new_list, i, old_list, j):
	'''  change entry of new list at position i to value of old_list at position> '''	
     new_list[i] = old_list[j]


def merge_sort(list_to_sort_by_merge):
	'''
	Sortitert rekursiv nach dem Mergesort Algorithmus 
	'''

    if ( len(list_to_sort_by_merge) > 1 ):
	#compute middle position with
        mid = len(list_to_sort_by_merge) // 2	
        left = list_to_sort_by_merge[:mid]
        right = list_to_sort_by_merge[mid:]

       	merge_sort(left)
        merge_sort(right)

        l = 0
        r = 0
        i = 0

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                assignment(new_list=list_to_sort_by_merge, i=i, old_list=left, j=l)
                l += 1
            else:
                assignment(new_list=list_to_sort_by_merge, i=i, old_list=right, j=r)
                r += 1
            i += 1

        while l < len(left):
            list_to_sort_by_merge[i] = left[l]
            l += 1
            i += 1

        while r < len(right):
            list_to_sort_by_merge[i] = right[r]
            r += 1
            i += 1


import matplotlib.pyplot as plt

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(my_list))
plt.bar(x, my_list)
plt.xlabel('Position in der Liste')
plt.ylabel('Eintrag in der Liste')
plt.title('Liste ohne Änderung')
plt.show()
<<<<<<< HEAD
merge_sort(my_list)
plt.bar(x, my_list)
plt.xlabel('Position in der Liste')
plt.ylabel('Eintrag in der Liste')
plt.title('Liste nach Sortierung')
>>>>>>> main
plt.show()

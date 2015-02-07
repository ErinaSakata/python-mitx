"""
Download the text file here. (Right click and save link as)
This file contains all of the 100,000 integers between 1 and 100,000 
(inclusive) in some order, with no integer repeated.

Your task is to compute the number of inversions in the file given,
 where the ith row of the file indicates the ith entry of an array.
Because of the large size of this array, you should implement the fast 
divide-and-conquer algorithm covered in the video lectures. The numeric 
answer for 
the given input file should be typed in the space below.
So if your answer is 1198233847, then just type 1198233847 in the space 
provided without any space / commas / any other punctuation marks. You can 
make up to 5 attempts, and we'll use the best one for grading.
(We do not require you to submit your code, so feel free to use any programming 
	language you want --- just type the final numeric answer in the following 
	space.)

[TIP: before submitting, first test the correctness of your program on some 
small test files or your own devising. Then post your best test cases to the 
discussion forums to help your fellow students!]
"""

lines = [int(line.strip()) for line in open('IntegerArray.txt')]

print lines[0:10]
print "length : ", len(lines)
sizeOfArray = len(lines)
count = 0

def merge_sort(li):
	"""
	Time Complexity: O(nlogn)
	Algorithmic Paradigm: Divide and Conquer

	"""

   	if len(li) < 2: 
   		return li 
   	m = len(li) / 2 
   	return merge(merge_sort(li[:m]), merge_sort(li[m:])) 

def merge(l, r):
    global count
    result = [] 
    i = j = 0 
    while i < len(l) and j < len(r): 
        if l[i] < r[j]: 
            result.append(l[i])
            i += 1 
        else: 
            result.append(r[j])
            count = count + (len(l) - i)
            j += 1
    result.extend(l[i:]) 
    result.extend(r[j:]) 
    return result

# unsorted = [10,2,3,22,33,7,4,1,2]
merge_sort(lines)
print count

# print count
# clarifying questions
# what if there is a tie for most frequent value at the k boundary?
#     - we will return a correct answer, but no guarantees about which one
# what if K is invalid?
#     - we will assume that the code will end up raising an error of some kind
# what if there is k negative values?
#     - they should just work , like a positive number

# logical steps
# 1- Build a frequency map of the list elements and their count
# 2- get the unique elements of the list into a new list, from map keys
# 3- sort the unique values based on their counts
# 4- return the first k values

def make_counts(arr):
    counts = {}
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
        # count = counts.get(num, 0)
        # counts[num] = count + 1
    return counts

def most_frequent_k_elements(arr, k):
    counts = make_counts(arr) # O(n), O(n)
    unique_nums = list(counts.keys()) # O(n), O(n)
    unique_nums.sort(key=lambda num: counts[num], reverse=True) #O(n log n), O(n)
    # unique_nums.sort(key=counts.get)
    return unique_nums[:k] # O(n), O(n)

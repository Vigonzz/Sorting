# Violet Gonzalez
# Week 3 assignment: Sorting

# Task 1: Given an array of strings Strings, group the words that are anagrams to each other.  
import time 
import random
import string

def _merger(sorted1, sorted2):
    """ From two inputs that are already sorted return a singular sorted list by checking the indices and then 
    appending """

    result = []

    # Two index variables for two lists, both starting at 0
    index_1 = 0
    index_2 = 0 

    # Got influence in terms of structure and understanding from the following article:
    # GeeksforGeeks. (2026c, August 17). Merge sort in python. https://www.geeksforgeeks.org/python/python-program-for-merge-sort/ 
    # check indices within a list and append it to the new list
    while index_1 < len(sorted1) and index_2 < len(sorted2):
        if sorted1[index_1] <= sorted2[index_2]:
            result.append(sorted1[index_1])
            index_1 += 1
        else:
            result.append(sorted2[index_2])
            index_2 += 1
    
    # Add any leftover characters into the list
    while index_1 < len(sorted1):
        result.append(sorted1[index_1])
        index_1 += 1
    
    while index_2 < len(sorted2):
        result.append(sorted2[index_2])
        index_2 += 1

    return result

def recursive_mergesort(existing_list):
    """ Helps sort out a given list of characters and returns a nre lost pf charcters in ASCII order """
    if len(existing_list) <= 1:
        return existing_list
    
    mid = len(existing_list) // 2

    # Slice the list to create two halves
    left = existing_list[0:mid]
    right = existing_list[mid:]

    # Sorts the halves into themselves 
    sorted_left = recursive_mergesort(left)
    sorted_right = recursive_mergesort(right)

    # Combine it all together
    new_list = _merger(sorted_left, sorted_right)

    return new_list

def quicksort(char_list):
    """ Same idea as recursive merge but instead of just dividing and conqour, it
     also pivots the middle index, by walking through every character and drop it into 
      one of the new lists by comparing the pivot """
    
    if len(char_list) <= 1:
        return char_list
    
    mid = len(char_list) // 2
    pivot = char_list[mid]

    # the partition 
    less = []
    equal = []
    greater = []

    for char in char_list:
        if char < pivot:
            less.append(char)
        elif char == pivot:
            equal.append(char)
        else:
            greater.append(char)
    
    # Recurse
    sorted_less = quicksort(less)
    sorted_greater = quicksort(greater)

    # Combine the list
    combine = sorted_less + equal + sorted_greater
    return combine

def sortString(word, algorithm = "merge"):
    """ Acts as a bridge between the words and sorting algorithms to turn the word into an
     anagram key,  """
    chars = list(word)
    if algorithm  == "merge":
        sorted_chars = recursive_mergesort(chars)
    elif algorithm == "quicksort":
        sorted_chars = quicksort(chars)
    else:
        raise ValueError("Algorithm chosen not recognized. Choose between quicksort or merge")
    return "".join(sorted_chars)

def groupAnagram(strings, algorithm="merge"):
    """ Group words that are anagrams together """
    groups = {}

    for word in strings:
        key = sortString(word, algorithm)

        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    
    # Return the groups
    return list(groups.values())

# I needed more understanding of choices and how it works:
# GeeksforGeeks. (2025b, July 12). Python - random.choices() method. https://www.geeksforgeeks.org/python/random-choices-method-in-python/ 
def time_sort(word, algorithm, runs = 5):
    ''' Runs sortstring repeatedly and times it. Returns the average of seconds per run '''
    # Start of the timer
    start = time.perf_counter()

    for run in range(runs):
        _ = sortString(word, algorithm)

    # end of the timer
    end = time.perf_counter()

    return (end - start) / runs

# Create a string of different sizes
sizes = [1_000, 10_000, 100_000]

#  Times both mergesort and quicksort, and returns the average. Creates a fair time test between both algorithms
for size in sizes:
    test_word = "".join(random.choices(string.ascii_lowercase, k=size))
    merge_time = time_sort(test_word, "merge")
    quick_time = time_sort(test_word, "quicksort")
    # Needed reference for decimal format:
    # Python string formatting. W3Schools. (n.d.). https://www.w3schools.com/python/python_string_formatting.asp 
    print(f"{size}, {merge_time:.6f}, {quick_time:.6f}")

# Testing helper function
print("\n-------Normal Merge------")
normal_merge = _merger(['a', 'g', 'o'], ['m','n'])
print(f"{normal_merge}\n")

print("-------Ties test------")
ties = _merger(['a', 'a'], ['a'])
print(f"{ties}\n")

print("-------Empty First List------")
empty = _merger([], ['b', 'c'])
print(f"{empty}\n")

# Test comparisons

# edge case test as per assignment details
print("\n-----Edge Case Tests for groupAnagram-----\n")

print("-----Empty List-----")
print("-----merge-----")
print(groupAnagram([], "merge"))
print("-----quicksort-----")
print(groupAnagram([], "quicksort"))


print("\n-----Single Word-----")
print("-----merge-----")
print(groupAnagram(["mango"], "merge"))
print("-----quicksort-----")
print(groupAnagram(["mango"], "quicksort"))

print("-----Empty String-----")
print("-----merge-----")
print(groupAnagram([""], "merge"))
print("-----quicksort-----")
print(groupAnagram([""], "quicksort"))

print("-----No Anagrams-----")
print("-----merge-----")
print(groupAnagram(["cat", "dog", "bird"], "merge"))
print("-----quicksort-----")
print(groupAnagram(["cat", "dog", "bird"], "quicksort"))

print("\n-----All Anagrams-----")
print("-----merge-----")
print(groupAnagram(["listen", "silent", "enlist"], "merge"))
print("-----quicksort-----")
print(groupAnagram(["listen", "silent", "enlist"], "quicksort"))

print("\n-----Duplicate Words-----")
print("-----merge-----")
print(groupAnagram(["rat", "rat", "tar"], "merge"))
print("-----quicksort-----")
print(groupAnagram(["rat", "rat", "tar"], "quicksort"))

print("\n-----Repeated letters-----")
print("-----merge-----")
print(groupAnagram(["aab", "aba", "abb"], "merge"))
print("-----quicksort-----")
print(groupAnagram(["aab", "aba", "abb"], "quicksort"))

print("\n-----Mixed Cases-----")
print("-----merge-----")
print(groupAnagram(["Rat", "tar"], "merge"))
print("-----quicksort-----")
print(groupAnagram(["Rat", "tar"], "quicksort"))

print("\n-----TEST 1-----")
test = recursive_mergesort(list("mango"))
print(test)

print("\n-----TEST 2-----")
print(recursive_mergesort(list("bucket")))

print("\n-----TEST 3-----")
print(recursive_mergesort(list([])))

print("\n-----TEST 4-----")
print(recursive_mergesort(list(['z'])))

print("\n-----TEST 5-----")
print(recursive_mergesort(list(list("aabba"))))

# Testing that our strings are sorted

print("\n\n----- Testing Sorting-----")

print("\n-----TEST 1-----")
print(sortString("mango"))

print("\n-----TEST 2-----")
print(sortString("ogman"))

print("\n-----TEST 3-----")
print(sortString("tango"))

print("\n-----TEST 4-----")
print(sortString("ogtan"))

print("\n-----TEST 5-----")
print(sortString(""))

# Testing grouping the anagrams
print("\n\n-----Testing Grouping-----")

print("\n-----Assignment Example-----")
print(groupAnagram(["bucket", "rat", "mango", "tango", "ogtan", "tar"]))

# Testing quicksort
print("\n\n-----Testing quicksort-----")
print("\n-----TEST 1-----")
test = quicksort(list("mango"))
print(test)

print("\n-----TEST 2-----")
print(quicksort(list("bucket")))

print("\n-----TEST 3-----")
print(quicksort(list([])))

print("\n-----TEST 4-----")
print(quicksort(list(['z'])))

print("\n-----TEST 5-----")
print(quicksort(list(list("aabba"))))

# Testing sort string with quicksort
print("\n\n----- Testing Sorting(quicksort)-----")

print("\n-----TEST 1-----")
print(sortString("mango", "quicksort"))

print("\n-----TEST 2-----")
print(sortString("ogman", "quicksort"))

print("\n-----TEST 3-----")
print(sortString("tango","quicksort"))

print("\n-----TEST 4-----")
print(sortString("ogtan","quicksort"))

print("\n-----TEST 5-----")
print(sortString("","quicksort"))


print("\n\n-----Testing Grouping(quicksort)-----")

print("\n-----Assignment Example-----")
print(groupAnagram(["bucket", "rat", "mango", "tango", "ogtan", "tar"], "quicksort"))
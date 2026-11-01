# Violet Gonzalez
# Week 3 assignment: Sorting

# Task 1: Given an array of strings Strings, group the words that are anagrams to each other.  

def _merger(sorted1, sorted2):
    """ From two inputs that are already sorted return a singular sorted list by checking the indices and then 
    appending """

    result = []

    # Two index variables for two lists, both starting at 0
    index_1 = 0
    index_2 = 0 

    # Got influence in terms of structure and understanding from the following article:
    # 
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
    """ - """
    if len(existing_list) <= 1:
        return existing_list
    
    mid = len(existing_list) // 2

    # Slice the list to create two halves
    left = existing_list[0:mid]
    right = existing_list[mid:]

    sorted_left = recursive_mergesort(left)
    sorted_right = recursive_mergesort(right)

    new_list = _merger(sorted_left, sorted_right)

    return new_list

def sortString(string, algorithm = "merge"):
    """ """
    chars = list(string)
    if algorithm  == "merge":
        sorted_chars = recursive_mergesort(chars)
    elif algorithm == "quicksort":
        sorted_chars = quicksort(chars)
    else:
        raise ValueError("Algorithm chosen not recgonized. Choose between quicksort or merge")
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


print("Testing our Recrusive Mergesort:/n")
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





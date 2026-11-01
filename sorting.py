# Violet Gonzalez
# Week 3 assignment: Sorting

# Task 1: Given an array of strings Strings, group the words that are anagrams to each other.  

def _merger(sorted1, sorted2):
    result = []

    # Two index variables for two lists, both starting at 0
    index_1 = 0
    index_2 = 0 

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
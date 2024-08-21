'''
a function that takes two lists of numbers and returns the result of merging 
the lists. The elements of the first list should become the elements at the 
even indexes of the returned list, while the elements of the second list should
become the elements at the odd indexes. For instance:
merge([1, 2, 3], [4, 5, 6]) # => [1, 4, 2, 5, 3, 6]
'''
'''
All of the elements in the second list can be appended into the 1st list
at index +1 of their original location in the second list
'''
'''
*2 + 1
'''
def merge(list1, list2):
    import copy
    list3 = copy.copy(list1)
    counter = 0
    while counter < len(list2):
        list3.insert(counter * 2 + 1, list2[counter])
        counter += 1
    return list3

print(merge([1, 2, 3], [4, 5, 6]))

'''
Problem:
a function that determines the index of the 3rd occurrence of a given character
in a string. For instance, if the given character is 'x' and the string is 
'axbxcdxex', the function should return 6 (the index of the 3rd 'x'). 
If the given character does not occur at least 3 times, return None.
'''
'''
Pseudocode:
use the .count() method
    string.count(substring) should return the number of occurences
    if 3 occurences, use .rfind
    if not, use .find replace the item at the return index, repeat 3 times
    
if string.count(substring) < 3:
    return None
elif string.count(substring) == 3:
    return string.rfind(substring)
else:
    do it manually
    initialize hits at 0
    iterate through each item in string and hits += 1 when substring found
    when hits = 3, return the index
    
'''

def third_occurence(string, substring):
    if string.count(substring) == -1:
        return None
    elif string.count(substring) == 3:
        return string.rfind(substring)
    else:
        hits = 0
        counter = 0
        while hits < 3:
            if string[counter] == substring:
                hits += 1
                counter += 1
        return counter
        
my_string = 'axbxcdxex'
print(third_occurence(my_string, 'x'))
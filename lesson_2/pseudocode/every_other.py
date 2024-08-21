'''
Problem:
a function that takes a list of integers, and returns a new list with every 
other element from the original list, starting with the first element. 
For instance: every_other([1,4,7,2,5]) # => [1,7,5]
'''

'''
Pseudocode:
def function_name(list_of_integers)
    iterate thru list_of_integers and only record the even values
    or iterate thru the list and delete the odd values
    or interate thru the list += 2 and keep those values
        initialize counter
        += 2
        record list[counter]
        keep this running for as long as counter <= length of list
'''
'''
Formal Pseudocode:
def every_other(list):
    initialize counter at 0
    start a new list
    while counter <= length of list:
        append the list[counter] to the new list
        counter += 2
    return new list
'''

def every_other(list):
    counter = 0
    output = []
    while counter <= len(list):
        output.append(list[counter])
        counter += 2
    return output

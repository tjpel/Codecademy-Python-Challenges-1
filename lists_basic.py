#problems found on Codecademy
#solutions created by Thomas Pelowitz, tpelowitz.com or github.com/tjpel

#-------------Question 1-------------------
print("Question 1")
#Create a function called append_size that has one parameter named lst.
#The function should append the size of lst (inclusive) to the end of lst. The function should then return this new list.
#For example, if lst was [23, 42, 108], the function should return [23, 42, 108, 3] because the size of lst was originally 3.

def append_size(lst):
    return lst + [len(lst)]

#test
print(append_size([23, 42, 108]))

#-------------Question 2-------------------
print("Question 2")
#Write a function named append_sum that has one parameter — a list named named lst.
#The function should add the last two elements of lst together and append the result to lst. It should do this process three times and then return lst.
#For example, if lst started as [1, 1, 2], the final result should be [1, 1, 2, 3, 5, 8].

def append_sum(lst):
    for i in range(3): lst.append(lst[-1]+lst[2])
    return lst

#test
print(append_sum([1, 1, 2]))

#-------------Question 3-------------------
print("Question 3")
#Write a function named larger_list that has two parameters named lst1 and lst2.
#The function should return the last element of the list that contains more elements. If both lists are the same size, then return the last element of lst1.
def larger_list(lst1, lst2):
    if len(lst1) >= len(lst2): return lst1[-1]
    return lst2[-1]

#test
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

#-------------Question 4-------------------
print("Question 4")
#Create a function named more_than_n that has three parameters named lst, item, and n.
#The function should return True if item appears in the list more than n times. The function should return False otherwise.

def more_than_n(lst, item, n):
    if lst.count(item)>n: return True
    return False

#test
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

#-------------Question 5-------------------
print("Question 5")
#Write a function named combine_sort that has two parameters named lst1 and lst2.
#The function should combine these two lists into one new list and sort the result. Return the new sorted list.

def combine_sort(lst1, lst2):
    return sorted(lst1+lst2)

#test
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
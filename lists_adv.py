#problems found on Codecademy
#solutions created by Thomas Pelowitz, tpelowitz.com or github.com/tjpel

#-------------Question 1-------------------
print("Question 1")
#Create a function called every_three_nums that has one parameter named start.
#The function should return a list of every third number between start and 100 (inclusive). For example, every_three_nums(91) should return the list [91, 94, 97, 100]. If start is greater than 100, the function should return an empty list.

def every_three_nums(start):
    if start > 100: return []
    output = [start]
    while start < 98:
        start += 3
        output.append(start)
    return output

#tests
print(every_three_nums(91))

#-------------Question 2-------------------
print("Question 2")
#Create a function named remove_middle which has three parameters named lst, start, and end.
#The function should return a list where all elements in lst with an index between start and end (inclusive) have been removed.
#For example, the following code should return [4, 23, 42] because elements at indices 1, 2, and 3 have been removed:

def remove_middle(lst, start, end):
    return lst[:start] + lst[end+1:]

#tests
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

#-------------Question 3-------------------
print("Question 3")
#Create a function named more_frequent_item that has three parameters named lst, item1, and item2.
#Return either item1 or item2 depending on which item appears more often in lst.
#If the two items appear the same number of times, return item1.

def more_frequent_item(lst, item1, item2):
    if lst.count(item2) > lst.count(item1):
        return item2
    else: return item1

#tests
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

#-------------Question 4-------------------
print("Question 4")
#Create a function named double_index that has two parameters: a list named lst and a single number named index.
#The function should return a new list where all elements are the same as in lst except for the element at index. 
#The element at index should be double the value of the element at index of the original lst.
#If index is not a valid index, the function should return the original list.

def double_index(lst, index):
    if index < len(lst):
        lst[index] *= 2
    return lst

#tests
print(double_index([3, 8, -10, 12], 2))

#-------------Question 5-------------------
print("Question 5")
#Create a function called middle_element that has one parameter named lst.
#If there are an odd number of elements in lst, the function should return the middle element. 
#If there are an even number of elements, the function should return the average of the middle two elements.

def middle_element(lst):
    if len(lst) % 2 == 0:
        top_middle = lst[int(len(lst) / 2)]
        bottom_middle = lst[int(len(lst) / 2) - 1]
        return (top_middle + bottom_middle) / 2
    else: return lst[int(len(lst)/2)]

#tests
print(middle_element([5, 2, -10, -4, 4, 5]))
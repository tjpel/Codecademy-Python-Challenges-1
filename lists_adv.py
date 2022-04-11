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

print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

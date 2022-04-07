#problems found on Codecademy
#solutions created by Thomas Pelowitz, tpelowitz.com or github.com/tjpel

#-------------Question 1-------------------
print("Question 1")
#Create a function named in_range() that has three parameters named num, lower, and upper.
#The function should return True if num is greater than or equal to lower and less than or equal to upper. Otherwise, return False.

def in_range(num, lower, upper):
    if (num >= lower) and (num <= upper):
        return True
    else:
        return False

#tests
print(in_range(10, 10, 10)) #should print True
print(in_range(5, 10, 20)) #should print False

#-------------Question 2-------------------
print("Question 2")
#Create a function named same_name() that has two parameters named your_name and my_name.
#If our names are identical, return True. Otherwise, return False.

def same_name(your_name, my_name):
    if your_name == my_name:
        return True
    else:
        return False

#print
print(same_name("Colby", "Colby")) #should print True
print(same_name("Tina", "Amber")) #should print False

#-------------Question 3-------------------
print("Question 3")
#Create a function named always_false() that has one parameter named num.
#Using an if statement, your variable num, and the operators >, and <, make it so your function will return False no matter what number is stored in num.
#An if statement that is always false is called a contradiction. You will rarely want to do this while programming, but it is important to realize it is possible to do this.

def always_false(num):
    if num == 0 and num != 0:
        return True
    else:
        return False

#tests
print(always_false(0)) #should print False
print(always_false(-1)) #should print False
print(always_false(1)) #should print False

#-------------Question 4-------------------
print("Question 4")
#Create a function named movie_review() that has one parameter named rating.
#If rating is less than or equal to 5, return "Avoid at all costs!". If rating is between 5 and 9, return "This one was fun.". If rating is 9 or above, return "Outstanding!"

def movie_review(rating):
    if rating <= 5:
        return "Avoid at all costs!"
    elif rating > 5 and rating < 9:
        return "This one was fun."
    elif rating >= 9:
        return "Outstanding!"
    else:
        return "Error."

#tests
print(movie_review(9)) #should print "Outstanding!"
print(movie_review(4)) #should print "Avoid at all costs!"
print(movie_review(6)) #should print "This one was fun."

#-------------Question 5-------------------
print("Question 5")
#Create a function called max_num() that has three parameters named num1, num2, and num3.
#The function should return the largest of these three numbers. If any of two numbers tie as the largest, you should return "It's a tie!".

def max_num(num1, num2, num3):
    if num1 > num2 and num1 > num3: #num1 biggest
        return num1
    elif num2 > num1 and num2 > num3: #num2 biggest
        return num2
    elif num3 > num1 and num3 > num2: #num3 biggest
        return num3
    else: return "It's a tie!"

#tests
print(max_num(-10, 0, 10)) #should print 10
print(max_num(-10, 5, -30)) #should print 5
print(max_num(-5, -10, -10)) #should print -5
print(max_num(2, 3, 3)) #should print "It's a tie!"
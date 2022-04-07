#problems found on Codecademy
#solutions created by Thomas Pelowitz, tpelowitz.com or github.com/tjpel

#-------------Question 1-------------------
print("Question 1")
#Create a function named large_power() that takes two parameters named base and exponent.
#If base raised to the exponent is greater than 5000, return True, otherwise return False.

def large_power(base, exponent):
    if(base**exponent > 5000):
        return True
    else:
        return False

#tests
print(large_power(2,13)) #should print True
print(large_power(2,12)) #should print False

#-------------Question 2-------------------
print("Question 2")
#Create a function called over_budget that has five parameters named budget, food_bill, electricity_bill, internet_bill, and rent.
#The function should return True if budget is less than the sum of the other four parameters — you’ve gone over budget! Return False otherwise.

def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
  if(budget < (food_bill+electricity_bill+internet_bill+rent)):
    return True
  else:
    return False

#tests
print(over_budget(100, 20, 30, 10, 40)) #should print False
print(over_budget(80, 20, 30, 10, 30)) #should print True

#-------------Question 3-------------------
print("Question 3")
#Create a function named twice_as_large() that has two parameters named num1 and num2.
#Return True if num1 is more than double num2. Return False otherwise.

def twice_as_large(num1, num2):
    if num1 > 2*num2:
        return True
    else:
        return False

#tests
print(twice_as_large(10, 5)) #should print False
print(twice_as_large(11, 5)) #should print True

#-------------Question 4-------------------
print("Question 4")
#Create a function called divisible_by_ten() that has one parameter named num.
#The function should return True if num is divisible by 10, and False otherwise. Consider using modulo operator % to check for divisibility.

def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False

#tests
print(divisible_by_ten(20)) #should print True
print(divisible_by_ten(25)) #should print False

#-------------Question 5-------------------
print("Question 5")
#Create a function named not_sum_to_ten() that has two parameters named num1 and num2.
#Return True if num1 and num2 do not sum to 10. Return False otherwise.

def not_sum_to_ten(num1, num2):
    if num1 + num2 == 10:
        return False
    else:
        return True

def not_sum_to_ten_alt(num1, num2):
    if num1 + num2 != 10:
        return True
    else:
        return False

#tests
print(not_sum_to_ten(9, -1)) #should print True
print(not_sum_to_ten(9, 1)) #should print False
print(not_sum_to_ten_alt(5,5)) #should print False
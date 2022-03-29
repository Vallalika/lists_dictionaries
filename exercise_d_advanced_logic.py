# For the following list of numbers:

from logging import BufferingFormatter
from operator import index
from termios import OFDEL


numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_list = []

for number in numbers:
    if number % 2 == 0:
        even_list.append(number)

print(even_list)


# 2. Print the difference between the largest and smallest value:
numbers.sort()
diff = numbers[-1] - numbers[0]
print(diff)

# 3. Print True if the list contains a 2 next to a 2 somewhere.
# print("Exercise 3:")
# print(numbers)

# # for each number in the list
# for number in numbers:
#     print("My number is ", number)

#     # track 2s
#     temp = 0

#     # if my number is 2 and temp is not 2:
#     if number == 2 and temp != 2:
#         print("entering number == 2 and temp != 2")

#         # store number in temp variable
#         temp = 2
#         print("value of temp is", temp)

#     # if my number is 2 and temp is also 2:
#     elif number == 2 and temp == 2:

#         # return True and break out of the loop
#         print(True)
#         break

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 








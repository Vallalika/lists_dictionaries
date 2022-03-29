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
print("")
print("Exercise 3:")
print("")

# is there a 2 in NUMBERS?
if 2 in numbers:
    # if yes, loop through every NUMBER in NUMBERS
    for number in numbers:
        # If NUMBER is 2
        if number == 2:
            # Find out its index and store it in INDEX
            index = numbers.index(number)
            # If INDEX is not the last one in the list and also the next number up is a 2
            if (index != len(numbers)-1) and (numbers[index+1] == 2):
                # then print True and break out of the loop
                print("True")
                break   

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22
    
    # Set up a SUM variable to add on to it, and an IGNORE variable to keep track of 6 and 7
    numbers = [11, 99, 6, 4, 99, 7, 11]
    
    sum = 0
    ignore = 0

    # Initiate a for loop for every NUMBER in NUMBERS
    for number in numbers:

        # If NUMBER is equal to 6 or 7:
        if (number == 6) or (number == 7):

            # Store it in the IGNORE variable
            ignore = number

        # Otherwise i.e. the number is neither a 6 nor a 7
        else:

            # If the value of IGNORE is NOT 6
            if ignore != 6:

                # Add NUMBER to SUM variable
                sum += number

    print(f"My sum is: {sum}")

# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 








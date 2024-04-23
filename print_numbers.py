# To print numbers
# Hi ishika
# Here's a Python script based on the logic you provided to print numbers from 1 to 100 with specific conditions:
# You can save this code in a Python file (e.g., print_numbers.py) and execute it as described in the previous message. This script will loop from 1 to 100 and print "buzzbam" for numbers divisible by both 3 and 5, "buzz" for numbers divisible by 3, "bam" for numbers divisible by 5, and the number itself for other numbers.
#############################################
start = 1
end = 100

while start <= end:
    if start % 3 == 0 and start % 5 == 0:
        print("buzzbam")
    elif start % 3 == 0:
        print("buzz")
    elif start % 5 == 0:
        print("bam")
    else:
        print(start)
    start += 1
##############################################
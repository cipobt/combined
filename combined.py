#This program reads from two different text ﬁles containing Integers sorted from smallest to largest and combines
#the content of both files into a third file where all the numbers are sorted from smallest to largest

#Reading from existing files
fa = open('numbers1.txt', 'r')
fb = open('numbers2.txt', 'r')

#Creating a temporary list to produce the third file later on
num_list = []

#Reading from the existing files and adding the numbers in no particular order to the temporary list
data = fa.readlines()
for line in data:
    num_list.append(int(line))

data = fb.readlines()
for line in data:
    num_list.append(int(line))

#Organizing the numbers from smallest to largest
sorted_nums = sorted(num_list)

#Creating the third file all_numbers
output = open('all_numbers.txt', 'w')

#Adding the sorted list of numbers to the new file
for num in sorted_nums:
    output.write(f"{num}\n")

#Closing the files
fa.close()
fb.close()
output.close()

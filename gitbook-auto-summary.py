# -*- coding: utf-8 -*-
# Author Frank Hu
# GitBook auto summary
# import all csv files in a folder

import os
import re

combine = [] #combined protein list

dir_input = input('Please input folder path(e.g. D:\Study\Inbox): ')
print('input directory is: ', dir_input) 

# output to flie
output = open(os.path.join(dir_input, 'SUMMARY.md'), 'w') # output to dir_input with "SUMMARY.md"
output.write('# Summary\n\n')
# todo: check summary.md in later versions (if overwrite)
# todo: seems that only windows uses \, os uses / for directory, need to test
    # uses os.path.join .normcase


def output_markdown(dire, iter_length=0):
    for filename in os.listdir(dire): # add list
        print('Processing: reading', filename) # output log
        # print(os.path.join(dire, filename))
        if os.path.isdir(os.path.join(dire, filename)):
            # is dir, iteration
            output.write('  ' * iter_length + '- ' + filename + '\n') # write dir information
            output_markdown(os.path.join(dire, filename), iter_length + 1) # iteration
        else:
            # isfile
            if re.search('.md$', filename): # re to find target markdown files, $ for matching end of filename
                # print(filename, filename[:-3], 'match') # string cut using pathonic slicing :) (https://docs.python.org/3.4/tutorial/introduction.html#strings)
                if filename != 'SUMMARY.md': # escape SUMMARY.md
                    # print(os.path.join(os.path.relpath(dire, dir_input), filename))
                    output.write('  ' * iter_length + '- [%s](%s)\n'%(filename[:-3], os.path.join(os.path.relpath(dire, dir_input), filename)))
                    # iterlength for indent, then output markdown list, uses relpath and join.

output_markdown(dir_input)

print('auto summary finished:)')
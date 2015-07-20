# -*- coding: utf-8 -*-
# Author Frank Hu
# GitBook auto summary
# summary all .md files in a GitBook folder

import os
import re

def output_markdown(dire, base_dir, output_file, iter_depth=0):
    """Main iterator for get information from every file/folder

    i: directory, base dire(for calulate relative path), output file, iter depth.
    o: write .md information (with identation) to output_file.
    """
    for filename in sort_dir_file(os.listdir(dire), base_dir): # add list and sort
        print('Processing: reading', filename) # output log
        # print(os.path.join(dire, filename))
        if os.path.isdir(os.path.join(dire, filename)):
            # is dir, iteration
            output_file.write('  ' * iter_depth + '- ' + filename + '\n') # write dir information
            output_markdown(os.path.join(dire, filename), base_dir, output_file, iter_depth + 1) # iteration
        else:
            # isfile
            if re.search('.md$', filename): # re to find target markdown files, $ for matching end of filename
                # print(filename, filename[:-3], 'match') # string cut using pathonic slicing :) (https://docs.python.org/3.4/tutorial/introduction.html#strings)
                if filename != 'SUMMARY.md': # escape SUMMARY.md
                    # print(os.path.join(os.path.relpath(dire, dir_input), filename))
                    output_file.write('  ' * iter_depth + 
                        '- [%s](%s)\n'%(filename[:-3], os.path.join(os.path.relpath(dire, base_dir), filename)))
                    # iter length for indent, then output markdown list, uses relpath and join.

def sort_dir_file(listdir, dire):
    # sort dirs and files, first files a-z, then dirs a-z
    list_of_file = []
    list_of_dir = []
    for filename in listdir:
        if os.path.isdir(os.path.join(dire, filename)):
            list_of_dir.append(filename)
        else: 
            list_of_file.append(filename)
    for dire in list_of_dir:
        list_of_file.append(dire)
    return list_of_file 

def main():
    combine = [] #combined protein list

    dir_input = input('Please input path(e.g. D:/Study/Inbox): ')
    print('Input directory is: ', dir_input) 

    # output to flie
    output = open(os.path.join(dir_input, 'SUMMARY.md'), 'w') # output to dir_input with "SUMMARY.md"
    output.write('# Summary\n\n')
    # todo: seems that only windows uses \, os/linux uses / for directory, need to test
    output_markdown(dir_input, dir_input, output)

    print('auto summary finished:)')
    return 0

if __name__ == '__main__':
    main()
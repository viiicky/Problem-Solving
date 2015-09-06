#!/usr/bin/env python3
# To write every line containing the word 'hello' in 10 files in another 11th file 
# Found this question on glassdoor.
# https://www.glassdoor.co.in/Interview/To-write-every-line-containing-the-word-and-amp-039-hello-and-amp-039-in-10-files-in-another-11th-file-QTN_1044132.htm

import re
regex = re.compile(r'\bhello\b')

fout = open('./output.txt', 'w')

for x in range(10):
    fin = open(input('Enter complete path for file {0}: '.format(x+1)))
    print('Please wait for a while...')
    for line in fin:
        if regex.search(line.lower()):  # search scans the complete string, whereas match matches only at the beginning.
            fout.write(line)
    fin.close()
fout.close()
print('Done')

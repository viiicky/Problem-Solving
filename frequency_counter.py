#!/usr/bin/env python3
# You are given a word document,
# you have to print the words with frequencies.
# Now print the kth rank word in terms of frequency.
# Print top k words as well by frequencies.
# Found this question on careercup:
# http://www.careercup.com/question?id=5702564332961792
#
# If n is the number of words present in the given document,
# then the below solution runs in O(n) time.
# Vikas Prasad
# 4 September 2015

import re

def frequency_counter(file_path, k):
    # for word documents
    # found this piece of code for fetching contents from docx file on SO, User name: benjamin
    import zipfile
    content = ""
    try:
        docx = zipfile.ZipFile(file_path)   # Load Docx into zipfile
    except FileNotFoundError:
        print('File not found.')
        exit()
    unpacked = docx.infolist()  # Unpack zipfile
    for item in unpacked:       # Find the /word/document.xml file in the package and assign it to variable
        if item.orig_filename == 'word/document.xml':
            content = docx.read(item.orig_filename)
            break
    # print(content)

    # docx file contain lot of xml, thus removing tags.
    # stripping <> tags and changing & to and
    stripped_content = re.compile(b'<.*?>').sub(b' ', content)  # strip tags
    stripped_content = re.compile(b'&amp;').sub(b'and', stripped_content )   # change & to and
    
    '''
    # for txt files
    try:
        fobj = open(file_path)
    except FileNotFoundError:
        print('File not found.')
        exit()
    content = fobj.read()       # please note its better to read line by line and then performing subsequent operations,
    stripped_content = content  # to make it memory efficient. Doing this way to generalise the function with docx file.
    # also for .txt files replace all b(byte) in re methods with r(str)
    '''
    # print(stripped_content)

    # Main logic starts here
    # Creating a words: frequency dictionary
    stripped_content = stripped_content.lower() # handling cases
    words_frequency = {}
    max_frequency = 1        # (will have to check this for zero word document, not an issue for now)
    words = re.compile(b'[A-Za-z]+').findall(stripped_content) # list of all the words in stripped_content
    # print(words)

    for w in words:     # create dictionary
        # if n is the number of words, this runs in O(n)
        try:
            words_frequency[w] += 1
            if words_frequency[w] > max_frequency:
                max_frequency = words_frequency[w]
        except KeyError:
            words_frequency[w] = 1
 
    # print words with frequencies
    print('Words with their frequencies:')
    for word in words_frequency:
        # O(n)
        print(word, words_frequency[word])
    print()

    # now replacing frequencies with ranks
    for word in words_frequency:
        # O(n)
        words_frequency[word] = max_frequency - words_frequency[word]

    # temp array to hold actual positions of words in the rank array
    temp_array = [[0] for _ in range(max_frequency)]
    for word in words_frequency:
        # O(n)
        temp_array[words_frequency[word]][0] = 1        # mark all positions which are a valid rank, leave rest unmarked
        temp_array[words_frequency[word]].append(word)  # append respective words

    for i, x in enumerate(temp_array[1 : ]):    # add up the array left to right to get the position for rank array
        # size of temp_array is max_frequency
        # thus this loop runs max_freqency - 1 time
        # aparrantly max_frequency <= n
        # thus this runs ins <= O(n)
        x[0] += temp_array[i][0]

    # rank array holds actual rank scaled down to 1
    rank_array = [[] for _ in range(temp_array[-1][0] + 1)]
    for word in words_frequency:
        # O(n)
        rank_array[temp_array[words_frequency[word]][0]].extend(temp_array[words_frequency[word]][1:])  # append words at the respective ranks
        temp_array[words_frequency[word]] = temp_array[words_frequency[word]][:1]       # remove words from temp array, so that they do not get reappended for same rank words in words_frequency

    print('Word(s) with rank', k, ': ', rank_array[k])
    print()

        
    print('Top', k, 'words are:')
    for i, words in enumerate(rank_array[1 : k+1]):
        print(i+1, words)
    print()

if __name__ == '__main__':
    # file_path = '/home/vikasprasad/classesPython.txt'
    # file_path = '/home/vikasprasad/cc.txt'
    # file_path = '/home/vikasprasad/CV.docx'
    file_path = input('Enter complete path for word document: ')
    # k = 5
    k = int(input('Enter value of k: '))
    frequency_counter(file_path, k)

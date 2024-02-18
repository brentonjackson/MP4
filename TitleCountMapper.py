#!/usr/bin/env python3

import sys
import string



stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]


# TODO
allWords = []
with open(stopWordsPath) as f:
    # TODO
        commonWords = f.read().split('\n')
print(commonWords)
#TODO
with open(delimitersPath) as f:
    # TODO
        delimiters = f.read()

for line in sys.stdin:
        #TODO Tokenize Wikipedia titles using provided delimiters in delimiters.txt
        for delimiter in delimiters:
        #       print("delimiter: ", delimiter)
                line = line.strip().strip('\t').strip("    ").strip("   ").strip('\n').strip('\r\n').replace(delimiter, ';')
        words = line.split(';')
       #TODO Make tokens lowercased and remove common words
        for token in words:
                if token.isspace() or token.strip() == '':
                        continue
                if (token.strip().lower() not in commonWords):
                        #print(token, "token space?", token.isspace())
                        allWords.append((token.lower().strip(), 1)) # add tuple to allwords list

for item in allWords:
        print('%s\t%s' % (item[0],item[1]))
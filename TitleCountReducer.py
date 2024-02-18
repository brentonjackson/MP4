#!/usr/bin/env python3
from operator import itemgetter
import sys

#TODO
wordMap = {}
# input comes from STDIN
for line in sys.stdin:
    # TODO
        wordMap[line.split('\t')[0]] = wordMap.get(line.split('\t')[0], 0) + 1

for item in wordMap.items():
        print('%s\t%s' % (item[0]  ,item[1]  )) #print as final output
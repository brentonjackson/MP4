#!/usr/bin/env python3
import sys

#TODO
linkMap = {}
# input comes from STDIN
for line in sys.stdin:
    # TODO
        linkMap[line.split('\t')[0]] = linkMap.get(line.split('\t')[0], 0) + 1

# TODO
for item in linkMap.items():
        print('%s\t%s' % (item[0], item[1]))
# print('%s\t%s' % (  ,  )) print as final output
#!/usr/bin/env python3
import sys


leaguePath = sys.argv[1]
#TODO


with open(leaguePath) as f:
        #TODO
        leaguePages = f.read().split()

for line in sys.stdin:

       #TODO
        parts = line.split()
        if len(parts) != 2:
                continue
        link, linkCount = parts
        if link in leaguePages:
                print(line)
       # print('%s\t%s' % (  ,  )) pass this output to reducer
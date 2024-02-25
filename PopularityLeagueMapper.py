#!/usr/bin/env python3
import sys


leaguePath = sys.argv[1]
#TODO


with open(leaguePath) as f:
        #TODO
        leaguePages = [int(line.strip()) for line in f]
for line in sys.stdin:
       #TODO
        line = line.strip()
        if line.isspace():
                continue
        parts = line.split()
        if len(parts) != 2:
                continue
        link, linkCount = parts
        if int(link) in leaguePages:
                print('%s\t%s' % (link, linkCount))

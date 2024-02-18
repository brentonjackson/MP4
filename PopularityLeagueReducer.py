#!/usr/bin/env python3
import sys
#TODO
data = []

# input comes from STDIN
for line in sys.stdin:
    # TODO
        parts = line.split()
        if len(parts) != 2:
                continue
        data.append(parts)

pageRanks = []
for i, (link1, count1) in enumerate(data):
        pageRank = 0
        for j, (link2, count2) in enumerate(data):
                if i != j:
                        if int(count2) < int(count1):
                                pageRank += 1
        pageRanks.append((link1, pageRank))

sorted_pages = sorted(pageRanks, key=lambda x: int(x[0]), reverse=True)


for page in sorted_pages:
        print('%s\t%s' % (page[0],page[1]))
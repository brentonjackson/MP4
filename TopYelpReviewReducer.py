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
        id, score = parts
        data.append((id, float(score)))
#TODO sort data
sorted_data = sorted(data, key=lambda x: x[1], reverse=True)
top_10 = sorted_data[-10:]
for item in top_10:
        print(item[0])
# print('%s\t%s' % (  ,  )) print as final output
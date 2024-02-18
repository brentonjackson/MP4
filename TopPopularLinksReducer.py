#!/usr/bin/env python3
import sys


data = []
# input comes from STDIN
for line in sys.stdin:
    # TODO
        parts = line.split()
        if len(parts) != 2:
                continue
        link, count = parts
        data.append((link, int(count)))

    # print('%s\t%s' % (  ,  )) print as final output
sorted_data = sorted(data, key=lambda x: (x[1], x[0]))
top_10 = sorted_data[-10:]
for item in top_10:
        print('%s\t%s' % (item[0],item[1]))
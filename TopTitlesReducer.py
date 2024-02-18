#!/usr/bin/env python3
import sys


# input comes from STDIN
data = []
for line in sys.stdin:
#       print(line)
        parts = line.split()
#       print("parts: %s, %s" % (parts[0], parts[1]))
        if len(parts) != 2:
#               print(f"Error: Unexpected input format - {line}")
                continue
        word, count = parts
        data.append((word, int(count)))

#print("data: ", data)
#TODO sort data by count then key
sorted_data = sorted(data, key=lambda x: (x[1], x[0]))
#print(sorted_data)
top_10 = sorted_data[-10:]
for item in top_10:
        print('%s\t%s' % (item[0],item[1]))
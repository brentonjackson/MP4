#!/usr/bin/env python3
import sys
import math


data = []
for line in sys.stdin:
    # TODO
        parts = line.split()
        if len(parts) != 2:
#               print(f"Error: Unexpected input format - {line}")
                continue
        word, count = parts
        data.append((word, int(count)))

counts = [count for _, count in data]
mean = math.floor(sum(counts) / len(counts))
total_sum = math.floor(sum(counts))
minimum = math.floor(min(counts))
maximum = math.floor(max(counts))
variance = math.floor(sum((count - mean) ** 2 for count in counts))


#TODO
# print('%s\t%s' % (  ,  )) print as final output
print(f"Mean:\t{mean}")
print(f"Sum:\t{total_sum}")
print(f"Minimum:\t{minimum}")
print(f"Maximum:\t{maximum}")
print(f"Variance:\t{variance}")
#!/usr/bin/env python3
import sys


#TODO setup data structures for orphans, keys, and linked sets
orphans = []
linked = set()
keys = set()


for line in sys.stdin:
  # TODO populate keys and linked sets
        parts = line.split(':')
        if len(parts) != 2:
                continue
        key, links = parts
        keys.add(key)
        for id in links.split():
                linked.add(id)


#TODO compile list of orphans
for key in keys:
        if key not in linked:
                orphans.append(key)
sorted_orphans = sorted(orphans, key=int)
# print(xx) print as final output
for orphan in sorted_orphans:
        print(orphan)
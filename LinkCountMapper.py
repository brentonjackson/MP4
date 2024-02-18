#!/usr/bin/env python3
import sys

allLinks = []
for line in sys.stdin:
  #TODO
        parts = line.split(':')
        if len(parts) != 2:
                continue
        key, links = parts
        for link in links.split():
                allLinks.append((link, 1))

for item in allLinks:
        print('%s\t%s' % (item[0], item[1]))
  # print('%s\t%s' % (  ,  )) pass this output to reducer
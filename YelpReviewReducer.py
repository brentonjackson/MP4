#!/usr/bin/env python3
from operator import itemgetter
import sys

#TODO
businessData = {}

# input comes from STDIN
for line in sys.stdin:
    # TODO
        line = eval(line)
        key = line['businessId']
        if key not in businessData:
                businessData[key] = {"sumStarsTimesLength": 0, "numReviews": 0}
        businessData[key]["sumStarsTimesLength"] += line["stars"] * len(line["reviewText"])
        businessData[key]["numReviews"] += 1

#TODO calculate weighted scores
scores = []
for businessId, data in businessData.items():
        if data["numReviews"] != 0:
                score = data["sumStarsTimesLength"] / data["numReviews"]
                scores.append((businessId, score))

# TODO
# print('%s\t%s' % (  ,  )) print as final output
for item in scores:
        print('%s\t%s' % (item[0], item[1]))
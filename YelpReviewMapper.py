#!/usr/bin/env python3

import sys
import string
import json

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]

#TODO
with open(stopWordsPath) as f:
    #TODO
        commonWords = f.read().split('\n')

#TODO
with open(delimitersPath) as f:
    #TODO
        delimiters = f.read()

newData = []
for line in sys.stdin:
    # TODO get all parts of line from json
        data = json.loads(line) # json dict now
        #TODO calculate avg stars
        stars = data['stars'] - 3


        #TODO make tokens lowercase and remove stopwords
        reviewText = data['text']
        parsedText = []
        for delimiter in delimiters:
                reviewText = reviewText.strip().replace(delimiter, ';')
        words = line.split(';')
        for token in words:
                if token.isspace() or token.strip() == '':
                        continue
                if (token.strip().lower() not in commonWords):
                        parsedText.append(token.lower().strip())

        #TODO add desired data to list
        dataObj = {}
        dataObj['businessId'] = data["business_id"]
        dataObj['stars'] = stars
        dataObj['reviewText'] = parsedText
        newData.append(dataObj)



    # print('%s\t%s' % (  ,  )) pass this output to reducer
for item in newData:
        print(item)
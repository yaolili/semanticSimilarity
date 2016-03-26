#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     umbcAPI.py
# ROLE:     TODO (some explanation)
# CREATED:  2016-03-25 18:46:06
# MODIFIED: 2016-03-25 21:36:30

import sys
import os
import time
import urllib
import urllib2
import scipy.stats
from utility import Utility

#The type of data is dict => data[w1:w2] = float(score)
#Here you cannot use score and you should calculate it by yourself.

def getScore(w1, w2):
    url = "http://swoogle.umbc.edu/SimService/GetSimilarity"
    data = {
            "operation" : "api",
            "phrase1" : w1,
            "phrase2" : w2
            }
            
    data = urllib.urlencode(data)
    request = urllib2.Request(url, data)
    response = urllib2.urlopen(request)
    return response.read()



def useAPI(data):
    originScore = []
    newScore = []
    #Here print i in order to know the process
    i = 1
    for key in data:
        originScore.append(data[key])
        w1, w2 = key.strip().split(":")
        score = getScore(w1, w2)
        if score == "-inf":
            newScore.append(-1)
        else:
            newScore.append(float(score))
        print i
        i += 1
    return scipy.stats.spearmanr(originScore, newScore)[0]

        
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "sys.argv[1]: read filePath!"
        print "sys.argv[2]: write filePath!"
        exit()
        
    utilityInstance = Utility()
    data = utilityInstance.readData(sys.argv[1])
    spearmanr = useAPI(data)
    utilityInstance.writeData("umbc", spearmanr, sys.argv[1], sys.argv[2])
        
    
    

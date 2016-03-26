#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     w2v.py
# ROLE:     TODO (some explanation)
# CREATED:  2016-03-26 16:37:48
# MODIFIED: 2016-03-26 17:36:30

import os
import sys
import time
import gensim
import scipy.stats
from utility import Utility

def embedding(data):
    originScore = []
    newScore = []
    start = time.clock()
    model = gensim.models.Word2Vec.load_word2vec_format('./data/GoogleNews-vectors-negative300.bin', binary = True) 
    end = time.clock()
    print (end - start)
    i = 1
    for key in data:
        originScore.append(data[key])
        w1, w2 = key.strip().split(":")
        score = model.similarity(w1, w2)
        newScore.append(float(score))
        print i
        i += 1
        # if i > 5:
            # print originScore
            # print newScore
            # print scipy.stats.spearmanr(originScore, newScore)[0]
            # exit()
    return scipy.stats.spearmanr(originScore, newScore)[0]
    
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "sys.argv[1]: read filePath!"
        print "sys.argv[2]: write filePath!"
        exit()
        
    utilityInstance = Utility()
    data = utilityInstance.readData(sys.argv[1])
    spearmanr = embedding(data)
    utilityInstance.writeData("w2v", spearmanr, sys.argv[1], sys.argv[2])


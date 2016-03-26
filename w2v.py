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
    newData = {}
    model = gensim.models.Word2Vec.load_word2vec_format('./data/GoogleNews-vectors-negative300.bin', binary = True) 
    i = 1
    for key in data:
        w1, w2 = key.strip().split(":")
        score = model.similarity(w1, w2)
        newData[key] = float(score)
        print i
        i += 1
    return newData
    
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "sys.argv[1]: read filePath!"
        print "sys.argv[2]: write filePath!"
        exit()
        
    utilityInstance = Utility()
    data = utilityInstance.readData(sys.argv[1])
    newData = embedding(data)
    utilityInstance.generateFile(sys.argv[2], newData)
    #utilityInstance.writeData("w2v", spearmanr, sys.argv[1], sys.argv[2])


#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     wordNet.py
# ROLE:     TODO (some explanation)
# CREATED:  2016-03-26 18:36:39
# MODIFIED: 2016-03-26 18:37:15

import sys
import os
import scipy.stats
from nltk.corpus import wordnet_ic
from nltk.corpus import wordnet as wn
from utility import Utility

def maxScore(obj1, obj2, method):
    bestScore = -1
    brown_ic = wordnet_ic.ic('ic-brown.dat')
    semcor_ic = wordnet_ic.ic('ic-semcor.dat')
    bnc_ic = wordnet_ic.ic('ic-bnc.dat')
    for i in range(len(obj1)):
        for j in range(len(obj2)):
            pos1 = obj1[i].pos()
            pos2 = obj2[j].pos()
            if method == "wup":
                score = obj1[i].wup_similarity(obj2[j])
            elif method == "res":
                if (pos1 != pos2) or pos1 == "s" or pos1 == "a":
                    continue
                #score = obj1[i].res_similarity(obj2[j], brown_ic)
                score = obj1[i].res_similarity(obj2[j], bnc_ic)
            elif method == "jcn":
                if (pos1 != pos2) or pos1 == "s" or pos1 == "a":
                    continue
                #score = obj1[i].jcn_similarity(obj2[j], brown_ic)
                score = obj1[i].jcn_similarity(obj2[j], bnc_ic)
            else:
                if (pos1 != pos2) or pos1 == "s" or pos1 == "a":
                    continue
                #score = obj1[i].lin_similarity(obj2[j], semcor_ic) 
                #score = obj1[i].lin_similarity(obj2[j], brown_ic)
                score = obj1[i].lin_similarity(obj2[j], bnc_ic) 
            if score != "None" and score > bestScore:
                bestScore = score
    return bestScore

def wordNet(data, method):
    newData = {}
    i = 1
    for key in data:
        w1, w2 = key.strip().split(":")
        obj1 =  wn.synsets(w1)
        obj2 = wn.synsets(w2)
        score = maxScore(obj1, obj2, method)
        newData[key] = float(score)
        print i
        i += 1
    return newData
    

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print "sys.argv[1]: read filePath!"
        print "sys.argv[2]: write filePath!"
        print "sys.argv[3]: wordNet method!"
        exit()
        
    utilityInstance = Utility()
    data = utilityInstance.readData(sys.argv[1])
    newData = wordNet(data, sys.argv[3])
    utilityInstance.generateFile(sys.argv[2], newData)
    #utilityInstance.writeData(sys.argv[3], spearmanr, sys.argv[1], sys.argv[2])




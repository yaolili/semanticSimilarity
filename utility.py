#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     utility.py
# ROLE:     TODO (some explanation)
# CREATED:  2016-03-26 08:57:59
# MODIFIED: 2016-03-26 09:00:43

import sys
import os
import scipy.stats

class Utility:
    def __init__(self):
        self.data = {}
        self.key = []
        
    def readData(self, filePath):
        with open(filePath, "r") as fin:
            for i, line in enumerate(fin):
                if i == 0:
                    continue
                aList = line.strip().split("\t")
                w1 = aList[0]
                w2 = aList[1]
                score = float(aList[2])
                key = w1 + ":" + w2
                self.key.append(key)
                self.data[key] = score
        print "readData done!"
        return self.data
    
    #Function writeData() is useless!
    # def writeData(self, method, spearmanr, readFile, writeFile):
        # result = open(writeFile, "a+")
        # result.write(readFile + "\t" + method + "\t" + str(spearmanr) + "\n" )
        # print "writeData done!"
        # result.close()
        
    def generateFile(self, writeFile, newData):
        result = open(writeFile, "w+")
        result.write("Word1" + "\t" + "Word2" + "\t" + "Score" + "\n")
        originScore = []
        newScore = []
        for i in range(len(self.key)):
            key = self.key[i]
            w1, w2 = key.strip().split(":")
            result.write(w1 + "\t" + w2 + "\t" + str(newData[key]) + "\n")
            originScore.append(self.data[key])
            newScore.append(newData[key])
        spearmanr = scipy.stats.spearmanr(originScore, newScore)[0]
        result.write(str(spearmanr))
        result.close()
            
#test code        
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "sys.argv[1]: filePath!"
        exit()
    testInstance = Utility()
    testInstance.readData(sys.argv[1])
    
        


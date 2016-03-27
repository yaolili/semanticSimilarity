# semanticSimilarity

(1) 运行wordNet.py的命令： python  wordNet.py  your_dataSet  resultFilePath  your_Method
其中 your_dataSet是指数据集，resultFilePath是指输出的文件，your_Method是指基于wordNet的有lin、wup、jcn、res这四种方法，
分别对应（Lin、Wu-Palmer、Jiang-Conrath、Resnik的方法）可任选一种进行实验。
因此示例的命令为： python  wordNet.py  set1.tab  lin/result1.csv  lin

(2) 运行umbcAPI.py的命令：python  umbcAPI.py  your_dataSet  resultFilePath
示例的命令为： python  umbcAPI.py  set1.tab  umbc/result1.csv

(3) 运行w2v.py的命令： python  w2v.py  your_dataSet  resultFilePath
示例的命令为：python  w2v.py  set1.tab  w2v/result1.csv

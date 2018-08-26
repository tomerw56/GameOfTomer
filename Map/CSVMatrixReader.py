import csv
import numpy as np
import os.path
from Common.Point import Point
class CSVMatrixReader:
    def __init__(self):
        self._RowCount = 0
        self._RestPoints=[]
        self._FileLoaded=False

    def parse(self,fileName):
        if os.path.isfile(fileName)==False:
            return False
        RowList=[]
        with open(fileName, 'r', newline='') as csvfile:
            spamreader = csv.reader(csvfile)
            for row in spamreader:
                RowList.append(row)
        self._RowCount = len(RowList)
        if(self._RowCount==0):
            print("No rows Found")
            return False


        self._Matrix=np.asmatrix(np.ones((self._RowCount, self._RowCount)))
        for index in range(0,len(RowList)):
            row=RowList[index]
            rowlen=len(row)
            if(rowlen!=self._RowCount):
                print("Row {0} is with {1} Items -which makes the file not square".format(index,rowlen))
                return False
            for rowIndex in range(0,rowlen):
                if int(row[rowIndex])==0:
                    self._RestPoints.append(Point(rowIndex,index))

                self._Matrix .itemset((index, rowIndex),row[rowIndex])
        self._FileLoaded=True
        return True

    @property
    def fileLoaded(self):
        return self._FileLoaded

    @property
    def Matrix(self):
        return self._Matrix

    @property
    def restpoints(self):
        return self._RestPoints



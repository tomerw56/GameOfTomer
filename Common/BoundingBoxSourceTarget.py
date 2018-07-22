from Common.Point import Point
import numpy as np;


class BoundingBoxSourceTarget:
    def __init__(self,map:np.matrix,p1:Point,p2:Point,margin=0):
        pass;
        self._szX, self._szY = map.shape
        self._top_Left_X=max(round((min(p1.x,p2.x))-margin),1);
        self._top_Left_Y = max(round((min(p1.y, p2.y)) - margin), 1);
        self._bottom_Right_X = min(round(max(p1.x, p2.x)  + margin), self._szX)
        self._bottom_Right_Y = min(round(max(p1.y, p2.y) + margin), self._szY)
        self._Valid=self._bottom_Right_Y<=self._szY;
        winsize_X=self._bottom_Right_X-self._top_Left_X+1
        winsize_Y = self._bottom_Right_Y - self._top_Left_Y + 1;
        self._BB=[self._top_Left_X,self._top_Left_Y,winsize_X,winsize_Y]
        self._DSMSubset=map[self._top_Left_X: self._top_Left_X+winsize_X,self._top_Left_Y: self._top_Left_Y+winsize_Y];



    @property
    def bb(self):
        return self._BB

    @property
    def dsmSubset(self):
        return self._DSMSubset

    @property
    def valid(self):
        return self._Valid

    @property
    def topleftX(self):
        return self._top_Left_X

    @property
    def topleftY(self):
        return self._top_Left_Y



    def __str__(self):
        if self._Valid==False:
            return 'Not Valid'

        return 'BB= {1}'.format(self._BB)

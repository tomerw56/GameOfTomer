
from Utils.ConfigProvider import ConfigProvider
from Common.Point import Point
class PlayerStatFacade():
    def __init__(self,id:int):
        self._Position=Point(0,0)
        self._ID = int(id)
        self._Score=0
        self._TimeInPosition=0
        self._IsDestoryed=False
        self._IsThretened=False
        self._ThreatenedTime=0
        self._ThreateningTime=0
        self._RestPointTime=0



    @property
    def id(self):
        return self._ID

    @property
    def position(self):
        return self._Position

    @property
    def score(self)->int:
        return self._Score

    @property
    def Threatened(self):
        return self._IsThretened


    @property
    def destroyed(self)->int:
        return self._IsDestoryed

    @property
    def timeinposition(self)->int:
        return self._TimeInPosition
    @property
    def threatenedTime(self)->int:
        return self._ThreatenedTime
    @property
    def threateningTime(self)->int:
        return self._ThreateningTime


    def __str__(self):
        return 'ID={0} Score= {1} Position={2} TimeInPosition={3} ThreatenedTime={4} ThreateningTime={5}'.format(self._ID, self._Score,self._Position,self._TimeInPosition,self._ThreatenedTime,self._ThreateningTime)

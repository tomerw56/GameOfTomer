from Engine.Recording.Decoder import Decoder
from Engine.Recording.Decoder import Decoder
from Engine.GameDraw.GameDrawing import GameDrawing
from Map.CSVMatrixReader import CSVMatrixReader


class PlayBackMode(object):
    def __init__(self,folder):
        self._decoder = Decoder(folder)
        self._gamestates =  self._decoder.DecodeAllStates()
        self._gamemetadata=self._decoder.DecodeMetaData()
        self._Valid=len(self._gamestates)>0

    def Play(self):
        if(self._Valid):
            csvreader = CSVMatrixReader()
            csvreader.parse(self._gamemetadata.infrapath)
            if(csvreader.fileLoaded):
                drawMatch = GameDrawing(csvreader.Matrix, self._gamestates)

    @property
    def valid(self) -> bool:
        return self._Valid

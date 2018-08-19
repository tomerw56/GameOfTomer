from Engine.Common.Facade.Enums import WinnigPlayer
from Engine.Common.Facade.Enums import WinnigReason
class VictoryAnalysis():
    def __init__(self,winner=WinnigPlayer.NO_WINNER,winningireason=WinnigReason.NO_WIN):
        self._winner=winner
        self._winningireason=winningireason
    @property
    def winner(self):
        return self._winner

    @property
    def winningireason(self):
        return self._winningireason


    @winner.setter
    def winner(self, value):
        self._winner = value

    @winningireason.setter
    def winningireason(self, value):
        self._winningireason = value

    def __str__(self):
        return 'Winner={0} WinningReason= {1}'.format(self._winner, self._winningireason)
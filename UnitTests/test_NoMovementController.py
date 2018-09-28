from unittest import TestCase

from Common.Point import Point
from Engine.Controllers.ControllersEnums import PlayerNoMovmentState
from Engine.Controllers.NoMovementController import NoMovementController
from Utils.UnitTestDummyConfigProvider import UnitTestDummyConfigProvider


class test_NoMovementController(TestCase):
    def setUp(self):

        self._ConfigProvider=UnitTestDummyConfigProvider()
        self._ConfigProvider.addValue('Game.MovementDefinations','maximumAllowedPath','3')
        self._ConfigProvider.addValue('NoMovement.Config', 'PointDecTime', '3')
        self._ConfigProvider.addValue('NoMovement.Config', 'SafePointDecTime', '2')
        self._IsSafePoint=False

    def test_NoMovementController_OK_NotSafePoint(self):

        playerPosition=Point(2,2)
        nomovementcontroller=NoMovementController(self._ConfigProvider)
        result=nomovementcontroller.IStaticForTooLong(playerPosition,1, self._IsSafePoint)
        self.assertTrue(result==PlayerNoMovmentState.OK, "OK")

    def test_NoMovementController_OK_FOR_MOVEMENT_NotSafePoint(self):

        nomovementcontroller=NoMovementController(self._ConfigProvider)
        playerPosition = Point(2, 2)
        result=nomovementcontroller.IStaticForTooLong(playerPosition,2, self._IsSafePoint)
        self.assertTrue(result==PlayerNoMovmentState.OK, "OK")
        playerPosition = Point(2, 5)
        result = nomovementcontroller.IStaticForTooLong(playerPosition, 2, self._IsSafePoint)
        self.assertTrue(result == PlayerNoMovmentState.OK, "OK")
        playerPosition = Point(3, 2)
        result = nomovementcontroller.IStaticForTooLong(playerPosition, 2, self._IsSafePoint)
        self.assertTrue(result == PlayerNoMovmentState.OK, "OK")




    def test_NoMovementController_STATIC_TIMEOUT_NotSafePoint(self):

        playerPosition=Point(2,2)
        nomovementcontroller=NoMovementController(self._ConfigProvider)
        result=nomovementcontroller.IStaticForTooLong(playerPosition,7, self._IsSafePoint)
        self.assertTrue(result==PlayerNoMovmentState.STATIC_TIMEOUT, "OK")

    def test_NoMovementController_OK_SafePoint(self):
        playerPosition = Point(2, 2)
        self._IsSafePoint=True
        nomovementcontroller = NoMovementController(self._ConfigProvider)
        result = nomovementcontroller.IStaticForTooLong(playerPosition, 1, self._IsSafePoint)
        self.assertTrue(result == PlayerNoMovmentState.OK, "OK")

    def test_NoMovementController_OK_FOR_MOVEMENT_SafePoint(self):
        nomovementcontroller = NoMovementController(self._ConfigProvider)
        self._IsSafePoint = True

        playerPosition = Point(2, 2)
        result = nomovementcontroller.IStaticForTooLong(playerPosition, 1, self._IsSafePoint)
        self.assertTrue(result == PlayerNoMovmentState.OK, "OK")
        playerPosition = Point(2, 5)
        result = nomovementcontroller.IStaticForTooLong(playerPosition, 1, self._IsSafePoint)
        self.assertTrue(result == PlayerNoMovmentState.OK, "OK")
        playerPosition = Point(3, 2)
        result = nomovementcontroller.IStaticForTooLong(playerPosition,1, self._IsSafePoint)
        self.assertTrue(result == PlayerNoMovmentState.OK, "OK")

    def test_NoMovementController_STATIC_TIMEOUT_SafePoint(self):
        playerPosition = Point(2, 2)
        self._IsSafePoint = True

        nomovementcontroller = NoMovementController(self._ConfigProvider)
        result = nomovementcontroller.IStaticForTooLong(playerPosition, 3, self._IsSafePoint)
        self.assertTrue(result == PlayerNoMovmentState.STATIC_TIMEOUT, "OK")

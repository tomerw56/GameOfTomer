from unittest import TestCase
from Common.MovmentCommand import MovementCommand
from Common.Point import Point

class TestMovementCommand(TestCase):
    def test_IsEmpty_True(self):
        move=MovementCommand()
        self.assertTrue(move.IsEmpty)


    def test_IsEmpty_False_To(self):
        move = MovementCommand(pTo=Point(0,0))

        self.assertFalse(move.IsEmpty)

    def test_GetEmpty(self):
        move = MovementCommand.GetEmpty()
        self.assertTrue(move.IsEmpty)
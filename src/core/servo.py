from tkinter import IntVar
from src.core.communicator import Communicator


class Servo:
    def __init__(self, angle: IntVar, communicator: Communicator) -> None:
        # Current servo angle
        self.angle = angle

        # Communication between Application and Arduino
        self.communicator = communicator

    def set(self, value: int) -> None:
        """
        Set the servo to a specified angle.

        :param int value: Specified angle to set.
        """
        self.communicator.trigger(f'SET {value}\n')

    def set_min(self, value: int) -> None:
        """
        Set the servo's the minimum bound/angle.

        :param int value: Specified minimum bound.
        """
        self.communicator.trigger(f'SET MIN {value}\n')

    def set_max(self, value: int) -> None:
        """
        Set the servo's the maximum bound/angle.

        :param int value: Specified maximum bound.
        """
        self.communicator.trigger(f'SET MAX {value}\n')

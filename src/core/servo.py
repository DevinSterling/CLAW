from tkinter import IntVar
from src.core.connection import Connection


class Servo:
    def __init__(self, angle: IntVar, min: IntVar, max: IntVar, connection: Connection) -> None:
        # Current servo angle
        self.angle = angle
        self.min = min
        self.max = max
        # Connection between Application and Arduino
        self.connection = connection

    def auto(self):
        temp = self.angle.get()
        min = self.min.get()
        max = self.max.get()

        self.connection.call(f'AUTO:\n')
        self.angle.set(min if (temp - min) >= (max - temp) else max)

    def set(self, value: int) -> None:
        """
        Set the servo to a specified angle.

        :param int value: Specified angle to set.
        """
        self.connection.call(f'SET:{value}:\n')

    def set_min(self, value: int) -> None:
        """
        Set the servo's the minimum bound/angle.

        :param int value: Specified minimum bound.
        """
        self.connection.call(f'MIN:{value}:\n')

    def set_max(self, value: int) -> None:
        """
        Set the servo's the maximum bound/angle.

        :param int value: Specified maximum bound.
        """
        self.connection.call(f'MAX:{value}:\n')

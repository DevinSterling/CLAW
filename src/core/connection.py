import time
from serial import Serial
from threading import Thread
from typing import Callable


class Connection:
    def __init__(self, console_callback: Callable[[str], None], port: str, baudrate: int) -> None:
        self.console_callback = console_callback
        self.is_connected = False
        self.port = port
        self.baudrate = baudrate
        self.serial: Serial | None = None

        # Establish listener for serial output
        Thread(target=self.__listener, daemon=True).start()

    def __listener(self):
        while True:
            try:
                # If there is a connection
                if self.is_connected:
                    line = self.serial.readline()

                    # Ignore empty lines
                    if line != b'':
                        self.console_callback(line.decode().strip())
                # If there is no connection
                else:
                    self.console_callback(f'Disconnected - {self.info()}, Attempting Connection...')

                    # Attempt connection
                    if self.__connect():
                        self.console_callback(f'Connected - {self.info()}')
            except Exception as e:
                self.console_callback(f'An Exception Occurred: {e}')
                self.stop()
                # cooldown
                time.sleep(2)

    def __connect(self) -> bool:
        # Close the unresponsive port
        if self.serial is not None:
            self.serial.close()

        # Open new connection
        self.serial = Serial(self.port, self.baudrate, timeout=.1)
        self.is_connected = self.serial.is_open

        return self.is_connected

    def info(self) -> str:
        return f'{self.port}@{self.baudrate}'

    def call(self, data: str) -> None:
        if self.is_connected and self.serial is not None:
            self.serial.write(bytes(data, 'ascii'))

    def stop(self):
        self.is_connected = False
        if self.serial is not None:
            self.serial.close()

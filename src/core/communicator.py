import threading
import time
from typing import Callable
from src.core.connection import Connection


class Communicator:
    def __init__(self, callback: Callable[[str], None], connection: Connection) -> None:
        self.callback = callback
        self.connection = connection

        # Establish connection
        threading.Thread(target=self.__ping, daemon=True).start()

    def __ping(self):
        last_status = True

        # Should clean this a little
        while True:
            # Check if disconnected
            if not (status := self.ping()):
                # Prevent over-flooding the console
                if status != last_status:
                    self.callback(f'Disconnected - {self.connection.info()}, Connecting...')

                # Attempt to reconnect
                try:
                    if self.connection.connect():
                        self.callback(f'Connected - {self.connection.info()}')
                except Exception as e:
                    # Prevent over-flooding the console
                    if status != last_status:
                        self.callback(f'An exception occurred: {e}')
                finally:
                    last_status = status

            time.sleep(1)

    def trigger(self, command: str) -> None:
        """
        Trigger a request to Arduino for execution of the
        provided `command`.

        :param str command: Request for the arduino code
        to execute.
        """
        # TODO: Add logic to communicate with arduino here,
        # `callback` here is only used to show the output.
        if (response := self.connection.call(bytes(command, 'utf-8'))) is not None:
            self.callback(str(response, 'utf-8'))

    def ping(self) -> bool:
        """Ping Arduino to test the connection"""
        return self.connection.call(b'PING') is not None

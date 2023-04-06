from typing import Callable


class Communicator:
    def __init__(self, callback: Callable[[str], None]) -> None:
        self.callback = callback

    def trigger(self, command: str) -> None:
        """
        Trigger a request to Arduino for execution of the
        provided `command`.

        :param str command: Request for the arduino code
        to execute.
        """
        self.callback(command)

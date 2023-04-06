import serial


class Connection:
    def __init__(self, port: str, baudrate: int) -> None:
        self.is_connected = False
        self.port = port
        self.baudrate = baudrate
        self.serial: serial.Serial | None = None

    def info(self) -> str:
        return f'{self.port}@{self.baudrate}'

    def connect(self) -> bool:
        # Close the unresponsive port
        if self.serial is not None:
            self.serial.close()

        # Open new connection
        self.serial = serial.Serial(self.port, self.baudrate, timeout=.1)
        self.is_connected = self.serial.is_open

        return self.is_connected

    def call(self, data: bytes) -> bytes | None:
        if self.is_connected:
            return data

    def stop(self):
        if self.serial is not None:
            self.serial.close()

import tkinter as tk
from tkinter import ttk
from datetime import datetime
from src.core.servo import Servo
from src.core.connection import Connection
from src.ui.widget import Slider, Splitter
from src.ui.const import BANNER
from src.ui.style import panned_window_style, button_style, serial_text_style


class App(tk.Frame):
    """Simple Application logic container"""
    def __init__(self, port: str, baud_rate: int, master: tk.Misc = None) -> None:
        super().__init__(master)

        # Observable variables
        self.min_bound: tk.IntVar = tk.IntVar(value=0)
        self.max_bound: tk.IntVar = tk.IntVar(value=180)
        self.servo_control: tk.IntVar = tk.IntVar(value=0)

        # Widgets
        self.min_bound_slider: Slider
        self.max_bound_slider: Slider
        self.servo_control_slider: Slider
        self.servo_auto_button: tk.Button
        self.serial_output: tk.Text

        # build the user interface
        self.__build()
        self.__bind()

        # Core components
        self.servo = Servo(
            self.servo_control,
            self.min_bound,
            self.max_bound,
            Connection(self.serial_in, port, baud_rate),
        )

    def __build(self) -> None:
        """Construct the user interface."""
        pane = tk.PanedWindow(self, **panned_window_style)
        pane.pack(fill=tk.BOTH, expand=True)
        pane.add(self.__build_controls())
        pane.add(self.__build_serial_out())

        self.pack(fill=tk.BOTH, expand=True)

    def __build_controls(self) -> ttk.Frame:
        """
        Construct the servo controls.

        :returns: Frame containing the servo controls.
        """
        frame = ttk.Frame(self, style='TFrame')
        frame.pack(fill=tk.BOTH, expand=True)

        # Frame label
        header = ttk.Frame(frame)
        header.pack(fill=tk.X)

        ttk.Label(header, text='Controls', style='Heading.TLabel').pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Button to trigger opening/retraction of the servo
        self.servo_auto_button = tk.Button(header, text='⭍', **button_style)
        self.servo_auto_button.pack(side=tk.LEFT, fill=tk.X)

        # Container to encompass slider controls
        container = ttk.Frame(frame, padding=(15, 15, 15, 0))
        container.pack(fill=tk.BOTH, expand=True)

        # Maximum bound for slider control
        self.min_bound_slider = Slider(container, label='Minimum Bound', variable=self.min_bound, to=self.max_bound)
        self.min_bound_slider.pack(fill=tk.X)
        Splitter(container).pack(fill=tk.X)

        # Minimum bound for slider control
        self.max_bound_slider = Slider(container, label='Maximum Bound', variable=self.max_bound, from_=self.min_bound)
        self.max_bound_slider.pack(fill=tk.X)
        Splitter(container).pack(fill=tk.X)

        # Manual servo control
        self.servo_control_slider = Slider(
            container,
            label='Servo Control',
            variable=self.servo_control,
            from_=self.min_bound,
            to=self.max_bound,
        )
        self.servo_control_slider.pack(fill=tk.X)

        return frame

    def __build_serial_out(self) -> ttk.Frame:
        """
        Construct the in-application console.

        :returns: Frame containing the console.
        """
        frame = ttk.Frame(self, style='Serial.TFrame')
        frame.pack()

        # Frame label
        self.serial_output = tk.Text(frame, **serial_text_style)
        self.serial_output.pack(fill=tk.BOTH, expand=True)
        self.serial_output.insert(tk.END, BANNER)
        self.serial_in('** Arduino Serial Output **\n')

        return frame

    def __bind(self) -> None:
        """Setup listeners and associated actions."""
        self.min_bound_slider.scale.bind('<ButtonRelease-1>', lambda _: self.servo.set_min(self.min_bound.get()))
        self.max_bound_slider.scale.bind('<ButtonRelease-1>', lambda _: self.servo.set_max(self.max_bound.get()))
        self.servo_control.trace_add('write', lambda *_: self.servo.set(self.servo_control.get()))
        self.servo_auto_button.bind('<ButtonRelease-1>', lambda _: self.servo.auto())
        self.master.protocol('WM_DELETE_WINDOW', self.__stop)

    def __stop(self) -> None:
        self.servo.connection.close()
        self.master.destroy()

    def serial_in(self, message: str) -> None:
        """
        Shows the provided `message` in the application console
        paired with the current timestamp.

        :param str message: Message to show in console
        """
        # Add newline if necessary
        newline = '\n' if not message.endswith('\n') else ''
        # Get timestamp
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        self.serial_output.config(state=tk.NORMAL)
        self.serial_output.insert(tk.END, f'[{time}]\t{message}{newline}')
        self.serial_output.config(state=tk.DISABLED)
        self.serial_output.see(tk.END)

import tkinter as tk
from tkinter import ttk
from src.ui.widget import Slider, Splitter
from src.ui.style import panned_window_style, button_style, serial_text_style


class App(tk.Frame):
    def __init__(self, master: tk.Misc = None) -> None:
        super().__init__(master)

        # Observable variables
        self.min_bound: tk.IntVar = tk.IntVar(value=0)
        self.max_bound: tk.IntVar = tk.IntVar(value=180)
        self.servo_control: tk.IntVar = tk.IntVar(value=0)

        # Widgets
        self.min_bound_slider: Slider
        self.max_bound_slider: Slider
        self.servo_control_slider: Slider
        self.serial_output: tk.Text

        # build the user interface
        self.__build()

    def __build(self) -> None:
        """
        Build the user interface
        :return: None
        """
        pane = tk.PanedWindow(self, **panned_window_style)
        pane.pack(fill=tk.BOTH, expand=True)
        pane.add(self.__build_controls())
        pane.add(self.__build_serial_out())

        self.pack(fill=tk.BOTH, expand=True)

    def __build_controls(self) -> ttk.Frame:
        frame = ttk.Frame(self, style='TFrame')
        frame.pack(fill=tk.BOTH, expand=True)

        # Frame label
        header = ttk.Frame(frame)
        header.pack(fill=tk.X)

        ttk.Label(header, text='Controls', style='Heading.TLabel').pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Button to trigger opening/retraction of the servo
        action_button = tk.Button(header, text='⭍', **button_style)
        action_button.pack(side=tk.LEFT, fill=tk.X)

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
        frame = ttk.Frame(self, style='Serial.TFrame')
        frame.pack()

        # Frame label
        self.serial_output = tk.Text(frame, **serial_text_style)
        self.serial_output.pack(fill=tk.BOTH, expand=True)
        self.serial_in('** Arduino Serial Output **\n')

        return frame

    def serial_in(self, message: str) -> None:
        self.serial_output.config(state=tk.NORMAL)
        self.serial_output.insert(tk.END, message)
        self.serial_output.config(state=tk.DISABLED)

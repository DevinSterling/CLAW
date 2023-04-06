import tkinter as tk
from tkinter import ttk
from src.ui.style import slider_style, splitter_style


class Slider(ttk.Frame):
    def __init__(
            self,
            master: tk.Misc = None,
            variable: tk.IntVar = tk.IntVar(value=0),
            from_: tk.IntVar = tk.IntVar(value=0),
            to: tk.IntVar = tk.IntVar(value=180),
            label: str = 'Slider',
    ) -> None:
        super().__init__(master, style='Slider.TFrame')

        # Observable variables
        self.variable: tk.IntVar = variable
        self.from_: tk.IntVar = from_
        self.to: tk.IntVar = to

        # Labels
        self.heading: ttk.Label = ttk.Label(self, text=label, style='Heading2.TLabel')
        self.min_label: ttk.Label = ttk.Label(self, textvariable=self.from_, padding=(0, 0, 8, 0))
        self.max_label: ttk.Label = ttk.Label(self, textvariable=self.to, padding=(8, 0, 0, 0))

        # Scale
        self.scale: tk.Scale = tk.Scale(
            self,
            variable=self.variable,
            from_=self.from_.get(),
            to=self.to.get(),
            command=self.__update_variable,
            **slider_style,
        )

        # Build and bind
        self.__build()
        self.__bind()

    def __build(self) -> None:
        """Construct the layout of the slider"""
        self.heading.pack(side='top', anchor='w')
        self.min_label.pack(side='left', anchor='s')
        self.scale.pack(side='left', fill=tk.X, expand=True)
        self.max_label.pack(side='left', anchor='s')

    def __bind(self) -> None:
        """Setup listeners and associated actions."""
        self.from_.trace_add('write', self.__update_min_bound)
        self.to.trace_add('write', self.__update_max_bound)

    def __update_variable(self, value: str) -> None:
        """
        Update the slider `variable`.

        :param str value: Value to set the slider `variable` to.
        """
        self.variable.set(int(value))

    def __update_min_bound(self, *_args) -> None:
        """Update slider minimum bound."""
        self.scale.config(from_=self.from_.get())

    def __update_max_bound(self, *_args) -> None:
        """Update slider maximum bound."""
        self.scale.config(to=self.to.get())


class Splitter(ttk.Frame):
    def __init__(self, master: tk.Misc = None) -> None:
        super().__init__(master)

        self.canvas = tk.Canvas(self, **splitter_style)
        self.canvas.create_line(0, 20, 999, 20, fill='#333', width=1)
        self.canvas.pack(fill=tk.X)

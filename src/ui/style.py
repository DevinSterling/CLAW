# UI Styles

import tkinter as tk
from tkinter import ttk
from src.ui.const import *

# Traditional styling
panned_window_style = {
    'orient': tk.HORIZONTAL,
    'borderwidth': 0,
    'background': '#191919',
    'sashwidth': 5,
}
serial_text_style = {
    'font': (PRIMARY_FONT, '12'),
    'wrap': tk.WORD,
    'background': '#000',
    'foreground': PRIMARY_FG,
    'border': 0,
    'padx': 10,
    'pady': 10,
    'insertbackground': PRIMARY_FG,
}
button_style = {
    'font': (PRIMARY_FONT, '14'),
    'background': PRIMARY_BG,
    'foreground': PRIMARY_FG,
    'activebackground': SECONDARY_BG,
    'activeforeground': PRIMARY_FG,
    'relief': tk.FLAT,
    'pady': 9,
    'padx': 13,
    'border': 0,
    'highlightthickness': 0,
}
slider_style = {
    'orient': tk.HORIZONTAL,
    'background': SECONDARY_BG,
    'foreground': 'white',
    'font': (PRIMARY_FONT, '11'),
    'sliderrelief': tk.FLAT,
    'troughcolor': '#777',
    'borderwidth': 0,
    'highlightthickness': 0,
    'width': 18,
}
splitter_style = {
    'background': SECONDARY_BG,
    'highlightthickness': 0,
    'height': 35,
}

# ttk styling
s = ttk.Style()
s.configure(
    'TFrame',
    background=SECONDARY_BG,
)
s.configure(
    'Serial.TFrame',
    background='#000',
)
s.configure(
    'TLabel',
    font=(PRIMARY_FONT, '11'),
    background=SECONDARY_BG,
    foreground=PRIMARY_FG,
)
s.configure(
    'Heading.TLabel',
    font=(PRIMARY_FONT, '14'),
    foreground='#ccc',
    background=PRIMARY_BG,
    padding=(13, 13, 0, 10)
)
s.configure(
    'Heading2.TLabel',
    font=(PRIMARY_FONT, '12'),
    foreground=PRIMARY_FG,
    background=SECONDARY_BG,
    padding=(0, 0, 0, 4)
)

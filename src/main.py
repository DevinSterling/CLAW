from src.app import App

app = App(port='COM3', baud_rate=9600)
app.master.title('CLAW')
app.master.geometry('800x400')
app.mainloop()

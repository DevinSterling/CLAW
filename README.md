# CLAW

Simple Tkinter application to control a servo through serial communication.

## User Interface
![CLAW user interface](/img/ui.png)
> In-application console showcases automated reconnection when the 
USB is temporarily disconnected.

## Features
- Real-time connection status through in-application console:
  - Check connectivity
  - View angle status
  - Provides servo control history (timestamped)
- Automated reconnect on disconnect
- Precise manual servo control (3 sliders):
  - Maximum bound
  - Minimum bound
  - Servo Angle
- Button to open/close servo (constrained by min/max bound set).
- Offers multiple views (split pane view):
  - Servo controls view
  - Serial output console view
  - Both controls and output view (side by side)

## Future Improvements
- Ability to change port/baud rate during runtime
  - Currently has to be set before application is launched
- More themes
  - Currently only dark theme

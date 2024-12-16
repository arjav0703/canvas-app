# Canvas

## This is Inspired by various other HighSeas projects.

## Overview
This is a simple drawing application built using Python's `Tkinter` library. It allows users to draw on a canvas with various tools such as pencil, line, rectangle, and eraser. The application also supports color selection and clearing the canvas.

## Features
- **Drawing Tools**: Pencil, Line, Rectangle, and Eraser.
- **Color Selection**: Choose any color to draw.
- **Canvas Clearing**: Clear the entire canvas to start fresh.
- **Eraser Mode**: Toggle eraser mode to erase drawn lines or shapes.

## Requirements
- Python 3.x
- Tkinter library (usually comes with Python installation)

## Installation

1. Make sure you have Python 3.x installed. If not, download and install it from [Python.org](https://www.python.org/downloads/).
2. Tkinter is included with most Python installations. If you need to install Tkinter, you can use the following command (on Linux):
   ```bash
   sudo apt-get install python3-tk
   ```

## Usage

1. Clone or download the Python script from this repository.
2. Run the script using Python:
   ```bash
   python main.py
   ```

### Methods
- **`__init__(self, root)`**: Initializes the application with the main window, canvas, and toolbar.
- **`setup_toolbar(self)`**: Sets up the toolbar with buttons for tool selection.
- **`start_draw(self, event)`**: Starts drawing when the mouse button is pressed.
- **`draw(self, event)`**: Draws based on the selected tool and mouse movements.
- **`stop_draw(self, event)`**: Stops drawing after the mouse button is released.
- **`select_color(self)`**: Opens a color chooser dialog to select a drawing color.
- **`toggle_eraser(self)`**: Switches to eraser mode and changes pen size.
- **`clear_canvas(self)`**: Clears the entire drawing canvas.
- **`set_tool(self, tool)`**: Switches between drawing tools.
- **`display_eraser(self, x, y)`**: Shows the eraser's current position on the canvas.

## Customization
- **Pen Size**: You can adjust the pen size by modifying the `self.pen_size` variable.
- **Canvas Size**: Modify the `width` and `height` attributes in `self.canvas` for a different-sized canvas.
- **Toolbar Styling**: You can customize the look of buttons by modifying the `style.configure` settings.


## Troubleshooting
- **Application not running?**
  - Make sure you have Python installed and Tkinter is available.
  - Ensure you are running the script in an environment that supports GUI applications.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
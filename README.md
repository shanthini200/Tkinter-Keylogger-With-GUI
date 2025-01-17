

# Keylogger with Tkinter GUI

This Python-based keylogger captures keystrokes and displays them in a Tkinter window. It logs each keystroke with a timestamp, stores them in a `log.txt` file, and features a button to stop the keylogger. The application provides a simple, real-time interface for monitoring keystrokes.

## Features

- Captures keystrokes in real-time.
- Displays the captured keystrokes in a Tkinter window.
- Logs each keystroke with a timestamp in a `log.txt` file.
- Includes a **Stop Keylogger** button to halt the keystroke capture.
- Ignores special keys like Shift and Ctrl.

## Requirements

- Python 3.x
- `pynput` library (to capture keyboard events)
- `tkinter` (for the GUI)

## Installation

1. Clone the repository or download the code.

    ```bash
    git clone <repository-url>
    ```

2. Install the required dependencies:

    ```bash
    pip install pynput
    ```

3. Run the Python script:

    ```bash
    python app_window.py
    ```

4. A GUI window will appear, showing captured keystrokes. Press **Stop Keylogger** to stop logging.

## Code Explanation

- **pynput.keyboard.Listener**: Captures key events and calls the `write_to_file` function to log the keystrokes.
- **Tkinter GUI**: Displays the keystrokes in a text box, and allows users to start and stop the keylogger via a button.
- **Timestamp**: Each keystroke is logged with a timestamp in the format `YYYY-MM-DD HH:MM:SS`.

## Stop Keylogger Function

- The **Stop Keylogger** button invokes the `stop_keylogger` function, which stops the listener thread and halts the keystroke capture.

## License

This project is licensed under the Apache License 2.0 - see the(LICENSE) file for details.

## Disclaimer

This keylogger is for educational purposes only. Misuse of this software could violate privacy laws. Please use responsibly and with permission.




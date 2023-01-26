import time
from plyer import notification
import tkinter as tk
from tkinter import PhotoImage


def start_notifications():
    global running
    running = True
    while running:
        notification.notify(
            title="ALERT!!!",
            message="Take a break! It has been an hour!",
            timeout=10
        )
        time.sleep(3600)


def stop_notifications():
    global running
    running = False


if __name__ == "__main__":
    global running
    running = False

    root = tk.Tk()
    root.title("Notification App")
    root.geometry("400x200")
    root.config(bg="white")
    img = PhotoImage(file='path/to/icon.png')
    root.tk.call('wm', 'iconphoto', root._w, img)
    start_button = tk.Button(root, text="Start", command=start_notifications,
                             bg="green", fg="white", font=("Helvetica", 16))
    stop_button = tk.Button(root, text="Stop", command=stop_notifications,
                            bg="red", fg="white", font=("Helvetica", 16))

    start_button.pack(padx=20, pady=20)
    stop_button.pack(padx=20, pady=20)

    root.mainloop()

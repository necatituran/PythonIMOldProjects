import time
from plyer import notification
import tkinter as tk


def start_notifications():
    global running
    running = True
    while running:
        notification.notify(
            title="FULL FOCUS",
            message="You can do it NECO THINK YOUR DREAMS",
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
root.title("FOCUS!")

start_button = tk.Button(root, text="Start", command=start_notifications)
stop_button = tk.Button(root, text="Stop", command=stop_notifications)

start_button.pack()
stop_button.pack()

root.mainloop()

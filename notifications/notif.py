import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="FULL FOCUS",
            message="NECO YOU CAN DO IT, THINK YOUR DREAMS",
            timeout=3600
        )
        time.sleep(3600)

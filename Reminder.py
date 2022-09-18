# Notification Reminder Program

import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please Drink Water",
            message = "Dont get Dehytrated...Please drink water first, then continue your work :)",
            app_icon = "D:\CODING\icon.ico",
            timeout = 10
        )
        time.sleep(60*60)

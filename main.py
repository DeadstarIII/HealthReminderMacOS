import tkinter as tk
import subprocess
import schedule
import time
import threading

class ReminderApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Health Reminder App")

        self.create_widgets()
        self.start_reminders()

    def create_widgets(self):
        instructions_label = tk.Label(self.root, text="Stay Healthy! Follow the reminders:")
        instructions_label.pack(pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def play_alarm_threaded(self):
        threading.Thread(target=self.play_alarm).start()

    def show_notification(self, message):
        print(f"Showing notification: {message}")
        subprocess.run(['osascript', '-e', f'display notification "{message}" with title "Health Reminder"'])
        # self.play_alarm_threaded()

    def walk_around(self):
        self.show_notification("It's time to go up and walk around the house!")

    def look_away(self):
        self.show_notification("Look at an object 20-30 feet away from your eyes!")

    def drink_water(self):
        self.show_notification("Stay hydrated! Time to drink water.")

    def on_closing(self):
        self.root.destroy()

    def start_reminders(self):
        schedule.every(30).minutes.do(self.walk_around)  
        schedule.every(20).minutes.do(self.look_away)
        schedule.every(30).minutes.do(self.drink_water)

        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    app = ReminderApp()
    app.root.mainloop()

import rumps
import threading
import subprocess
import schedule
import time

class ReminderApp(rumps.App):
    def __init__(self):
        super(ReminderApp, self).__init__("Health Reminder", icon="./assets/icon.png")
        self.menu = ["Walk Around", "Look Away", "Drink Water", None]
        self.schedule_thread = threading.Thread(target=self.schedule_loop)
        self.schedule_thread.daemon = True 
        self.schedule_thread.start()

    def show_notification(self, message):
        subprocess.run(['osascript', '-e', f'display notification "{message}" with title "Health Reminder"'])

    #def play_alarm(self):
    #    subprocess.run(['afplay', './assets/iPhone.mp3'])

    def schedule_reminders(self):
        schedule.every(40).minutes.do(self.walk_around)
        schedule.every(30).minutes.do(self.drink_water)
        schedule.every(20).minutes.do(self.look_away)

    def schedule_loop(self):
        while True:
            schedule.run_pending()
            time.sleep(1)  # Sleep for a short interval to avoid consuming too much CPU

    @rumps.clicked("Walk Around")
    def walk_around(self, *_):
        self.show_notification("It's time to go up and walk around the house!")

    @rumps.clicked("Look Away")
    def look_away(self, *_):
        self.show_notification("Look at an object 20-30 feet away from your eyes!")

    @rumps.clicked("Drink Water")
    def drink_water(self, *_):
        self.show_notification("Stay hydrated! Time to drink water.")

if __name__ == "__main__":
    app = ReminderApp()
    app.schedule_reminders()  
    app.run()

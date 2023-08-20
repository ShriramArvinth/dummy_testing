import schedule
import time
import main as capture_and_upload from take_photo_upload_delete_photo
import RPi.GPIO as GPIO
import requests

# List of times to schedule the function
times_to_schedule = ["08:00", "12:30", "17:15"]

# Schedule the function for each time in the list
for time_str in times_to_schedule:
    schedule.every().day.at(time_str).do(capture_and_upload)

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    schedule.run_pending()
    time.sleep(1)
    pin_state = GPIO.input(pin_to_monitor)
    if pin_state:
        x = requests.get("https://agriculture-monitoring-system.glitch.me/ping")
        time.sleep(5)
        
GPIO.cleanup()

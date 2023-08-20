import schedule
import time
import main as capture_and_upload from take_photo_upload_delete_photo

# List of times to schedule the function
times_to_schedule = ["08:00", "12:30", "17:15"]

# Schedule the function for each time in the list
for time_str in times_to_schedule:
    schedule.every().day.at(time_str).do(capture_and_upload)

while True:
    schedule.run_pending()
    time.sleep(1)

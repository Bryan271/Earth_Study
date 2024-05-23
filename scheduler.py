# scheduler.py
'''
The scheduler runs in 5 minute increments before starting a new iteration loop. 
This is to take a screenshot of each image every 60 seconds for a total of 5 seperate views.
The views I have chosen update every 5 minutes. 
You may need to adjust thes settings for different time structures if you like.
'''
import time
from selenium_module import SeleniumHandler

def start_cycle(handler):
    handler.continue_screenshot()

if __name__ == "__main__":
    # Initialize the SeleniumHandler
    handler = SeleniumHandler(None)  # Assuming you don't have a root GUI object

    while True:
        print("Starting a new cycle...")
        cycle_start_time = time.time()
        start_cycle(handler)
        elapsed_time = time.time() - cycle_start_time
        sleep_time = max(0, 300 - elapsed_time)  # Ensure the cycle lasts exactly 300 seconds
        time.sleep(sleep_time)

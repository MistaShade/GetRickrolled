import webbrowser
import time
import random

while True:
    sites = random.choice(['https://youtu.be/dQw4w9WgXcQ'])
    visit = "http://youtu.be/dQw4w9gXcQ"
    webbrowser.open(visit)
    seconds = random.randrange(5, 20)
    time.sleep(seconds)
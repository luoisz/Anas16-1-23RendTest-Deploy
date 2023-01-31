import time
import urllib.request
while True:
  URL = "https://www.example.com"
  Wait_Time = 10
  print("Pinging...")
  time.sleep(Wait_Time)
  ping = urllib.request.urlopen(URL)
  status = str(ping.status)
  print(f"Cron-Job is working with status ({status})")

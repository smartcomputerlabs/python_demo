from pygooglenews import GoogleNews
import json
import time

gn = GoogleNews()
top = gn.top_news()

entries = top["entries"]
count = 0
for entry in entries:
  count = count + 1
  print(
    str(count) + ". " + entry["title"] + entry["published"]
  )
  time.sleep(0.25)
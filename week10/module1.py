# Using the requests and time modules, create a function which returns the amount of time it takes a webpage to load
# (how long it takes for a complete response to a request).
# Test your code with multiple sites such as google, ynet, imdb, etc.

import time
import requests

def request_time(link):
    t1 = time.time()
    r = requests.get(link)
    t2 = time.time() - t1
    return time.time() - t1


print(f" google request time {request_time('https://www.google.fr')}")
print(f" yahoo request time {request_time('https://www.yahoo.com')}")
print(f" walla request time {request_time('https://www.walla.co.il')}")

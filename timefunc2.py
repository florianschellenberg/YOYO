import time
from threading import Timer
def print_time():
    print("From print_time", time.time())

def print_some_times():
    print(time.time())
    Timer(2, print_time, ()).start()
    Timer(5, print_time, ()).start()
    time.sleep(11)  # sleep while time-delay events execute
    print(time.time())

print_some_times()

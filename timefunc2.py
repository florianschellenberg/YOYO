# import time
# from threading import Timer
# def print_time():
#     print("From print_time", time.time())

# def print_some_times():
#     print(time.time())
#     Timer(2, print_time, ()).start()
#     Timer(5, print_time, ()).start()
#     time.sleep(11)  # sleep while time-delay events execute
#     print(time.time())

# print_some_times()

import sched, time
s = sched.scheduler(time.time, time.sleep)
def print_time(a='default'):
    print("From print_time", time.time(), a)

def print_some_times():
    print(time.time())
    s.enter(10, 1, print_time)
    s.enter(5, 2, print_time, argument=('positional',))
    s.enter(5, 1, print_time, kwargs={'a': 'keyword'})
    s.run()
    print(time.time())

print_some_times()
import sched, time, winsound



s = sched.scheduler(time.time, time.sleep)
def print_time(): 
    print("From print_time", time.time())
    winsound.PlaySound('2.wav', winsound.SND_FILENAME)


def print_some_times():
     print(time.time())
     s.enter(2, 1, print_time, ())
     s.enter(4, 1, print_time, ())
     time.sleep(11)  # sleep while time-delay events execute
     s.run()

     print(time.time())

print_some_times()

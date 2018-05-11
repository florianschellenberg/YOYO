import time, winsound
from threading import Timer

# winsound.PlaySound('2.wav', winsound.SND_FILENAME)
# print("something")
# time.sleep(5.5)    # pause 5.5 seconds
# winsound.PlaySound('2.wav', winsound.SND_FILENAME)
# print("something")

def to_play_sound(hour, min):
    now = datetime.now()
    currentHour = now.hour
    currentMin = now.minute
    if currentHour == hour and currentMin == min and not is_played:
        is_played = True
        os.system("2.wav")
    if currentHour != myHour or currentMin != myMin:
        is_played = False
while True:
    t = Timer(30.0, to_play_sound, [20, 13])
    t.start()
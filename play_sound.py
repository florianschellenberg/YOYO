import winsound

# winsound.PlaySound('2.wav', winsound.SND_FILENAME)
import winsound
duration = 1000  # millisecond
freq = 440  # Hz
winsound.Beep(freq, duration)
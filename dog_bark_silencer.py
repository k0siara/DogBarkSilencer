from playsound import playsound
import RPi.GPIO as GPIO
import time
import random

sounds = [
    "sound1.mp3",
    "sound2.mp3",
    "sound3.mp3",
    "sound4.mp3",
    "sound5.mp3"
]

channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
    if GPIO.input(channel):
        on_bark_detected()

def on_bark_detected():
    global sounds
    random_sound = random.choice(sounds)
    playsound(random_sound)

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)

while True:
    time.sleep(1)

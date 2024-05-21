import os
import vlc
import time
import gpio as GPIO
from pydub import AudioSegment
import sys
sys.path.insert(0, '/home/rock/Desktop/Hearsight/')
from config import *
from play_audio import GTTSA

play_audio = GTTSA()
GPIO.setup(448, GPIO.IN)  # Exit Button

def announce_waiting():
    play_audio.play_audio_file("waiting_for_your_command.mp3")
    print("Waiting for your command")

if __name__ == "__main__":
    start_time = time.time()
    while True:
        input_state = GPIO.input(448)  # Move this inside the loop to continuously read the button state
        
        if input_state == True:
            play_audio.play_machine_audio("/home/rock/Desktop/Hearsight/audios/beeb/340Hz-5sec.wav")
            sys.exit()
            break
        
        elapsed_time = time.time() - start_time
        if elapsed_time >= 150:  # Check if 2.5 minutes have elapsed 150
            announce_waiting()
            start_time = time.time()  # Reset start time for the next iteration
            
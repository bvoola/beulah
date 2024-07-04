import random
import time
from gtts import gTTS
import pygame
import os

# List of Hindi alphabets
hindi_alphabets = [
    "अ", "आ", "इ", "ई", "उ", "ऊ", "ऋ", "ए", "ऐ", "ओ", "औ", 
    "क", "ख", "ग", "घ", "ङ", "च", "छ", "ज", "झ", "ञ", 
    "ट", "ठ", "ड", "ढ", "ण", "त", "थ", "द", "ध", "न", 
    "प", "फ", "ब", "भ", "म", "य", "र", "ल", "व", 
    "श", "ष", "स", "ह", "क्ष", "त्र", "ज्ञ"
]

def play_hindi_alphabet_sound(alphabet):
    # Create a gTTS object
    tts = gTTS(text=alphabet, lang='hi')
    # Save the audio file
    tts.save("alphabet.mp3")
    # Initialize pygame mixer
    pygame.mixer.init()
    # Load and play the audio file
    pygame.mixer.music.load("alphabet.mp3")
    pygame.mixer.music.play()
    # Wait until the sound has finished playing
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    # Clean up by quitting pygame mixer and removing the file
    pygame.mixer.quit()
    os.remove("alphabet.mp3")

def main():
    while True:
        # Shuffle the list of Hindi alphabets to ensure random order
        random.shuffle(hindi_alphabets)
        for alphabet in hindi_alphabets:
            print(f"Write the following Hindi alphabet: {alphabet}")
            
            for _ in range(3):  # 100 repetitions, each with a 3-second interval, totals 5 minutes
                # Play the sound of the selected alphabet
                play_hindi_alphabet_sound(alphabet)
                # Wait for 3 seconds
                time.sleep(2)
            print("Moving to the next letter...")

if __name__ == "__main__":
    main()

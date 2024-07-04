import random
import time
from gtts import gTTS
import pygame

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

def main():
    while True:
        # Select a random Hindi alphabet
        alphabet = random.choice(hindi_alphabets)
        print(f"Write the following Hindi alphabet: {alphabet}")
        
        for _ in range(100):  # 100 repetitions, each with a 3-second interval, totals 5 minutes
            # Play the sound of the selected alphabet
            play_hindi_alphabet_sound(alphabet)
            # Wait for 3 seconds
            time.sleep(3)
        print("Moving to the next letter...")
        # os.remove("alphabet.mp3")

if __name__ == "__main__":
    main()

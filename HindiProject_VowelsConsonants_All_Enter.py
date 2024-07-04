import random
import time
from gtts import gTTS
import pygame
import os

# List of Hindi alphabets and their Barakhadi (vowel-consonant combinations)
hindi_alphabets = [
    "अ", "आ", "इ", "ई", "उ", "ऊ", "ऋ", "ए", "ऐ", "ओ", "औ", 
    "क", "का", "कि", "की", "कु", "कू", "कृ", "के", "कै", "को", "कौ", 
    "ख", "खा", "खि", "खी", "खु", "खू", "खृ", "खे", "खै", "खो", "खौ", 
    "ग", "गा", "गि", "गी", "गु", "गू", "गृ", "गे", "गै", "गो", "गौ", 
    "घ", "घा", "घि", "घी", "घु", "घू", "घृ", "घे", "घै", "घो", "घौ", 
    "ङ", "ङा", "ङि", "ङी", "ङु", "ङू", "ङृ", "ङे", "ङै", "ङो", "ङौ", 
    "च", "चा", "चि", "ची", "चु", "चू", "चृ", "चे", "चै", "चो", "चौ", 
    "छ", "छा", "छि", "छी", "छु", "छू", "छृ", "छे", "छै", "छो", "छौ", 
    "ज", "जा", "जि", "जी", "जु", "जू", "जृ", "जे", "जै", "जो", "जौ", 
    "झ", "झा", "झि", "झी", "झु", "झू", "झृ", "झे", "झै", "झो", "झौ", 
    "ञ", "ञा", "ञि", "ञी", "ञु", "ञू", "ञृ", "ञे", "ञै", "ञो", "ञौ", 
    "ट", "टा", "टि", "टी", "टु", "टू", "टृ", "टे", "टै", "टो", "टौ", 
    "ठ", "ठा", "ठि", "ठी", "ठु", "ठू", "ठृ", "ठे", "ठै", "ठो", "ठौ", 
    "ड", "डा", "डि", "डी", "डु", "डू", "डृ", "डे", "डै", "डो", "डौ", 
    "ढ", "ढा", "ढि", "ढी", "ढु", "ढू", "ढृ", "ढे", "ढै", "ढो", "ढौ", 
    "ण", "णा", "णि", "णी", "णु", "णू", "णृ", "णे", "णै", "णो", "णौ", 
    "त", "ता", "ति", "ती", "तु", "तू", "तृ", "ते", "तै", "तो", "तौ", 
    "थ", "था", "थि", "थी", "थु", "थू", "थृ", "थे", "थै", "थो", "थौ", 
    "द", "दा", "दि", "दी", "दु", "दू", "दृ", "दे", "दै", "दो", "दौ", 
    "ध", "धा", "धि", "धी", "धु", "धू", "धृ", "धे", "धै", "धो", "धौ", 
    "न", "ना", "नि", "नी", "नु", "नू", "नृ", "ने", "नै", "नो", "नौ", 
    "प", "पा", "पि", "पी", "पु", "पू", "पृ", "पे", "पै", "पो", "पौ", 
    "फ", "फा", "फि", "फी", "फु", "फू", "फृ", "फे", "फै", "फो", "फौ", 
    "ब", "बा", "बि", "बी", "बु", "बू", "बृ", "बे", "बै", "बो", "बौ", 
    "भ", "भा", "भि", "भी", "भु", "भू", "भृ", "भे", "भै", "भो", "भौ", 
    "म", "मा", "मि", "मी", "मु", "मू", "मृ", "मे", "मै", "मो", "मौ", 
    "य", "या", "यि", "यी", "यु", "यू", "यृ", "ये", "यै", "यो", "यौ", 
    "र", "रा", "रि", "री", "रु", "रू", "ृ", "रे", "रै", "रो", "रौ", 
    "ल", "ला", "लि", "ली", "लु", "लू", "लृ", "ले", "लै", "लो", "लौ", 
    "व", "वा", "वि", "वी", "वु", "वू", "वृ", "वे", "वै", "वो", "वौ", 
    "श", "शा", "शि", "शी", "शु", "शू", "शृ", "शे", "शै", "शो", "शौ", 
    "ष", "षा", "षि", "षी", "षु", "षू", "षृ", "षे", "षै", "षो", "षौ", 
    "स", "सा", "सि", "सी", "सु", "सू", "सृ", "से", "सै", "सो", "सौ", 
    "ह", "हा", "हि", "ही", "हु", "हू", "हृ", "हे", "है", "हो", "हौ", 
    "क्ष", "क्षा", "क्षि", "क्षी", "क्षु", "क्षू", "क्षृ", "क्षे", "क्षै", "क्षो", "क्षौ", 
    "त्र", "त्रा", "त्रि", "त्री", "त्रु", "त्रू", "त्रृ", "त्रे", "त्रै", "त्रो", "त्रौ", 
    "ज्ञ", "ज्ञा", "ज्ञि", "ज्ञी", "ज्ञु", "ज्ञू", "ज्ञृ", "ज्ञे", "ज्ञै", "ज्ञो", "ज्ञौ"
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
                time.sleep(3)
            print("Press Enter to proceed to the next letter...")
            input()  # Wait for the user to press Enter before proceeding

if __name__ == "__main__":
    main()

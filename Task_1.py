import pyttsx3

def list_voices(engine):
    """Lists available voices for the user to choose."""
    voices = engine.getProperty('voices')
    print("\nAvailable Voices:")
    for index, voice in enumerate(voices):
        print(f"{index}: {voice.name} ({voice.languages})")
    print()

def text_to_speech(text, voice_index=0, rate=175):
    """Converts text to speech using specified voice and rate."""
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    try:
        engine.setProperty('voice', voices[voice_index].id)
    except IndexError:
        print("Invalid voice index. Using default voice.")
    engine.setProperty('rate', rate)
    print("\nSpeaking...")
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    engine = pyttsx3.init()

    # List and choose voice
    list_voices(engine)
    while True:
        voice_input = input("Select a voice by index (or press Enter for default): ").strip()
        if voice_input == "":
            voice_index = 0
            print("Using default voice.\n")
            break
        elif voice_input.isdigit() and int(voice_input) < len(engine.getProperty('voices')):
            voice_index = int(voice_input)
            print(f"Selected voice {voice_index}.\n")
            break
        else:
            print("Invalid input. Please enter a valid voice index.\n")

    # Choose speech rate
    while True:
        rate_input = input("Enter speech rate (default is 175, like Siri): ").strip()
        if rate_input == "":
            rate = 175
            print("Using default speech rate of 175.\n")
            break
        elif rate_input.isdigit():
            rate = int(rate_input)
            print(f"Using speech rate: {rate}.\n")
            break
        else:
            print("Invalid input. Please enter a numeric value.\n")

    # Input text
    text = input("Enter the text to convert to speech: ").strip()
    if not text:
        text = "Hello! This is a test of the text-to-speech system. I hope you find it helpful."
        print("No text entered. Using default text.\n")

    # Convert text to speech
    text_to_speech(text, voice_index, rate)

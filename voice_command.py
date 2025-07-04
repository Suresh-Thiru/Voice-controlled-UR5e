# voice_command.py

import speech_recognition as sr
from difflib import get_close_matches


def map_command(spoken_text):
    """
    Matches spoken input to the closest valid command.
    """
    valid_commands = ['pick it', 'place it', 'go home', 'bye']
    matches = get_close_matches(spoken_text, valid_commands, n=1, cutoff=0.6)
    if matches:
        return matches[0]
    return None

def recognize_command():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("🎙️ Listening for a command (say: Pick it, Place it, Bye, or Go Home)...")
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"🗣️ Raw input: {command}")
        mapped_command = map_command(command)

        if mapped_command:
            print(f"✅ Mapped command: {mapped_command}")
            return mapped_command
        else:
            print("❌ Unrecognized command.")
            return None

    except sr.UnknownValueError:
        print("❌ Could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"❌ API error: {e}")
        return None

# Run this function to test
if __name__ == "__main__":
    recognize_command()

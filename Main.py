# main.py

import time
from voice_command import recognize_command
from ur_script import send_to_ur5e

def main():
    while True:
        command = recognize_command()
        if command:
            send_to_ur5e(command)
        else:
            print("No valid voice command received. Please try again.")
        time.sleep(1)

if __name__ == "__main__":
    main()

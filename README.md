# Voice-controlled-UR5e

# 🎙️ Voice-Controlled UR5e Robot with Robotiq Gripper

This project demonstrates **voice-command control** of a **Universal Robots UR5e** robotic arm integrated with a **Robotiq gripper** using Python. Users can control the robot to execute pick-and-place actions simply by speaking predefined commands such as "Pick it", "Place it", "Go home", or "Bye".

![WhatsApp Image 2025-07-04 at 17 36 07_49c2e08d](https://github.com/user-attachments/assets/4c76d577-2920-4169-90df-c922801f0a58)



## 📹 Demo Video

Watch the robot in action: https://youtu.be/2efVzOwd7k4

## 🚀 Features

- 🎤 **Voice command recognition** via Google Speech API
- 🤖 Real-time control of UR5e using URScript over TCP/IP
- ✋ Robotiq gripper manipulation (open/close)
- 🏠 Predefined positions for pick, place, and home
- 🔌 Modular Python code structure for reusability

## 🗂️ Project Structure

voice-ur5e-control/
1. main.py             # Main loop to control robot with voice
2. voice_command.py    # Captures and processes voice input
3. ur_script.py        # Sends URScript commands to UR5e
4. requirements.txt    # Python dependencies
5. README.md           # This file


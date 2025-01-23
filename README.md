# Text-to-Speech Python Application

Overview

This Python application converts user-inputted text into speech. It allows users to select a voice, adjust the speech rate, and hear their text spoken aloud. The speech rate is set to 175 words per minute by default, similar to Apple's Siri.

# Features

Choose from multiple available voices.

Adjust speech rate to control speed.

Default settings for ease of use.

Error handling for invalid inputs.

Automatic fallback text if no input is provided.

# Technologies Used

Python 3.x

pyttsx3 library for text-to-speech conversion.

# Installation

Ensure you have Python installed (3.7 or later).

Install the required dependency:

pip install pyttsx3

# Usage

Run the script:

python text_to_speech.py

# Follow the on-screen prompts:

Choose a voice from the available list (press Enter to use the default voice).

Set the speech rate (press Enter to use the default rate of 175).

Input the text to be spoken.

# Example Run

Available Voices:
0: Microsoft David Desktop - English (United States)
1: Microsoft Zira Desktop - English (United States)

Select a voice by index (or press Enter for default): 1
Selected voice 1.

Enter speech rate (default is 175, like Siri):
Using default speech rate of 175.

Enter the text to convert to speech: Hello, this is a test.
Speaking...

# Default Values

Voice: First available voice (index 0)

Speech Rate: 175 (Siri-like speed)

Default Text: "Hello! This is a test of the text-to-speech system. I hope you find it helpful."

# Error Handling

If an invalid voice index is entered, the default voice will be used.

If a non-numeric speech rate is provided, the default rate will be applied.

# Potential Improvements

GUI integration with Tkinter or PyQt.

Save spoken output as an audio file.

Support for additional languages and accents.

# Author

Het Maheta

# Acknowledgments

Python Software Foundation

Contributors to pyttsx3


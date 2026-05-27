# Morse Code Converter

A Python command-line tool that converts text to Morse code and Morse code back to text — with a reference table, demo mode, and clean terminal interface.

## Demo
╔══════════════════════════════════════════╗
║         MORSE CODE CONVERTER             ║
║   Text <-> Morse  |  by Sanjana Banala   ║
╚══════════════════════════════════════════╝
[1] Text  →  Morse code
[2] Morse →  Text
[3] Show reference table
[4] Run demo
[5] Exit

**Example output:**
Input  : HELLO WORLD
Morse  : .... . .-.. .-.. --- / .-- --- .-. .-.. -..
Decoded: HELLO WORLD
Input  : SOS
Morse  : ... --- ...
Decoded: SOS

## Features
- Convert any text (A–Z, 0–9, punctuation) to Morse code
- Decode Morse code back to readable text
- Full reference table for all 26 letters and 10 digits
- Demo mode with sample conversions
- Clean terminal interface

## How to run
**Requirements:** Python 3.x — no external libraries needed.

```bash
git clone https://github.com/2207sanjana/morse-code-converter.git
cd morse-code-converter
python3 morse_converter.py
```

## How it works
Uses a Python dictionary to map every character to its Morse equivalent, and a reverse dictionary for decoding:

```python
MORSE_CODE = {'A': '.-', 'B': '-...', 'S': '...', 'O': '---', ' ': '/'}
REVERSE_MORSE = {v: k for k, v in MORSE_CODE.items()}
```

Words are separated by ` / ` and letters by a single space.

## Skills demonstrated
`Python` `dictionaries` `loops` `functions` `string manipulation` `signal encoding`

## Author
**Sanjana Banala** — M.Sc. ECE, University of Kassel  
[GitHub](https://github.com/2207sanjana)

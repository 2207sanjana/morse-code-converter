# Morse Code Converter

A Python command-line tool that converts text to Morse code and Morse code back to text — with a reference table, demo mode, and clean terminal interface.

## Demo

```
  ╔══════════════════════════════════════════╗
  ║         MORSE CODE CONVERTER             ║
  ║   Text <-> Morse  |  by Sanjana Banala   ║
  ╚══════════════════════════════════════════╝

  What would you like to do?
  [1] Text  →  Morse code
  [2] Morse →  Text
  [3] Show reference table
  [4] Run demo
  [5] Exit
```

**Example output:**
```
  Input  : HELLO WORLD
  Morse  : .... . .-.. .-.. --- / .-- --- .-. .-.. -..
  Decoded: HELLO WORLD

  Input  : SOS
  Morse  : ... --- ...
  Decoded: SOS
```

## Features

- Convert any text (A–Z, 0–9, punctuation) to Morse code
- Decode Morse code back to readable text
- Full reference table for all 26 letters and 10 digits
- Demo mode with sample conversions
- Skips unknown characters gracefully with a notice
- Clean, readable terminal output

## How to run

**Requirements:** Python 3.x — no external libraries needed.

```bash
# Clone the repo
git clone https://github.com/2207sanjana/morse-code-converter.git
cd morse-code-converter

# Run the program
python3 morse_converter.py
```

## Morse code format (for decoding)

| Rule | Example |
|---|---|
| Separate letters with one space | `.... .` = HE |
| Separate words with ` / ` | `... --- ... / -... --- ... -.-. ....` = SOS BOSCH |
| Dots and dashes only | `.` `-` |

## How it works

The program uses a Python **dictionary** to map every character to its Morse code equivalent:

```python
MORSE_CODE = {
    'A': '.-',
    'B': '-...',
    'S': '...',
    'O': '---',
    ' ': '/',
    # ... all 26 letters, digits, punctuation
}
```

For decoding, it builds a **reverse dictionary** automatically:
```python
REVERSE_MORSE = {v: k for k, v in MORSE_CODE.items()}
```

Then splits the input by spaces to decode letter by letter, and by ` / ` to decode word by word.

## Project background

Morse code is a signal encoding system used in radio communications, maritime signalling, and early telecommunications — directly related to signal processing and communication engineering. This project was built to practise Python fundamentals (dictionaries, loops, functions, file I/O) while connecting to real-world signals concepts from my ECE background.

## Skills demonstrated

- Python fundamentals: dictionaries, loops, functions, string manipulation
- Command-line interface design
- Input validation and error handling
- Signal encoding/decoding logic

## Author

**Sanjana Banala**
Master's student — Electrical Communication Engineering, University of Kassel
[GitHub](https://github.com/2207sanjana) · [LinkedIn](https://linkedin.com/in/your-profile)

## License

MIT License — free to use and modify.

"""
Morse Code Converter
Converts text to Morse code and Morse code back to text.
Author: Sanjana Banala
"""

import time
import sys

MORSE_CODE = {
    'A': '.-',   'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.',    'F': '..-.', 'G': '--.',  'H': '....',
    'I': '..',   'J': '.---', 'K': '-.-',  'L': '.-..',
    'M': '--',   'N': '-.',   'O': '---',  'P': '.--.',
    'Q': '--.-', 'R': '.-.',  'S': '...',  'T': '-',
    'U': '..-',  'V': '...-', 'W': '.--',  'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--',
    '-': '-....-', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '_': '..--.-', '"': '.-..-.', '$': '...-..-',
    '@': '.--.-.', ' ': '/'
}

REVERSE_MORSE = {v: k for k, v in MORSE_CODE.items()}


def text_to_morse(text):
    text = text.upper()
    result = []
    unknown = []

    for char in text:
        if char in MORSE_CODE:
            result.append(MORSE_CODE[char])
        else:
            unknown.append(char)

    if unknown:
        print(f"  Note: These characters were skipped (not in Morse): {' '.join(set(unknown))}")

    return ' '.join(result)


def morse_to_text(morse):
    morse = morse.strip()
    words = morse.split(' / ')
    result = []

    for word in words:
        letters = word.strip().split(' ')
        word_result = []
        for code in letters:
            code = code.strip()
            if code == '':
                continue
            if code in REVERSE_MORSE:
                word_result.append(REVERSE_MORSE[code])
            else:
                word_result.append(f'[?{code}]')
        result.append(''.join(word_result))

    return ' '.join(result)


def print_slow(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def show_reference_table():
    print("\n  --- Morse Code Reference Table ---")
    print(f"  {'CHAR':<6} {'CODE':<10}  {'CHAR':<6} {'CODE':<10}")
    print("  " + "-" * 36)
    letters = [(k, v) for k, v in MORSE_CODE.items() if k.isalpha()]
    mid = len(letters) // 2
    for i in range(mid):
        l1, c1 = letters[i]
        l2, c2 = letters[i + mid]
        print(f"  {l1:<6} {c1:<10}  {l2:<6} {c2:<10}")
    print()


def show_banner():
    banner = """
  ╔══════════════════════════════════════════╗
  ║         MORSE CODE CONVERTER             ║
  ║   Text <-> Morse  |  by Sanjana Banala   ║
  ╚══════════════════════════════════════════╝
    """
    print(banner)


def show_menu():
    print("  What would you like to do?")
    print("  [1] Text  →  Morse code")
    print("  [2] Morse →  Text")
    print("  [3] Show reference table")
    print("  [4] Run demo")
    print("  [5] Exit")
    print()


def run_demo():
    demos = [
        "HELLO WORLD",
        "SOS",
        "BOSCH",
        "ECE KASSEL"
    ]
    print("\n  --- Demo Mode ---\n")
    for text in demos:
        morse = text_to_morse(text)
        back = morse_to_text(morse)
        print(f"  Input  : {text}")
        print(f"  Morse  : {morse}")
        print(f"  Decoded: {back}")
        print()
        time.sleep(0.3)


def main():
    show_banner()
    print_slow("  Welcome! This tool converts text to Morse code and back.\n")

    while True:
        show_menu()
        choice = input("  Enter your choice (1-5): ").strip()

        if choice == '1':
            text = input("\n  Enter text to convert: ").strip()
            if not text:
                print("  Please enter some text.\n")
                continue
            morse = text_to_morse(text)
            print(f"\n  Morse code: {morse}\n")

        elif choice == '2':
            print("\n  Morse code format tips:")
            print("  - Separate letters with a single space")
            print("  - Separate words with  /  (space-slash-space)")
            print("  - Example:  .... . .-.. .-.. --- / .-- --- .-. .-.. -..\n")
            morse = input("  Enter Morse code: ").strip()
            if not morse:
                print("  Please enter some Morse code.\n")
                continue
            text = morse_to_text(morse)
            print(f"\n  Decoded text: {text}\n")

        elif choice == '3':
            show_reference_table()

        elif choice == '4':
            run_demo()

        elif choice == '5':
            print_slow("\n  73 de Sanjana (That's Morse for 'Best regards'). Goodbye!\n")
            sys.exit(0)

        else:
            print("  Invalid choice. Please enter 1, 2, 3, 4, or 5.\n")


if __name__ == "__main__":
    main()

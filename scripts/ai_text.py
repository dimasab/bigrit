# ai_text.py
import random
import string
import textwrap
from datetime import datetime
from lorem_text import lorem
from typing import List

def text() -> str:
    """Buat kata."""
    words = kata.words(random.randint(5, 20))
    return words.capitalize()

def random_sentence() -> str:
    """Buat kalimat."""
    sentence = kalimat.sentence()
    return sentence

def random_paragraphs(n: int) -> List[str]:
    """Buat paragraf."""
    paragraphs = [paragraf.paragraph() for _ in range(n)]
    return paragraphs

def wrap_text(text: str, width: int) -> str:
    """Wrap teks."""
    wrapped = textwrap.fill(text, width)
    return wrapped

def capitalize_text(text: str) -> str:
    """Kapitalisasi teks."""
    return text.upper()

def random_alphanumeric_text(length: int) -> str:
    """Alfanumerik."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def random_word(length: int) -> str:
    """Kata."""
    characters = string.ascii_lowercase
    return ''.join(random.choice(characters) for _ in range(length))

def reverse_text(text: str) -> str:
    """Reverse."""
    return text[::-1]

def word_count(text: str) -> int:
    """Perhitungan."""
    return len(text.split())

def unique_words(text: str) -> set:
    """Unik."""
    words = text.split()
    return set(words)

def random_char(lowercase: bool = True) -> str:
    """Karakter"""
    characters = string.ascii_lowercase if lowercase else string.ascii_letters
    return random.choice(characters)

def generate_poem(n_lines: int) -> str:
    poem_lines = [lorem.sentence() for _ in range(n_lines)]
    return "\n".join(poem_lines)

def add_timestamp(text: str) -> str:
    """Timestamp."""
    return f"{text} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

def random_title() -> str:
    """Generates a random title."""
    adjectives = ['Keren', 'Hebat', 'Fantastis', 'Misterius', 'Mengejutkan']
    nouns = ['Petualangan', 'Kisah']
    return f"{random.choice(adjectives)} {random.choice(nouns)}"

def alternating_case(text: str) -> str:
    """Alternating."""
    result = ''.join(char.upper() if i % 2 == 0 else char.lower() for i, char in enumerate(text))
    return result

def encode_to_morse(text: str) -> str:
    morse_code = {
        'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 
        'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
        'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 
        'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 
        'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 
        'z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', 
        '0': '-----', ' ': '/'
    }
    encoded_text = ' '.join(morse_code[char] for char in text.lower() if char in morse_code)
    return encoded_text

def text_summary(text: str) -> str:
    """Ringkasan."""
    words = text.split()
    num_words = len(words)
    return f"Text contains {num_words} words. First 10 words: {' '.join(words[:10])}"

def make_question(text: str) -> str:
    """pertanyaan."""
    if not text.endswith('?'):
        return text.rstrip('.!?') + '?'
    return text

def text_to_pig_latin(text: str) -> str:
    """Latin."""
    def convert_word(word):
        if word[0] in 'aeiou':
            return word + "way"
        else:
            return word[1:] + word[0] + "ay"
    
    words = text.split()
    return ' '.join(convert_word(word) for word in words)

def shuffle_words(text: str) -> str:
    """Gabungkan."""
    words = text.split()
    random.shuffle(words)
    return ' '.join(words)

def emphasize(text: str, character: str = '*') -> str:
    emphasized_text = ' '.join(f"{character}{word}{character}" for word in text.split())
    return emphasized_text

def censor_vowels(text: str) -> str:
    vowels = "aeiou"
    return ''.join('*' if char.lower() in vowels else char for char in text)

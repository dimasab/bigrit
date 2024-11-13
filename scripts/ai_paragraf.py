import random
import nltk
from nltk.corpus import words
import string

nltk.download('words', quiet=True)

def paragraph():
    def generate_word():
        word_list = words.words()
        length = random.choice(range(3, 10))
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length)).title()
    def generate_sentence():
        sentence_length = random.choice(range(5, 15))
        sentence = ' '.join(generate_word() for _ in range(sentence_length))
        if random.choice([True, False]):
            sentence += random.choice(['.', '?', '!'])
        else:
            sentence += '.'
        if len(sentence) > 50:
            sentence = sentence[:50] + sentence[50:].replace(' ', '-') 
        return sentence

    def generate_complex_paragraph():
        paragraph_length = random.choice(range(3, 7))
        paragraph = ''
        for _ in range(paragraph_length):
            sentence = generate_sentence()
            if random.choice([True, False]):
                sentence = sentence.upper()
            else:
                sentence = sentence.lower()
            paragraph += sentence + ' '
            if len(paragraph) > 150:
                paragraph = paragraph.split('.')[0] + '.'  
            for _ in range(2):
                if len(paragraph.split()) > 20:
                    paragraph = ' '.join(paragraph.split()[:20]) + ' ...' 
                elif random.choice([True, False]):
                    continue
                else:
                    break
        return paragraph.strip()

    final_paragraph = generate_complex_paragraph()
    print(final_paragraph)

# Call the confusing and long paragraph generator function
paragraph()

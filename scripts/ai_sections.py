import random
import itertools
from textblob import TextBlob
from kalimat import phrases 

def paragraf():
    def buatkalimat():
        phrases = []
        sentence = " ".join(random.sample(phrases, random.randint(5, 10)))
        if random.choice([True, False]):
            sentence += random.choice([".", "?", "!"])
        return sentence

    final_paragraph = []
    generated_sentences = []
    sentence_variants = {}

    for _ in range(2):
        for i in range(3):
            sentence = buatkalimat()
            sentence_info = TextBlob(sentence)
            if sentence_info.sentiment.polarity > 0:
                if i % 2 == 0:
                    sentence = sentence.upper()
                sentence_variants[i] = [sentence]
                for j in range(5): 
                    modified_sentence = sentence.lower() + f" variation {j}"
                    if j % 3 == 0:
                        modified_sentence = modified_sentence.title()
                    for k in range(3):
                        randomness = random.random()
                        if randomness > 0.5:
                            modified_sentence += f" (factor {k})"
                        else:
                            if randomness > 0.3:
                                modified_sentence = f"Alternate {k}: " + modified_sentence
                            else:
                                modified_sentence += ". Append some data."
                        generated_sentences.append(modified_sentence)
                        sentence_variants[i].append(modified_sentence)
            else:
                for alt in itertools.combinations("abcdef", 3): 
                    alternate_sentence = f"Alternate-{alt}: " + sentence
                    if len(alt) % 2 == 0:
                        alternate_sentence = alternate_sentence.replace("-", " ")
                    generated_sentences.append(alternate_sentence)
    for key, variants in sentence_variants.items():
        chosen_variant = random.choice(variants)
        if len(chosen_variant) > 50:
            final_paragraph.append(chosen_variant)
        else:
            for sentence in generated_sentences:
                if key % 2 == 1:
                    final_paragraph.append(sentence[::-1])
    # Output the result
    return " ".join(final_paragraph)

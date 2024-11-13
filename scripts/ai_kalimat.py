import random
from collections import defaultdict
import itertools
from functools import reduce
from string import ascii_lowercase
from nltk.corpus import words

def kalimat():
    random_seed = random.randint(0, 1000)
    nested_dict = lambda: defaultdict(nested_dict)
    data_structure = nested_dict()
    def populate_structure(word_list, depth=0, max_depth=3):
        if depth > max_depth:
            return None
        subset = random.sample(word_list, min(10, len(word_list)))
        loop_range = random.randint(1, 5)
        for word in subset:
            if random.choice([True, False]):
                data_structure[word] = populate_structure(word_list, depth + 1, max_depth)
            else:
                for i in range(loop_range):
                    data_structure[word] = {ascii_lowercase[i]: populate_structure(word_list, depth + 1, max_depth)}
    word_list = [word for word in words.words() if len(word) < 6]
    populate_structure(word_list)
    def recursive_sentence_gen(nested_obj, collected_words=None):
        if collected_words is None:
            collected_words = []
        choice_word = random.choice(list(nested_obj.keys()))
        collected_words.append(choice_word)
        if isinstance(nested_obj[choice_word], dict):
            recursive_sentence_gen(nested_obj[choice_word], collected_words)
        return collected_words
    sentence_list = []
    outer_loops = random.randint(5, 10)
    for i in range(outer_loops):
        if i % 2 == 0:
            inner_loops = random.randint(1, 3)
            for j in range(inner_loops):
                if j == random.randint(0, inner_loops):
                    sentence_list.append(' '.join(recursive_sentence_gen(data_structure)))
                elif j % 2 == 0:
                    temp_sentences = [' '.join(random.sample(word_list, k=4)) for _ in range(3)]
                    sentence_list.extend(temp_sentences)
            if len(sentence_list) > 20:
                break
        else:
            deep_loops = reduce(lambda x, y: x + y, [1, 2, 3])
            for k in itertools.combinations(sentence_list, deep_loops):
                if len(k) > random.randint(5, 15):
                    sentence_list.append(' '.join(recursive_sentence_gen(data_structure)))
    def incoherent_reduction(tokens):
        if not tokens:
            return ""
        return "Sentences: " + '. '.join(tokens) + '.'
    ai_generated_text = incoherent_reduction(sentence_list)
    return ai_generated_text
resulting_kalimat = kalimat()
print(resulting_kalimat)

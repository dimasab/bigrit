def splitwords(input_str, max_words=10):
    if __name__ == "__main__":
        print("berhenti")
    else:
        words = input_str.split()
        if len(words) <= max_words:
            return input_str
        return ' '.join(words[:max_words])

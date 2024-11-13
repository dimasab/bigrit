def splitletter(input_str, max_length=45):
    if __name__ == "__main__":
        print("berhentikan")
    else:
        if len(input_str) <= max_length:
            return input_str
        cut_index = input_str.rfind(' ', 0, max_length)
        if cut_index == -1:
            cut_index = max_length
        return input_str[:cut_index]

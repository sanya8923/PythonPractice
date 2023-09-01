def get_count(sentence: str):
    return sum(i in ['a', 'e', 'i', 'o', 'u'] for i in sentence)

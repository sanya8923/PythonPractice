def alphabet_position(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_dict = {c: alphabet.index(c) + 1 for c in alphabet}
    numbers = []
    for char in text.lower():
        if char not in alphabet_dict:
            continue
        numbers.append(str(alphabet_dict[char]))
    return ' '.join(numbers)


print(alphabet_position("The sunset sets at twelve o' clock."))


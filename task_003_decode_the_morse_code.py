MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

MORSE_CODE = {values: keys for keys, values in MORSE_CODE_DICT.items()}


def decode_morse(morse_code: str):
    words_list = [word for word in morse_code.strip().split('   ')]
    words_str = ''.join(words_list)
    text = [MORSE_CODE[letter] for letter in words_str.split(' ')]
    return words_list
# ' '.join(''.join(MORSE_CODE[letter] for letter in word.splite(' ')) for word in morse_code.strip().split('   '))


print(decode_morse('..--.. ..---   --.-'))


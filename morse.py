"""
A set of functions for converting from Morse code to English
"""


letter_to_morse = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 
                   'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 
                   'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
                   'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..',
                   '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-',
                   '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
                   ' ':'/' }


def encode(message: str) -> str:
    """
    Given a string of charaters, return the morse message as a string

    Examples:
        >>> encode("sos")
        '... --- ...'
    """
    return ' '.join(letter_to_morse[l] for l in message)


def decode(morse_message: str) -> str:
    """
    Given a morse message, return the english message

    Examples:
        >>> decode("... --- ...")
        'sos'
    """
    morse_to_letter = {v: k for k, v in letter_to_morse.items()}
    return ''.join(morse_to_letter[c] for c in morse_message.split())

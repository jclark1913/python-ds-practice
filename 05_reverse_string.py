def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    str1 = ""
    phrase_list = list(phrase)
    phrase_list.reverse()

    return str1.join(phrase_list)
    
    # return phrase[::-1]
def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    # .upper() converts
    # check if to_swap is lower or upper
    # if lower
        # convert all uppers in phrase to lowercase
    # if to_swap is upper
        # convert all lowercase in phrase to uppercase

    flipped_str = ""

    for letter in phrase:
        if letter.lower() == to_swap.lower():
            if letter.islower():
                flipped_str += letter.upper()
            elif letter.isupper():
                flipped_str += letter.lower()
        else:
            flipped_str += letter
            
    return flipped_str
            

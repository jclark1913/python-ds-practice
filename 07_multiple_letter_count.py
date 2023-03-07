def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    # freq = {}

    freq = {letter: phrase.count(letter) for letter in phrase}

    # dictionary comprehension w/ .count
    # for letter in phrase:
    #     if letter in freq:
    #         freq[letter] += 1
    #     else:
    #         freq[letter] = 1

    return freq
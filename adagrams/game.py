import random
SCORE_CHART = {
        'A': 1, 
        'B': 3, 
        'C': 3, 
        'D': 2, 
        'E': 1, 
        'F': 4, 
        'G': 2, 
        'H': 4, 
        'I': 1, 
        'J': 8, 
        'K': 5, 
        'L': 1, 
        'M': 3, 
        'N': 1, 
        'O': 1, 
        'P': 3, 
        'Q': 10, 
        'R': 1, 
        'S': 1, 
        'T': 1, 
        'U': 1, 
        'V': 4, 
        'W': 4, 
        'X': 8, 
        'Y': 4, 
        'Z': 10
    }

def draw_letters():
    """ Draw letter from letter_pool """
    LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}
    letters = []
   
   # Draw a random letter
    while len(letters) < 10:
        letter = random.choice(list(LETTER_POOL))
        if LETTER_POOL[letter] == 0: # Check letter is in pool
            continue
        else: # Remove one letter from the letter pool
            letters.append(letter)
            LETTER_POOL[letter] -= 1
   
    return letters

def uses_available_letters(word, letter_bank):
    """ check each letter used in leter_bank_copy """
    letter_bank_copy = letter_bank[:]
    word = word.upper()
    for letter in word:
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False
    return True

def score_word(word):
    """Score word using score chart and give bonus points for longer words.""" 
    word = word.upper()
    score = 0
    for letter in word:
        score += SCORE_CHART[letter]
    
    if len(word) > 6:
        score += 8
    
    return score


def get_highest_word_score(word_list):
    """Find highest scoring word and its score."""
    # Score each word in the input list and store word-score pairs in list of tuples
    word_and_score = []
    for word in word_list:
        score = score_word(word)
        score_tuple = (word, score)
        word_and_score.append(score_tuple)
    
    # Create dictionary using word-score pair in each tuple as key and value
    word_and_score_dict = {}
    for word, score in word_and_score:
        word_and_score_dict[word] = score

    highest_score = 0
    best_word = ""
    # Iterate through dictionary and see if new highscore is found
    for word, score in word_and_score_dict.items():
        if score > highest_score:
            highest_score = score
            best_word = word
        # Break tie
        elif score == highest_score:
            if len(word) == 10 and len(best_word) != 10:
                best_word = word
            elif len(word) == 10 and len(best_word) == 10:
                continue
            elif len(word) >= len(best_word):
                continue
            elif len(word) < len(best_word) and len(best_word) != 10:
                best_word = word


    winner_tuple = best_word, highest_score
    return(winner_tuple)

    
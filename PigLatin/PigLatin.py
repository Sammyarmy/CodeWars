def pig_it(text: str):
    words = text.split()
    new_text = ''
    for word in words:
        first_letter = word[:1]
        end_of_word = word[1:]
        print('first letter: ' + first_letter)
        print('end of word: ' + end_of_word)
        new_word = end_of_word + first_letter
        new_text += new_word
        if(new_word.isalpha()):
            new_text += "ay"
        new_text += " "
        print('new text: ' + new_text)
    return new_text.strip()
HANGMAN_ASCII_ART = """  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/"""

print(HANGMAN_ASCII_ART)
index = int(input("Enter a number:"))

MAX_TRIES = 7

def is_valid_input(letter, old_letters):
    if len(letter) != 1:
        return False
    elif letter not in "abcdefghijkmnlopqrstuvwxyz":
        return False
    elif len(letter) != 1 and letter not in "abcdefghijkmnlopqrstuvwxyz":
        return False
    else:
        letter = letter.lower()
        if letter not in old_letters:
            old_letters.append(letter)
        elif letter in old_letters:
            return False
    return old_letters


def show_hidden_word(secret, old_letters):
    word_tmp = secret
    for i in secret:
        if i not in old_letters:
            word_tmp = word_tmp.replace(i, "_ ")
        else:
            continue
    return word_tmp

def check_win(secret, old_guessed):
    for i in secret:
        if i in old_guessed:
            return True
        else:
            return False

HANGMAN_PHOTOS = {1: """x-------x""",
                  2: """    x-------x
    |
    |
    |
    |
    |
""",
                  3: """    x-------x
    |       |
    |       0
    |
    |
    |""",
                  4: """    x-------x
    |       |
    |       0
    |       |
    |
    |""", 5: """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""", 6: """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""", 7: """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""}


def print_hangman(num_tries):
    num_tries += 1
    global HANGMAN_PHOTOS
    print(HANGMAN_PHOTOS[num_tries])

def choose_word(file_path, index):
    file = open(file_path, 'r')
    file_1 = file.read()
    lst = file_1.split(" ")
    word = lst[index]
    file.close()
    return word

def main():
    global index
    global guessed_letter
    num_of_tries = 0
    old_letters_guessed = []
    secret_word = choose_word(r"C:\_download\2019 b\python\hangman\hangman.txt", index)
    word_len = "_ " * len(secret_word)
    print(word_len)

    while num_of_tries != MAX_TRIES:
        guessed_letter = str(input("Enter a letter: "))
        # checks if the letter is valid - in english
        valid = is_valid_input(guessed_letter, old_letters_guessed)
        if valid == False:
            print("this letter in valid")
            # if the letter guessed is right the _ replaced with the letter in the right place
        word_1 = show_hidden_word(secret_word, old_letters_guessed)
        print(word_1)
        print(old_letters_guessed)
        print(print_hangman(num_of_tries))
        num_of_tries += 1
        # the end of the loop
        # checks if the winner won or not

    win = check_win(secret_word, old_letters_guessed)
    if win == True:
        print("congrats! you won!")
    elif win == False:
        print("You lost, maybe next time! ")

if __name__ == '__main__':
    main()
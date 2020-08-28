import random

word_list = ['python', 'java', 'kotlin', 'javascript']
word_choice = random.choice(word_list)
length = len(word_choice)
covered_word = '-' * length
guesses = ''
lives = 8

print('H A N G M A N')
while True:
    menu_choice = input('Type "play" to play the game, "exit" to quit:')
    if menu_choice == 'exit':
        exit()
    if menu_choice == 'play':
        while lives > 0:
            print('')
            print(covered_word)
            if word_choice == covered_word:
                print('You guessed the word!')
                print('You survived!')
                break
            guess = input('Input a letter:')
            if len(guess) != 1:
                print('You should input a single letter')
                continue
            elif ord(guess) < 97 or ord(guess) > 122:
                print('It is not an ASCII lowercase letter')
                continue
            elif guess in guesses:
                print('You already typed this letter')
                continue
            if guess in word_choice:
                for i in range(length):
                    covered_word = list(covered_word)
                    if guess == word_choice[i]:
                        covered_word[i] = guess
                covered_word = ''.join(covered_word)
            else:
                print('No such letter in the word')
                lives -= 1
            guesses += guess
        else:
            print('You are hanged!')
    print('')

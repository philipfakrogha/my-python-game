import random
from question_list import question_list
from quizzes_riddles_art import stages, logo


lives = 6


print(logo)



user_name = input("what is your name?\n")
print(f"""Hello {user_name}, wellcome to Quizzes and Riddles meets Hangman!
This is a game of quizzes and riddles with a man about to be hanged, if you answer correctly, you get
to save the man from being hanged but if you fail to get the correct answer after the given number of tries
the man is hanged and its gameover. Please follow the instructions below carefully:\n
Instructions:  
  * A random question or riddle will be given to you.
  * You will answer the question or riddle by typing a letter or a number at a time in the given blanks,
  (the typed letter or number in the blank must be part of the letters or numbers for the answer, and this 
  is done continuously untill the letters or numbers for the answer is complete in the given blanks).
  * The player is limited to onle 6 tries.
  * GOOD LUCK👍!!!
""")


def game_on():
  game_options = input("Type: 'START' to start the game or 'QUIT' to quit the game!\n").lower()
  if game_options == 'start':
    print("okay! let's play")
    if game_options == 'quit':
      quit()
  else:
    print("Sorry! please check your spellings and try again. Thank you.")
    quit()


game_on()


chosen_word = random.choice(question_list)
question, answer = chosen_word

print(question)


placeholder = ""
word_length = len(answer)
for position in range(word_length):
  placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

print("REMEMBER TO ANSWER THE QUESTION BY GUESSING OR TYPING A LETTER/NUMBER AT A TIME. DO NOT TYPE THE ANSWER ALL AT ONES. THANK YOU.")

while not game_over:
  print(f"**********{lives}/6 LIVES LEFT**********")
  guess = input("Guess a letter: ").lower()

  if guess in correct_letters:
    print(f"You've already guessed {guess}")

  display = ""

  for letter in answer:
    if letter == guess:
      display += letter
      correct_letters.append(guess)
    elif letter in correct_letters:
      display += letter
    else:
      display += "_"

  print("Word to guess: " + display)


  if guess not in answer:
    lives -= 1
    print(f"You guessed {guess}, that's not in the word. You lose a life.")

    if lives == 0:
      game_over = True

      print(f"**********IT WAS {answer}! YOU LOSE AND THE MAN IS HANGED, YOU FAILED TO SAVE HIS LIFE**********")

  if "_" not in display:
    game_over = True
    print(f"**********YOU WIN! WELDONE {user_name}, YOU SAVED THE MAN FROM BEING HANGED.**********")

  print(stages[lives])

 


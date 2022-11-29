
secret_word = "love"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
 if guess_count < guess_limit:
    out_of_guesses = False
    guess = input("Enter your guesss: ")
    guess_count += 1
 else:
     out_of_guesses = True

if out_of_guesses:
    print("wrong guess")
elif not out_of_guesses:
     print("you win!")


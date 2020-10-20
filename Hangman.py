import random

wordList = ["car", "band", "ape", "monkey", "plane", "boat", "cat", "dog", "bird", "mouse"]

word = random.choice(wordList)

looper = True

counter = 10

characterCount = len(word)

underScore = "_ "

while looper == True:
    guess = (str)(input())
    wordCopy = word
    underScores = "_ " * characterCount
    print(underScores)

    if guess == word:
        print("You win")
        looper == False
        
    elif word.count(guess) >= 1:
        print("The Amount of " + (str)(guess) + " is " + (str)(word.count(guess)))
        wordCopyCopy = wordCopy.replace(guess, "_ ")
        
    elif counter <= 0:
        print("You lose.")
        looper = False
    
    counter = counter - 1
    print("You have " + (str)(counter) + " guesses remaining.")
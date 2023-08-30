import random
import tkinter as tk

maxGuesses = 10  # maximum number of guesses
numLength = 3  # number of digits in the mystery number

minNumber = int('1' + '0' * (numLength - 1))  # lowest possible number
maxNumber = int('1' + '0' * numLength)  # highest possible number

mysteryNum = random.randint(minNumber, maxNumber - 1)  # generate a random number
mysteryNumList = [int(x) for x in str(mysteryNum)] # turn the mystery number into a list of digits


def checkAnswer(guess): # checks how accurate the guess is
    rightPosRightPlace = [] # right digit in the right position
    rightPosWrongPlace = [] # right digit in the wrong position

    for i, digit in enumerate(guess):
        if digit == mysteryNumList[i]:
            rightPosRightPlace.append(digit)
        elif digit in mysteryNumList:
            rightPosWrongPlace.append(digit)

    if len(rightPosRightPlace) == numLength: # all digits are correct
        return True
    else:
        resultLabel['text'] = (f"In Right pos: {len(rightPosRightPlace)}\n"
                                f"In Wrong pos: {len(rightPosWrongPlace)}\n"
                                f"Wrong Numbers: {numLength - len(rightPosRightPlace) - len(rightPosWrongPlace)}")
        return False


def game():
    guess = entry.get()
    if not guess.isdigit() or not minNumber <= int(guess) < maxNumber:
        resultLabel['text'] = "Invalid input"
        return

    guessList = [int(x) for x in str(guess)] # turn the guess into a list of digits
    winner = checkAnswer(guessList)
    if winner:
        resultLabel['text'] = "You WIN!!!"
        root.after_cancel(timerId)
    else:
        global tries
        tries += 1
        guessesLeftLabel['text'] = f"Guesses left: {maxGuesses - tries}"
        if tries == maxGuesses: # no more tries left
            resultLabel['text'] = f"Number was: {mysteryNum}\nBetter luck next time!"
            root.after_cancel(timerId)


def updateTimer():
    global timeElapsed, timerId
    timeElapsed += 1
    timerLabel['text'] = f"Time elapsed: {timeElapsed}s"
    timerId = root.after(1000, updateTimer)


# Create the main window
root = tk.Tk()
root.title("Guessing Game")
root.configure(bg="#F0F0F0")

# Create the entry widget for user input
entryLabel = tk.Label(root, text=f"Enter a {numLength}-digit number:", bg="#F0F0F0")
entryLabel.pack()
entry = tk.Entry(root)
entry.pack()

# Create the button to submit the guess
submitButton = tk.Button(root, text="Submit", command=game)
submitButton.pack()

# Create the label to display the result
resultLabel = tk.Label(root, text="", bg="#F0F0F0")
resultLabel.pack()

# Create the label to display the timer
timerLabel = tk.Label(root, text=f"Time elapsed: 0s", bg="#F0F0F0")
timerLabel.pack()

# Create the label to display the number of guesses left
guessesLeftLabel = tk.Label(root, text=f"Guesses left: {maxGuesses}", bg="#F0F0F0")
guessesLeftLabel.pack()

tries = 0
timeElapsed = 0

timerId = root.after(1000, updateTimer)

# Run the main loop
root.mainloop()

import random

MaxGuesses = 10  # maximum number of guesses
NumLength = 3  # no of digits in number, ie 100 is 3-digit number

MinNumber = int('1' + '0' * (NumLength - 1))  # lowest number possible depending on NumLength
MaxNumber = int('1' + '0' * NumLength)  # highest number possible depending on NumLength

MysteryNum = random.randint(MinNumber, MaxNumber - 1)  # generate a random number between MinNum & MaxNum
Allnums = list(range(MinNumber, MaxNumber))  # List of all number between MinNum & MaxNum

MNList = [int(x) for x in str(MysteryNum)] #turn MysteryNum into list to check each number in it


def ValidateNum(): #Validates that input is number
    digit = False
    while not digit:
        num = input('Enter a {} digit number: '.format(NumLength)) #user enters a number
        if num.isdigit() and int(num) in Allnums: #check if input is numerical and between Min & Max numbers
            return int(num)
        else:
            print("Invalid input\n")


def CheckAnswer(guess): #checks how accurate is the answer
    RNRP = [] #Right Position Right Place
    RNWP = [] #Right Position Wrong Place

    for i in range(NumLength):#Loop through each digit of number
        if guess[i] in MNList and guess[i] == MNList[i]:
            RNRP.append(guess[i])
        elif guess[i] in MNList and guess[i] != MNList[i]:
            RNWP.append(guess[i])

    if len(RNRP) == NumLength: #if all Numbers are correct
        return 1
    else:
        print("In Right pos:", len(RNRP),
              "\tIn Wrong pos:", len(RNWP),
              "\tWrong Numbers:", len(guess) - len(RNRP) - len(RNWP),'\n')
        return 0


def Game():
    tries = 0
    print("Welcome to the Guessing game\n"
          "I have a number consisting of {} digits".format(NumLength))
    print('You have {} guesses to figure it out\nGood luck!!\n'.format(MaxGuesses))
    while tries < MaxGuesses:
        guess = ValidateNum() #check if valid input
        Guesslist = [int(x) for x in str(guess)] #turn input into list of digits
        winner = CheckAnswer(Guesslist)
        if winner:
            print("You WIN!!!\n")
            break
        elif not winner:
            tries += 1

    if tries == MaxGuesses: #no more tries
        MysteryNum = ''.join([str(x) for x in MNList]) #return MysteryNum back to num from list of digits
        print("Number was:", MysteryNum, "\nBetter luck next time!")


Game()

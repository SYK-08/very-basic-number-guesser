try:
    def main():
        n = 20
        global tries
        tries = 10
        guess1 = 0
        guess = int(input('Guess a number between 10 and 41 thought by the computer:'))
        if guess>n:
            print('Try a lower number. Tries left:', tries)
        elif guess<n:
            print('Try a greater number. Tries left:', tries)
        elif guess==n:
            print('Great! The number was '+ str(n) + ' and you did it in '+ str(guess1)+' tries.')
        while guess!=n:
            guess1+=1
            tries-=1
            if tries == -1:
                print("Game Over!")
                break
            guess = int(input('Guess the number:'))
            if guess>n:
                print('Try a lower number. Tries left:', tries)
            elif guess<n:
                print('Try a greater number. Tries left:', tries)
            elif guess==n:
                print('Great! The number was '+ str(n) + ' and you did it in '+ str(guess1)+' tries.')
    main()
except ValueError as v:
    print("Invalid input! Please try again.")
    print(main())

try:
    def again():
        while tries == -1:
            z = input("Would you like to play again?(y/n)")
            if z == "n":
                exit('Oh, okay. See ya.')
            elif z == "y":
                print('Great!')
                main()
    again()
except ValueError as w:
    print('Invalid input! Please try again.')
    print(again())

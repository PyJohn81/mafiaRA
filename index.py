from package import keyIn , spit

def main():
    choice = input('What would you like to do? ( new | assign )\n')
    if (choice == 'new'):
        keyIn.keyInFunc()
        spit.spitFunc()
    elif (choice == 'assign'):
        spit.spitFunc()
    else:
        input('Choice not recognized! Try again . . .\n')
        main()

if (__name__ == '__main__'):
    print('Welcome to the Mafia Role Assigner!!!')
    main()
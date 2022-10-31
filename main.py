#Importing requried modules 
import maskpass, os
 
#Different OS use different commands to clear the screen, linux:clear win:cls 
clearing_screen = 'cls'

#Defining The Correct Password and The Password Attempt amount 
correct_password = 'password1'
password_attempt = 11


#Clearing the Screen
os.system(clearing_screen)

#Defining password loop
while True:

    #Checking if the user trys to bypass the password with a keyboard interrupt
    try:

        #Getting the users password input with a security mask
        password_input = maskpass.askpass(prompt="Password: ", mask="*")
        
        #Checking if password is the correct password, if so we break from loop
        if password_input == correct_password:
            break

        #Else, we subtract one from their attempts , and print it to the user 
        password_attempt -= 1
        print(f'Wrong password, you have {password_attempt} remaining')

        #If the user has run out of password attempts then we clear the screen and quit the program
        if password_attempt == 0:
            os.system(clearing_screen)
            print('You have run out of password attempt, goodbye')
            exit()

    except KeyboardInterrupt:
        
        #A taunting message is displayed if the user tries to use KeyboardInterrupt, and the loop continues
        print("Nice try, it won't be that easy")
        continue

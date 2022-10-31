#Importing requried modules 
import maskpass, os
 
#Clearing the Termial 
clearing_screen = 'cls'
os.system(clearing_screen)
correct_password = 'password1'
password_attempt = 11
while True:
    password_input = maskpass.askpass(prompt="Password: ", mask="*")
    if password_input == correct_password:
        break
    password_attempt -= 1
    print(f'Wrong password, you have {password_attempt} remaining')
    if password_attempt == 0:
        os.system(clearing_screen)
        print('You have run out of password attempt, goodbye')
        exit()

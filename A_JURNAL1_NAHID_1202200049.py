
import time
def register():
    username = input("Please enter a username: ")
    print('')
    password = input("Please enter your desired password: ")
    print('')
    file = open("accountfile3.txt","a")
    file.write(username)
    file.write(" ")
    file.write(password)
    file.write("\n")
    file.close()
    if login():
        print("You are now logged in...")
    else:
        print("You aren't logged in!")
def login():
    x = False
    while x == False:
        username = input("Please enter your username: ")
        print('')
        password = input("Please enter your password: ")
        print('')
        for line in open("accountfile3.txt","r").readlines(): # Read the lines
            login_info = line.split() # Split on the space, and store the results in a list of two strings
        if username == login_info[0] and password == login_info[1]:
            print("Correct credentials!")
            return True

        break
    print("Incorrect credentials.")
    print('')
print('Hello')
print('')
time.sleep(1)
print('This is python_workspace')
print('')
time.sleep(1)
print('These are the choices available: ')
print('')
print('|' + '-'*24 + '|')
print('|    1. Register         |')
print('|                        |')
print('|    2. Login            |')
print('|                        |')
print('|    3. Exit             |')
print('|' + '-'*24 + '|')
y = True
while y == True:
    choice1 = input('Please enter the number: ')
    print('')
    if choice1 == '1':
        register()
        break
    elif choice1 == '2':
        login()
        break
    elif choice1 == '3':
        break
    else:
        print('Incorrect input, please enter either: 1, 2, 3')
        print('')
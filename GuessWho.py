import random
peopleDictionary = {
        'Alex': {'eyes':'brown', 'hair':'black ', 'glasses': False, 'gender': 'male'},
        'Alfred': {'eyes': 'blue', 'hair': 'red', 'glasses': False, 'gender': 'male'},
        'Sam': {'eyes': 'brown', 'hair': 'white', 'glasses': True, 'gender': 'male'},
        'Anita': {'eyes': 'blue', 'hair': 'blond', 'glasses': False, 'gender': 'female'},
        'Anne': {'eyes': 'brown', 'hair': 'black', 'glasses': False, 'gender': 'female'},
        'Bernard': {'eyes': 'brown', 'hair': 'brown', 'glasses': True, 'gender': 'male'},
        'Bob': {'eyes': 'blue', 'hair': 'black', 'glasses': True, 'gender': 'male'}
    }
randint = random.randint
secret_person = randint(1,7)
if secret_person == 1:
    secret_person = 'Alex'
elif secret_person == 2:
    secret_person = 'Alfred'
elif secret_person == 3:
    secret_person = 'Sam'
elif secret_person == 4:
    secret_person = 'Anita'
elif secret_person == 5:
    secret_person = 'Anne'
elif secret_person == 6:
    secret_person = 'Bernard'
else:
    secret_person = 'Bob'
def list_people():
    print(peopleDictionary)
def guess(person):
    if person == secret_person.lower():
        return True
    else:
        return False
def eyes(color):
    if color == peopleDictionary[secret_person]['eyes']:
        return True
    else:
        return False
def hair(color):
    if color == peopleDictionary[secret_person]['hair']:
        return True
    else:
        return False
def getHelp():
    print('The eyes, hair color, and person can be guessed. Type guess before guessing the person. ' +
    'Type list for a list of people.')
def glasses():
    return peopleDictionary[secret_person]['glasses']
def gender(gender):
    if peopleDictionary[secret_person]['gender'] == gender:
        return True
    else:
        return False
def split_command(string):
    print()
def main():
    gameOver = False
    counter = 0
    while not gameOver:
        counter += 1
        command = input('What would you like to do? Type help for a list of commands. ').lower()
        command_list = command.split()
        print(command_list)
        if counter < 4:
            if command_list == ['eyes'] or command_list ==['hair'] or command_list == ['guess']:
                print('Enter a valid command. ')
            else:
                if command == 'list':
                    list_people()
                elif 'guess' in command_list:
                    command_list.remove('guess')
                    who = command_list[0]
                    if guess(who) == True:
                        print('That is correct.')
                        gameOver = True
                    else:
                        print('That is incorrect.')
                        gameOver = False
                elif 'eyes' in command_list:
                    command_list.remove('eyes')
                    eye_color = command_list[0]
                    print(eyes(eye_color))
                elif 'hair' in command_list:
                    command_list.remove('hair')
                    hair_color = command_list[0]
                    print(hair(hair_color))
                elif 'help' in command_list:
                    getHelp()
                elif 'glasses' in command_list:
                    print(glasses())
                elif 'male' in command_list or 'female' in command_list:
                    guessed_gender = command_list[0]
                    print(gender(guessed_gender))
                elif 'quit' in command_list:
                    print('You have quit.')
                    gameOver = True
                else:
                    print('Enter a valid command. ')
        else:
            if 'guess' not in command_list:
                print('You must guess now. ')
            else:
                if 'guess' in command_list:
                    command_list.remove('guess')
                    who = command_list[0]
                if guess(who) == True:
                    print('That is correct.')
                    gameOver = True
                else:
                    print('That is incorrect. You lose.')
                    gameOver = True
main()
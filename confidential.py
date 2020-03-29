alphabet = 'abcdefghijklmnopqrstuvwxyz'
#print(alphabet[8])

print('Please enter any key (1-100): ')
key = int(input())

newMessage = ''
message = input('Please enter your message: ')

for character in message:
    if character in alphabet:

        position = alphabet.find(character)
        newPosition = (position + key) % 26
        newCharacter = alphabet[newPosition]
        #print('The new character is: ', newCharacter)
        newMessage += newCharacter
    else:
        newMessage += character
print('Your new message is: ', newMessage)

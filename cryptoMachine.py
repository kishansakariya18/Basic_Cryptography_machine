# What is Cryptography?

# Cryptography is associated with the process of converting ordinary plain text into unintelligible text and vice-versa. It is a method of storing and transmitting data in a particular form so that only those for whom it is intended can read and process it.
def my_cryptography():
    key = 'abcdefghijklmnopqrstuvwxyz !'
    value = key[-1] + key[0 : -1]

    encryptDict = dict(zip(key,value))
    decryptDict = dict(zip(value,key))

    message = input("please enter your your secret message : ")
    mode = input("Please Enter the mode : Encode(E) or Decode(D) : ")

    if mode.upper() == 'E':
        newMessage = ''.join([encryptDict[letter] for letter in message.lower()])  #creact new string
    elif mode.upper() == 'D':
        newMessage = ''.join([decryptDict[letter] for letter in message.lower()])
    else:
        print("Please Enter a correct choice")
    return newMessage.capitalize()
print(my_cryptography())


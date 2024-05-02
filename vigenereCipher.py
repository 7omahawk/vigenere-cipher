# making vigenere cipher cipher encryption and decryption using python

import sys
domain = 26
string = "abcdefghijklmnopqrstuvwxyz"


# converting key value to number and making keyStream size as userInput size
def theKey(userInput, key, string):
    
    keyStream = ()   # making tuples for indvidually identify the alphabetes numbers instead of string
    counter = 0

    while(counter <= len(userInput)):
        for m in range(len(key)):
            for n in range(len(string)):
                if string[n] == key[m]:

                    keyStream = keyStream + (n,)
        counter += len(key)

    keyStream = keyStream[:len(userInput)]
    return keyStream


def encryption(userInput, key, domain, string):
    
    cipher = ""
    theKey(userInput, key, string)

    k = theKey(userInput, key, string)

    for i in range(len(userInput)):
        for j in range(len(string)):
            if string[j] == userInput[i]:
                text = (string[(j+k[i])%domain])
                cipher = cipher + text
    
    print(f"The encrypted message is: {cipher}")
    print('\n')


def decryption(userInput, key, domain, string):
    
    plainText = ""
    theKey(userInput, key, string)

    k = theKey(userInput, key, string)

    for i in range(len(userInput)):
        for j in range(len(string)):
            if string[j] == userInput[i]:
                text = (string[(j-k[i])%domain])
                plainText = plainText + text
    
    print(f"The decrypted message is: {plainText}")
    print('\n')


while(True):
    print("Enter your choice(Number): ")
    print("1. Encryption: ")
    print("2. Decryption: ")
    print("3. Exit: ")

    number = int(input("Enter the number: "))

    def choice(number):
        if number == 1:
            userInput = input("Enter your text to encrypt: ")
            key = input("Enter the key: ")
            userInput = userInput.lower()
            encryption(userInput, key, domain, string)
        elif number == 2:
            userInput = input("Enter your text to decrypt: ")
            key = input("Enter the key: ")
            userInput = userInput.lower()
            decryption(userInput, key, domain, string)
        elif number == 3:
            sys.exit()
        else:
            print("Input should be a number from 1 to 3")

    choice(number) 
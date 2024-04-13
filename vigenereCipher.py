# making vigenere cipher cipher encryption and decryption using python

import sys
domain = 26
string = "abcdefghijklmnopqrstuvwxyz"

def keyValue(key):
    k = ""
    for i in range(len(key)):
        for j in range(len(string)):
            if string[j] == key[i]:
                k = k + str(j)      # the value of the key
                print(k)
                # return k


def encryption(userInput, key, domain, string):
    
    
    cipher = ""
    for i in range(len(userInput)):
        for j in range(len(string)):
            if string[j] == userInput[i]:
                # k = keyValue(key)
                k = keyValue(key)
                # mainKey = int(str(k)[::-1])   #inverse the value of q by string slicing reverse method
                # fakeKey = mainKey
                # mainKey = fakeKey % 10
                # mainKey = int(fakeKey / 10)
                mainKey = 1
                text = (string[(j+mainKey)%domain])
                cipher = cipher + text
    

                
    print(f"The encrypted message is: {cipher}")
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
            print(key)
            userInput = userInput.lower()
            encryption(userInput, key, domain, string)
        elif number == 2:
            userInput = input("Enter your text to decrypt: ")
            key = int(input("Enter the key: "))
            userInput = userInput.lower()
        elif number == 3:
            sys.exit()
        else:
            print("Input should be a number from 1 to 3")

    choice(number) 




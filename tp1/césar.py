# -*- coding: utf-8 -*-

import time

def cesar():
    letters = "abcdefghijklmnopqrstuvwxyz"
    print("Please enter your string > ")
    string_to_encode = input()
    print("Please enter your shift > ")
    cipher_shift = input()
    string_to_encode = string_to_encode.lower()
    cipher_shift = int(cipher_shift)
    string_encrypted = ""
    start_time = time.time()
    for character in string_to_encode:
        position = letters.find(character)
        new_position = (position + cipher_shift) % 26
        if character in letters:
            string_encrypted = string_encrypted + letters[new_position]
        else:
            string_encrypted = string_encrypted + character
    print("Cipher shift > "+ str(cipher_shift))
    print("Message      > "+ str(string_encrypted))
    print("--- %s seconds ---" % (time.time() - start_time))

def cesarBrut():
    letters = "abcdefghijklmnopqrstuvwxyz"
    print("Please enter your string > ")
    string_to_encode = input()
    
    listRes = []
    for cipher_shift in range(0, 26):
        string_to_encode = string_to_encode.lower()
        cipher_shift = int(cipher_shift)
        string_encrypted = ""
        for character in string_to_encode:
            position = letters.find(character)
            new_position = (position + cipher_shift) % 26
            if character in letters:
                string_encrypted = string_encrypted + letters[new_position]
            else:
                string_encrypted = string_encrypted + character
        listRes += [string_encrypted]
    print(listRes)
    
def cesarBrutCorrection():
    letters = "abcdefghijklmnopqrstuvwxyz"
    print("Please enter your encoded string > ")
    encoded_string = input()
    start_time = time.time()
    x = 0
    while x < 26:
        x = x + 1
        string_to_decrypt = encoded_string.lower()
        cipher_shift = int(x)
        string_decrypted = ""
        for character in string_to_decrypt:
            position = letters.find(character)
            new_position = position - cipher_shift
            if character in letters:
                string_decrypted = string_decrypted + letters[new_position]
            else:
                string_decrypted = string_decrypted + character
        print("Cipher shift > "+ str(cipher_shift))
        print("Message      > "+ str(string_decrypted))
    print("--- %s seconds ---" % (time.time() - start_time))
        
cesarBrutCorrection()
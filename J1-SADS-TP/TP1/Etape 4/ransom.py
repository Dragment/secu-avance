from os import listdir
from os.path import isfile, join

def cesar(string, shift):
    letters = "abcdefghijklmnopqrstuvwxyz"
    string_to_encode = string
    cipher_shift = shift
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
    return string_encrypted



    #recover all files of path
def all_files():
    files = []
    for f in listdir("./TEST/"):
        if isfile(join("./TEST/", f)):
            files.append(join("./TEST/", f))
    return files

files_list = all_files()

for f in files_list:
    file_content = open(f,"r")
    new_file = open(f+".encrypted","w")
    for line in file_content:
        cesared_line = cesar(str(line), 7)
        new_file.write(cesared_line+"\n")

    file_content.close()
    new_file.close()
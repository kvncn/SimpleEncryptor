###
### Author: Kevin Cascais Nisterenko
### Course: CSc 110
### Description: My program/solution for Decrypter PA - Week 9.
###              This program decrypts an encrypted text file
###              using its key for the decription algorithm and then
###              the program writes the decrypted file. For this purpose
###              4 functions are defined. The get_files function asks the user
###              for an encrypted file and an index/key file and then it creates
###              a list for each file in which every line is an element of the
###              lists. Then, the program runs the decryption_algorithm function
###              with these lists as parameters. To decrypt the file it
###              first creates a list of empty strings that are concatonated using
###              a for loop that creates a position variable to then do the concatonation
###              at the correct index. Then the write_decrypted_file function uses a for
###              loop to iterate through the decrypted file list and write the contents
###              into a file. Lastly, main is called and it calls the aforementioned functions.
###              Obs. in line 41 and 42, the use of .readlines() in the same line as the open()
###              method was shown by Jason (TA) during class.
###

def main():
    # Gets the index file list and encrypted file list.
    encrypted_file, index_file = get_files()

    # Performs the decryption algorithm on the encrypted file list.
    decrypted_list = decryption_algorithm(encrypted_file, index_file)

    # Writes the decrypted file.
    write_decrypted_file(decrypted_list)

def get_files():
    '''
    This function will ask the user input for the encrypted file
    and the index file, it will open these files and read all lines into
    a respective list for each file. The function returns the lists of
    all lines in the file and the list of indexes.
    '''
    encrypted_file_name = input('Enter the name of an encrypted text file:\n')
    index_file_name = input('Enter the name of the encryption index file:\n')

    encrypted_file_list = open(encrypted_file_name, 'r').readlines()
    index_file_list = open(index_file_name, 'r').readlines()

    return encrypted_file_list, index_file_list

def decryption_algorithm(encrypted_file_list, index_file_list):
    '''
    This function first creates a decrypted list the same length
    as the encrypted file list, however, all elements are empty strings.
    Then the function uses a for loop to find the index in index list and
    concatonates the appropriate element of the encrypted file list in
    the correct position. Then the function returns the decrypted list, with
    all elements (lines) in the correct order.
    encrypted_file_list: encrypted_file_list: list of lines of encrypted file.
    index_file_list: list of indexes of the encrypted file.
    '''
    # Sets a list of empty strings that will be concatonated in the for loop.
    decrypted_list = [''] * len(encrypted_file_list)

    # Concatonates the appropriate line by looking at index list and encrypted
    # file list.
    for i in range(0, len(encrypted_file_list)):
        # It is subtracted by 1 because otherwise it will not have a base 0 index.
        position = int(index_file_list[i]) - 1
        decrypted_list[position] += encrypted_file_list[i]

    return decrypted_list

def write_decrypted_file(decrypted_list):
    '''
    This function uses a for loop to
    add the newline character for all lines
    and remove it on the last line of the decrypted
    file list. It also uses the for loop to write
    all of the lines in a new file.
    decrypted_file: list of lines of the original
                    file in the correct order
                    (after decryption).
    '''
    decrypted_file = open('decrypted.txt', 'w')

    # This loop will write every element of the decrypted
    # file as a line in .txt file. It also ensures that every
    # line but the last will have a newline character.
    for line in decrypted_list:
        if '\n' not in line:
            line += '\n'
        if line == decrypted_list[-1]:
            line.strip('\n')
        decrypted_file.write(line)

    decrypted_file.close()

main()
###
### Author: Kevin Cascais Nisterenko
### Course: CSc 110
### Description: My program/solution for Encrypter PA - Week 9.
###              This program encrypts a text file and creates two
###              new files, an encrypted file and an encryption index/key
###              file. For this purpose this program defines 7 functions. The
###              get_file_to_encrypt function gets user input of a file and creates
###              a list of all lines in the file. The get_index_list function creates
###              a list of integers that represent the line numbers/index of the input
###              file. The swap_elements function performs a single element swap in a
###              a list and for this program it is called inside the while loop of the
###              encrypter_algorithm function, which will mix the elements in the lists
###              in a random order and return these two lists after they are encrypted.
###              The write_encrypted_file function uses a for loop to write the lines of
###              the encrypted list in a new file and the write_key_file will use a similar
###              process to create the index/key file. In order to then work, the program
###              defines main, which sets the random seed and calls the appropriate functions
###              to create the two encrypted files. Obs. in line 47, the use of .readlines()
###              in the same line as the open() method was shown by Jason (TA) during class.
###

import random

def main():
    random.seed(125)

    # Gets the input file list and index list.
    file_list = get_file_to_encrypt()
    index_list = get_index_list(file_list)

    # Perform the encryption and return the lists.
    encrypted_file_list, encrypted_index_list = encrypter_algorithm(file_list, index_list)

    # Write the two files.
    write_encrypted_file(encrypted_file_list)
    write_key_file(index_list)

def get_file_to_encrypt():
    '''
    This function will ask the user input for the file to
    encrypt, it will open the file and read all lines into
    a list. The function returns the list of all lines in
    the file.
    '''
    file_to_encrypt_name = input('Enter a name of a text file to encrypt:\n')
    file_to_encrypt = open(file_to_encrypt_name, 'r').readlines()

    return file_to_encrypt

def get_index_list(file_to_encrypt):
    '''
    This function uses a for loop that iterates through
    the length of original file to create a list
    of indexes (before encryption) and each index
    corresponds to a line in the original file.
    After the loop runs the function returns the index
    list.
    file_to_encrypt: list of lines of the original file
                     (file before encryption).
    '''
    index_list = []

    # Iterates from 1 to length of file list to create the index
    # list.
    for i in range(1, len(file_to_encrypt)+1):
        index_list.append(i)

    return index_list

def swap_elements(lst, first_random_int, second_random_int):
    '''
    This function performs a single element swap in a passed
    list by variable and index reassignment.
    lst: any list, in the case of this program this function will
         be used with the index and file lists.
    first_random_int: integer used in the indexes of the list elements.
    second_random_int: integer used in the indexes of the list elements.
    '''

    # These lines perform the swapping.
    temp_file_lst = lst[first_random_int]
    lst[first_random_int] = lst[second_random_int]
    lst[second_random_int] = temp_file_lst

def encrypter_algorithm(file_list, index_list):
    '''
    This function uses a while loop to iterate
    through both lists and perform the element swap
    with the random numbers by calling the swap_elements
    function with the random integers and lists as arguments.
    The function then returns the encrypted file list and the index list.
    file_list: list of lines of the original file
               (file before encryption).
    index_list: list of indexes of the original file
                (file before encryption).
    '''
    i = 0
    # This loop runs 5 times the number of lines following the algorithm
    # in the spec.
    while i < len(file_list) * 5:
        # The random integers are reassigned in each iteration so that different
        # lines are shuffled.
        first_random_int = random.randint(0, len(file_list)-1)
        second_random_int = random.randint(0, len(file_list)-1)
        # Both lists are swapped so that the indexes and lines coincide.
        swap_elements(file_list, first_random_int, second_random_int)
        swap_elements(index_list, first_random_int, second_random_int)
        i += 1

    return file_list, index_list

def write_encrypted_file(encrypted_file_list):
    '''
    This function uses a for loop to
    add the newline character for all lines
    and remove it on the last line of the encrypted
    file list. It also uses the for loop to write
    all of the lines in a new file.
    encrypted_file_list: list of lines of the original
                         file in a randomized order
                         (after encryption).
    '''
    encrypted_file = open('encrypted.txt', 'w')

    # This loop will write every element of the encrypted
    # file as a line in .txt file. It also ensures that every
    # line but the last will have a newline character.
    for line in encrypted_file_list:
        if '\n' not in line:
            line += '\n'
        if line == encrypted_file_list[-1]:
            line.strip('\n')
        encrypted_file.write(line)

    encrypted_file.close()

def write_key_file(index_list):
    '''
    This function uses a for loop to
    add the newline character for all lines
    of the index list excetp the last one.
    It also uses the for loop to write
    all of the lines in a new file.
    index_ist: list of indexes of the original
               file in a randomized order
               (after encryption).
    '''
    index_file = open('index.txt', 'w')

    # This loop will write every element of the index
    # file as a line in .txt file. It also ensures that every
    # line but the last will have a newline character.
    for line in index_list:
        line = str(line)
        if line != index_list[-1]:
            line += '\n'
        index_file.write(line)

    index_file.close()

main()
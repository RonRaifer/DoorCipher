# Ron Raifer

from q1_decrypt import Decrypt
from q1_encrypt import Encrypt
from q2_attack import IterativeAttack


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def door_cipher():
    ptext = input("Enter Text: ")
    while len(ptext) < 2:
        ptext = input(bcolors.WARNING + "PlainText must contain at least 2 chars" + bcolors.ENDC + "\nEnter Text: ")
    key = input("Enter Key [4 chars only*]: ")
    while len(key) != 4:
        key = input(bcolors.WARNING + "Key must be 4 chars" + bcolors.ENDC + "\nEnter Key [4 chars only*]: ")

    # DOOR ENCRYPTION
    encrypt = Encrypt()
    keymatrix_final, cipher_text = encrypt.door_encryption(ptext, key)
    cipher_str = ''.join(cipher_text)
    print(bcolors.BOLD + "\nEncrypted text: " + bcolors.ENDC + bcolors.OKBLUE + cipher_str + bcolors.ENDC)
    print(bcolors.BOLD + "Calculated Key: " + bcolors.ENDC, keymatrix_final)

    # DOOR DECRYPTION
    # decrypt = Decrypt()
    # keymatrix_final, decipher_text = decrypt.door_decryption(cipher_str, key)
    # decipher_str = ''.join(decipher_text)
    # print(bcolors.BOLD + "Decrypted text: " + bcolors.ENDC + bcolors.OKBLUE + decipher_str + bcolors.ENDC)
    # print(bcolors.BOLD + "Calculated Key: " + bcolors.ENDC, keymatrix_final)

    # ITERATIVE ATTACK
    # attack = IterativeAttack()
    # attack_txt, iternum = attack.attack(cipher_str, key)
    # print(bcolors.BOLD + "\nAttacked encrypted text result: " + bcolors.ENDC +
    #      bcolors.OKBLUE + attack_txt + bcolors.ENDC +
    #      bcolors.BOLD + " Number of iterations: " + bcolors.ENDC, iternum)


door_cipher()

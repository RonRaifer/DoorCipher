# Ron Raifer
from q1_encrypt import Encrypt


class IterativeAttack:
    def attack(self, ctext, key):
        encrypt = Encrypt()
        ptext = ctext
        number_of_iterations = 0
        k, encrypted_txt = encrypt.door_encryption(ctext, key)
        encrypted_txt = ''.join(encrypted_txt)
        while encrypted_txt != ctext:
            ptext = encrypted_txt
            k, encrypted_txt = encrypt.door_encryption(encrypted_txt, key)
            encrypted_txt = ''.join(encrypted_txt)
            number_of_iterations += 1
        return ptext, number_of_iterations

# Ron Raifer
import functions


class Encrypt:
    def door_encryption(self, ptext, key):
        f = functions.Functions()
        keymatrix = f.string_to_key_matrix(key)
        # calc key matrix
        keymatrix_final = f.keymatrix_calculation(keymatrix)
        if f.inverse_num_calculation(f.determinant_calculation(keymatrix_final)) == -1:
            print("\n\nKey Matrix is not invertible!\n")
            print(keymatrix)
            exit(1)
        text_new = ptext
        # in case text length is odd
        if len(ptext) % 2 == 1:
            text_new += 'A'
        slices = [0, 0]
        i = 0
        cipher_text = [0 for x in range(len(text_new))]
        while i < len(text_new):
            slices[0] = f.cvt_char_to_int(text_new[i])
            slices[1] = f.cvt_char_to_int(text_new[i+1])
            vec = f.vec_mat_mul_calculation(slices, keymatrix_final)
            cipher_text[i] = f.cvt_int_to_char(vec[0])
            cipher_text[i+1] = f.cvt_int_to_char(vec[1])
            i += 2
        return keymatrix_final, cipher_text

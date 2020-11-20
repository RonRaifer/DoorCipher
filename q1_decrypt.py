# Ron Raifer
import functions


class Decrypt:
    def door_decryption(self, ctext, key):
        f = functions.Functions()
        keymatrix = f.string_to_key_matrix(key)
        #
        keymatrix_tmp = f.keymatrix_calculation(keymatrix)
        keymatrix_final = f.inverse_mat_calculation(keymatrix_tmp)
        #
        slices = [0, 0]
        i = 0
        decipher_text = [0 for x in range(len(ctext))]
        while i < len(ctext):
            slices[0] = f.cvt_char_to_int(ctext[i])
            slices[1] = f.cvt_char_to_int(ctext[i+1])
            vec = f.vec_mat_mul_calculation(slices, keymatrix_final)
            decipher_text[i] = f.cvt_int_to_char(vec[0])
            decipher_text[i+1] = f.cvt_int_to_char(vec[1])
            i += 2
        return keymatrix_final, decipher_text